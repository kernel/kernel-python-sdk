from __future__ import annotations

from collections.abc import AsyncIterator, Iterable, Iterator
from contextlib import asynccontextmanager, contextmanager
from typing import IO, Any, Mapping, cast

import httpx

from ..._models import FinalRequestOptions
from ..._types import BinaryTypes, Body, NotGiven, Timeout, not_given
from .routing import BrowserRoute
from .util import sanitize_curl_raw_params


def request_via_browser_route(
    parent: Any,
    route: BrowserRoute,
    method: str,
    url: str,
    *,
    content: BinaryTypes | None = None,
    json: Body | None = None,
    headers: Mapping[str, str] | None = None,
    params: Mapping[str, object] | None = None,
    timeout: float | Timeout | None | NotGiven = not_given,
) -> httpx.Response:
    if json is not None and content is not None:
        raise TypeError("Passing both `json` and `content` is not supported")
    query: dict[str, object] = {**sanitize_curl_raw_params(params), "url": url, "jwt": route.jwt}
    options = FinalRequestOptions.construct(
        method=method.upper(),
        url=route.base_url.rstrip("/") + "/curl/raw",
        params=query,
        headers=headers or {},
        content=_normalize_binary_content(content),
        json_data=json,
        timeout=timeout,
    )
    return cast(httpx.Response, parent.request(httpx.Response, options))


@contextmanager
def stream_via_browser_route(
    parent: Any,
    route: BrowserRoute,
    method: str,
    url: str,
    *,
    content: BinaryTypes | None = None,
    headers: Mapping[str, str] | None = None,
    params: Mapping[str, object] | None = None,
    timeout: float | Timeout | None | NotGiven = not_given,
) -> Iterator[httpx.Response]:
    query: dict[str, Any] = sanitize_curl_raw_params(params)
    query["jwt"] = route.jwt
    query["url"] = url
    request_headers = {k: v for k, v in parent.default_headers.items() if isinstance(v, str)}
    if content is None:
        request_headers.pop("Content-Type", None)
    if headers:
        request_headers.update(headers)
    request_headers.pop("Authorization", None)
    effective_timeout = parent.timeout if isinstance(timeout, NotGiven) else timeout
    with parent._client.stream(
        method.upper(),
        route.base_url.rstrip("/") + "/curl/raw",
        params=query,
        headers=request_headers,
        content=_normalize_binary_content(content),
        timeout=_normalize_timeout(effective_timeout),
    ) as response:
        yield response


async def async_request_via_browser_route(
    parent: Any,
    route: BrowserRoute,
    method: str,
    url: str,
    *,
    content: BinaryTypes | None = None,
    json: Body | None = None,
    headers: Mapping[str, str] | None = None,
    params: Mapping[str, object] | None = None,
    timeout: float | Timeout | None | NotGiven = not_given,
) -> httpx.Response:
    if json is not None and content is not None:
        raise TypeError("Passing both `json` and `content` is not supported")
    query: dict[str, object] = {**sanitize_curl_raw_params(params), "url": url, "jwt": route.jwt}
    options = FinalRequestOptions.construct(
        method=method.upper(),
        url=route.base_url.rstrip("/") + "/curl/raw",
        params=query,
        headers=headers or {},
        content=_normalize_binary_content(content),
        json_data=json,
        timeout=timeout,
    )
    return cast(httpx.Response, await parent.request(httpx.Response, options))


@asynccontextmanager
async def async_stream_via_browser_route(
    parent: Any,
    route: BrowserRoute,
    method: str,
    url: str,
    *,
    content: BinaryTypes | None = None,
    headers: Mapping[str, str] | None = None,
    params: Mapping[str, object] | None = None,
    timeout: float | Timeout | None | NotGiven = not_given,
) -> AsyncIterator[httpx.Response]:
    query: dict[str, Any] = sanitize_curl_raw_params(params)
    query["jwt"] = route.jwt
    query["url"] = url
    request_headers = {k: v for k, v in parent.default_headers.items() if isinstance(v, str)}
    if content is None:
        request_headers.pop("Content-Type", None)
    if headers:
        request_headers.update(headers)
    request_headers.pop("Authorization", None)
    effective_timeout = parent.timeout if isinstance(timeout, NotGiven) else timeout
    async with parent._client.stream(
        method.upper(),
        route.base_url.rstrip("/") + "/curl/raw",
        params=query,
        headers=request_headers,
        content=_normalize_binary_content(content),
        timeout=_normalize_timeout(effective_timeout),
    ) as response:
        yield response


def _normalize_timeout(timeout: float | Timeout | None | NotGiven) -> float | Timeout | None:
    return None if isinstance(timeout, NotGiven) else timeout


def _normalize_binary_content(content: BinaryTypes | None) -> bytes | IO[bytes] | Iterable[bytes] | None:
    if content is None:
        return None
    if isinstance(content, bytearray):
        return bytes(content)
    if isinstance(content, memoryview):
        return content.tobytes()
    return content
