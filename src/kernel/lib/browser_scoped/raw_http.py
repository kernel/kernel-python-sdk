from __future__ import annotations

from contextlib import asynccontextmanager, contextmanager
from typing import IO, Any, Mapping, cast
from collections.abc import AsyncIterator, Iterable, Iterator

import httpx

from ..._models import FinalRequestOptions
from ..._types import Body, BinaryTypes, NotGiven, Timeout, not_given
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
    q: dict[str, object] = {**sanitize_curl_raw_params(params), "url": url}
    q["jwt"] = route.jwt
    opts = FinalRequestOptions.construct(
        method=method.upper(),
        url=route.base_url.rstrip("/") + "/curl/raw",
        params=q,
        headers=headers or {},
        content=_normalize_binary_content(content),
        json_data=json,
        timeout=timeout,
    )
    return cast(httpx.Response, parent.request(httpx.Response, opts))


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
    q: dict[str, Any] = sanitize_curl_raw_params(params)
    q["jwt"] = route.jwt
    q["url"] = url
    h = {k: v for k, v in parent.default_headers.items() if isinstance(v, str)}
    if content is None:
        h.pop("Content-Type", None)
    if headers:
        h.update(headers)
    h.pop("Authorization", None)
    eff_timeout = parent.timeout if isinstance(timeout, NotGiven) else timeout
    with parent._client.stream(
        method.upper(),
        route.base_url.rstrip("/") + "/curl/raw",
        params=q,
        headers=h,
        content=_normalize_binary_content(content),
        timeout=_normalize_timeout(eff_timeout),
    ) as resp:
        yield resp


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
    q: dict[str, object] = {**sanitize_curl_raw_params(params), "url": url}
    q["jwt"] = route.jwt
    opts = FinalRequestOptions.construct(
        method=method.upper(),
        url=route.base_url.rstrip("/") + "/curl/raw",
        params=q,
        headers=headers or {},
        content=_normalize_binary_content(content),
        json_data=json,
        timeout=timeout,
    )
    return cast(httpx.Response, await parent.request(httpx.Response, opts))


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
    q: dict[str, Any] = sanitize_curl_raw_params(params)
    q["jwt"] = route.jwt
    q["url"] = url
    h = {k: v for k, v in parent.default_headers.items() if isinstance(v, str)}
    if content is None:
        h.pop("Content-Type", None)
    if headers:
        h.update(headers)
    h.pop("Authorization", None)
    eff_timeout = parent.timeout if isinstance(timeout, NotGiven) else timeout
    async with parent._client.stream(
        method.upper(),
        route.base_url.rstrip("/") + "/curl/raw",
        params=q,
        headers=h,
        content=_normalize_binary_content(content),
        timeout=_normalize_timeout(eff_timeout),
    ) as resp:
        yield resp


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
