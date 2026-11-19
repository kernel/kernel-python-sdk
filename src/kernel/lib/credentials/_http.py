from __future__ import annotations

from typing import Dict, Mapping, Optional, NamedTuple

import httpx

from ._errors import WorkloadIdentityError
from ._constants import MAX_RESPONSE_BYTES, TOKEN_EXCHANGE_TIMEOUT, user_agent

__all__ = ["BoundedResponse", "send", "async_send"]


class BoundedResponse(NamedTuple):
    status_code: int
    headers: httpx.Headers
    content: bytes


def _build_request(
    method: str, url: str, *, headers: Mapping[str, str], data: Optional[Dict[str, str]]
) -> httpx.Request:
    # Built without the HTTP client: it is usually the API client's, and its
    # default headers, query parameters and cookies are meant for the API.
    return httpx.Request(
        method,
        url,
        # identity: the size limit below counts bytes as they arrive, which a compressed body would defeat.
        headers={"Accept-Encoding": "identity", "User-Agent": user_agent(), **headers},
        data=data,
        extensions={"timeout": httpx.Timeout(TOKEN_EXCHANGE_TIMEOUT).as_dict()},
    )


def _too_large(what: str) -> WorkloadIdentityError:
    return WorkloadIdentityError(
        f"The response from {what} is larger than {MAX_RESPONSE_BYTES} bytes; refusing to read it."
    )


def _check_headers(response: httpx.Response, what: str) -> None:
    # With no content encoding, reading the body yields the bytes as they
    # arrive, so the size limit applies to what is actually held in memory.
    encoding = response.headers.get("Content-Encoding", "identity").strip().lower()
    if encoding not in ("", "identity"):
        raise WorkloadIdentityError(f"The response from {what} has a content encoding, although none was accepted.")
    length = response.headers.get("Content-Length", "")
    if length.isdigit() and int(length) > MAX_RESPONSE_BYTES:
        raise _too_large(what)


def _unreachable(what: str, url: str, err: httpx.HTTPError) -> WorkloadIdentityError:
    return WorkloadIdentityError(f"Failed to reach {what} at {url}: {err or type(err).__name__}")


def _protocol_error(what: str, url: str, err: httpx.ProtocolError) -> WorkloadIdentityError:
    if isinstance(err, httpx.LocalProtocolError):
        return WorkloadIdentityError(
            f"The request to {what} at {url} could not be sent (LocalProtocolError). "
            "Check the configured token and URL for stray whitespace or control characters."
        )
    return WorkloadIdentityError(f"The response from {what} at {url} was not valid HTTP ({type(err).__name__}).")


def send(
    http_client: Optional[httpx.Client],
    method: str,
    url: str,
    *,
    headers: Mapping[str, str],
    data: Optional[Dict[str, str]] = None,
    what: str,
    trust_env: bool = True,
) -> BoundedResponse:
    """Send one request and read at most `MAX_RESPONSE_BYTES` of the response.

    The request goes through `http_client`'s transport, so its proxies apply,
    but carries only the given headers: none of the client's default headers,
    query parameters or auth. Redirects are not followed, so the credentials
    in the request reach only the URL they were meant for.
    `http_client=None` uses a new client for this request; `trust_env=False`
    makes that client ignore proxy settings from the environment.
    """
    if http_client is None:
        with httpx.Client(trust_env=trust_env) as own_client:
            return send(own_client, method, url, headers=headers, data=data, what=what)

    request = _build_request(method, url, headers=headers, data=data)
    try:
        response = http_client.send(request, stream=True, auth=None, follow_redirects=False)
        try:
            _check_headers(response, what)
            chunks: list[bytes] = []
            size = 0
            for chunk in response.iter_bytes():
                size += len(chunk)
                if size > MAX_RESPONSE_BYTES:
                    raise _too_large(what)
                chunks.append(chunk)
        finally:
            response.close()
    except httpx.ProtocolError as err:
        # The HTTP stack's message quotes the header line it could not send or
        # parse, which can hold a credential, so neither it nor the chain is kept.
        raise _protocol_error(what, url, err) from None
    except httpx.HTTPError as err:
        raise _unreachable(what, url, err) from err
    return BoundedResponse(response.status_code, response.headers, b"".join(chunks))


async def async_send(
    http_client: Optional[httpx.AsyncClient],
    method: str,
    url: str,
    *,
    headers: Mapping[str, str],
    data: Optional[Dict[str, str]] = None,
    what: str,
    trust_env: bool = True,
) -> BoundedResponse:
    """Async version of `send`."""
    if http_client is None:
        async with httpx.AsyncClient(trust_env=trust_env) as own_client:
            return await async_send(own_client, method, url, headers=headers, data=data, what=what)

    request = _build_request(method, url, headers=headers, data=data)
    try:
        response = await http_client.send(request, stream=True, auth=None, follow_redirects=False)
        try:
            _check_headers(response, what)
            chunks: list[bytes] = []
            size = 0
            async for chunk in response.aiter_bytes():
                size += len(chunk)
                if size > MAX_RESPONSE_BYTES:
                    raise _too_large(what)
                chunks.append(chunk)
        finally:
            await response.aclose()
    except httpx.ProtocolError as err:
        # The HTTP stack's message quotes the header line it could not send or
        # parse, which can hold a credential, so neither it nor the chain is kept.
        raise _protocol_error(what, url, err) from None
    except httpx.HTTPError as err:
        raise _unreachable(what, url, err) from err
    return BoundedResponse(response.status_code, response.headers, b"".join(chunks))
