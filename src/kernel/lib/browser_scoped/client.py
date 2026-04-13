"""Browser-scoped view over a session: VM subresources and raw HTTP via internal /curl/raw."""

from __future__ import annotations

import inspect
from typing import IO, TYPE_CHECKING, Any, Mapping, cast
from contextlib import contextmanager, asynccontextmanager
from collections.abc import Iterable, Iterator, AsyncIterator

import httpx

from .util import (
    jwt_from_cdp_ws_url,
    sanitize_curl_raw_params,
    base_url_from_browser_like,
    cdp_ws_url_from_browser_like,
    session_id_from_browser_like,
)
from ..._types import Body, Timeout, NotGiven, BinaryTypes, not_given
from ..._models import FinalRequestOptions
from .browser_session_kernel import build_browser_session_kernel, build_async_browser_session_kernel

if TYPE_CHECKING:
    from ..._client import Kernel, AsyncKernel
    from ...resources.browsers.logs import LogsResource, AsyncLogsResource
    from ...resources.browsers.fs.fs import FsResource, AsyncFsResource
    from ...resources.browsers.process import ProcessResource, AsyncProcessResource
    from ...resources.browsers.replays import ReplaysResource, AsyncReplaysResource
    from ...resources.browsers.computer import ComputerResource, AsyncComputerResource
    from ...resources.browsers.playwright import PlaywrightResource, AsyncPlaywrightResource


class _BoundBrowserSubresource:
    """Delegates to a generated resource while defaulting `id` to the scoped session."""

    def __init__(self, inner: Any, session_id: str) -> None:
        object.__setattr__(self, "_inner", inner)
        object.__setattr__(self, "_session_id", session_id)

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        attr = getattr(self._inner, name)
        if name.startswith("with_") or not callable(attr):
            return attr
        try:
            sig = inspect.signature(attr)
        except (TypeError, ValueError):
            return attr
        if "id" not in sig.parameters:
            return attr

        def bound(*args: Any, **kwargs: Any) -> Any:
            kw = dict(kwargs)
            kw["id"] = self._session_id
            return attr(*args, **kw)

        return bound


class BrowserScopedClient:
    """Session-scoped API: subresources without repeating session id; HTTP via browser /curl/raw."""

    def __init__(self, parent: Kernel, *, session_id: str, session_base_url: str, jwt: str) -> None:
        self._parent = parent
        self.session_id = session_id
        self._session_base_url = session_base_url
        self._jwt = jwt
        self._http = build_browser_session_kernel(
            parent, session_id=session_id, session_base_url=session_base_url, jwt=jwt
        )

    @property
    def parent(self) -> Kernel:
        """Control-plane client this view was created from (for future id remapping hooks)."""
        return self._parent

    @property
    def base_url(self) -> str:
        return self._session_base_url

    @property
    def process(self) -> ProcessResource:
        from ...resources.browsers.process import ProcessResource

        return cast(ProcessResource, _BoundBrowserSubresource(ProcessResource(self._http), self.session_id))

    @property
    def computer(self) -> ComputerResource:
        from ...resources.browsers.computer import ComputerResource

        return cast(ComputerResource, _BoundBrowserSubresource(ComputerResource(self._http), self.session_id))

    @property
    def fs(self) -> FsResource:
        from ...resources.browsers.fs.fs import FsResource

        return cast(FsResource, _BoundBrowserSubresource(FsResource(self._http), self.session_id))

    @property
    def logs(self) -> LogsResource:
        from ...resources.browsers.logs import LogsResource

        return cast(LogsResource, _BoundBrowserSubresource(LogsResource(self._http), self.session_id))

    @property
    def playwright(self) -> PlaywrightResource:
        from ...resources.browsers.playwright import PlaywrightResource

        return cast(PlaywrightResource, _BoundBrowserSubresource(PlaywrightResource(self._http), self.session_id))

    @property
    def replays(self) -> ReplaysResource:
        from ...resources.browsers.replays import ReplaysResource

        return cast(ReplaysResource, _BoundBrowserSubresource(ReplaysResource(self._http), self.session_id))

    def request(
        self,
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
        opts = FinalRequestOptions.construct(
            method=method.upper(),
            url="/curl/raw",
            params=q,
            headers=_normalize_headers(headers),
            content=_normalize_binary_content(content),
            json_data=json,
            timeout=_normalize_timeout(timeout),
        )
        return self._http.request(httpx.Response, opts)

    @contextmanager
    def stream(
        self,
        method: str,
        url: str,
        *,
        content: BinaryTypes | None = None,
        headers: Mapping[str, str] | None = None,
        params: Mapping[str, object] | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> Iterator[httpx.Response]:
        q: dict[str, Any] = dict(self._http.default_query)
        q.update(sanitize_curl_raw_params(params))
        q["url"] = url
        h = {k: v for k, v in self._http.default_headers.items() if isinstance(v, str)}
        if content is None:
            h.pop("Content-Type", None)
        if headers:
            h.update(headers)
        eff_timeout = self._http.timeout if isinstance(timeout, NotGiven) else timeout
        cm = self._http._client.stream(
            method.upper(),
            self._http._prepare_url("/curl/raw"),
            params=q,
            headers=h,
            content=_normalize_binary_content(content),
            timeout=_normalize_timeout(eff_timeout),
        )
        with cm as resp:
            yield resp


class AsyncBrowserScopedClient:
    def __init__(self, parent: AsyncKernel, *, session_id: str, session_base_url: str, jwt: str) -> None:
        self._parent = parent
        self.session_id = session_id
        self._session_base_url = session_base_url
        self._jwt = jwt
        self._http = build_async_browser_session_kernel(
            parent, session_id=session_id, session_base_url=session_base_url, jwt=jwt
        )

    @property
    def parent(self) -> AsyncKernel:
        return self._parent

    @property
    def base_url(self) -> str:
        return self._session_base_url

    @property
    def process(self) -> AsyncProcessResource:
        from ...resources.browsers.process import AsyncProcessResource

        return cast(AsyncProcessResource, _BoundBrowserSubresource(AsyncProcessResource(self._http), self.session_id))

    @property
    def computer(self) -> AsyncComputerResource:
        from ...resources.browsers.computer import AsyncComputerResource

        return cast(
            AsyncComputerResource, _BoundBrowserSubresource(AsyncComputerResource(self._http), self.session_id)
        )

    @property
    def fs(self) -> AsyncFsResource:
        from ...resources.browsers.fs.fs import AsyncFsResource

        return cast(AsyncFsResource, _BoundBrowserSubresource(AsyncFsResource(self._http), self.session_id))

    @property
    def logs(self) -> AsyncLogsResource:
        from ...resources.browsers.logs import AsyncLogsResource

        return cast(AsyncLogsResource, _BoundBrowserSubresource(AsyncLogsResource(self._http), self.session_id))

    @property
    def playwright(self) -> AsyncPlaywrightResource:
        from ...resources.browsers.playwright import AsyncPlaywrightResource

        return cast(
            AsyncPlaywrightResource, _BoundBrowserSubresource(AsyncPlaywrightResource(self._http), self.session_id)
        )

    @property
    def replays(self) -> AsyncReplaysResource:
        from ...resources.browsers.replays import AsyncReplaysResource

        return cast(AsyncReplaysResource, _BoundBrowserSubresource(AsyncReplaysResource(self._http), self.session_id))

    async def request(
        self,
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
        opts = FinalRequestOptions.construct(
            method=method.upper(),
            url="/curl/raw",
            params=q,
            headers=_normalize_headers(headers),
            content=_normalize_binary_content(content),
            json_data=json,
            timeout=_normalize_timeout(timeout),
        )
        return await self._http.request(httpx.Response, opts)

    @asynccontextmanager
    async def stream(
        self,
        method: str,
        url: str,
        *,
        content: BinaryTypes | None = None,
        headers: Mapping[str, str] | None = None,
        params: Mapping[str, object] | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
    ) -> AsyncIterator[httpx.Response]:
        q: dict[str, Any] = dict(self._http.default_query)
        q.update(sanitize_curl_raw_params(params))
        q["url"] = url
        h = {k: v for k, v in self._http.default_headers.items() if isinstance(v, str)}
        if content is None:
            h.pop("Content-Type", None)
        if headers:
            h.update(headers)
        eff_timeout = self._http.timeout if isinstance(timeout, NotGiven) else timeout
        async with self._http._client.stream(
            method.upper(),
            self._http._prepare_url("/curl/raw"),
            params=q,
            headers=h,
            content=_normalize_binary_content(content),
            timeout=_normalize_timeout(eff_timeout),
        ) as resp:
            yield resp


def browser_scoped_from_browser(parent: Kernel, browser: Any) -> BrowserScopedClient:
    session_id = session_id_from_browser_like(browser)
    session_base = base_url_from_browser_like(browser)
    if not session_base:
        raise ValueError("browser.base_url is required for a browser-scoped client")
    jwt = jwt_from_cdp_ws_url(cdp_ws_url_from_browser_like(browser))
    if not jwt:
        raise ValueError("could not parse jwt from browser.cdp_ws_url; required for browser session HTTP")
    return BrowserScopedClient(parent, session_id=session_id, session_base_url=session_base, jwt=jwt)


def async_browser_scoped_from_browser(parent: AsyncKernel, browser: Any) -> AsyncBrowserScopedClient:
    session_id = session_id_from_browser_like(browser)
    session_base = base_url_from_browser_like(browser)
    if not session_base:
        raise ValueError("browser.base_url is required for a browser-scoped client")
    jwt = jwt_from_cdp_ws_url(cdp_ws_url_from_browser_like(browser))
    if not jwt:
        raise ValueError("could not parse jwt from browser.cdp_ws_url; required for browser session HTTP")
    return AsyncBrowserScopedClient(parent, session_id=session_id, session_base_url=session_base, jwt=jwt)


def _normalize_headers(headers: Mapping[str, str] | None) -> Mapping[str, str]:
    return headers if headers is not None else {}


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
