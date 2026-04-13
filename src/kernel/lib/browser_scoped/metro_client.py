"""Internal HTTP clients that speak to metro-api /browser/kernel paths."""

from __future__ import annotations

from typing import Any, cast

from ..._client import Kernel, AsyncKernel
from ..._compat import model_copy
from ..._models import FinalRequestOptions


class _BrowserMetroKernel(Kernel):
    """Kernel client clone whose requests hit metro base_url with /browsers/{id} stripped."""

    _scoped_session_id: str

    def __init__(self, *, browser_session_id: str, **kwargs: Any) -> None:
        self._scoped_session_id = browser_session_id
        super().__init__(**kwargs)

    def _prepare_options(self, options: FinalRequestOptions) -> FinalRequestOptions:
        options = super()._prepare_options(options)
        url = options.url
        if not isinstance(url, str):
            return options
        prefix = f"/browsers/{self._scoped_session_id}/"
        if not url.startswith(prefix):
            return options
        suffix = url[len(prefix) :].lstrip("/")
        new_url = f"/{suffix}" if suffix else "/"
        out = model_copy(options)
        out.url = new_url
        return cast(FinalRequestOptions, out)


class _BrowserMetroAsyncKernel(AsyncKernel):
    _scoped_session_id: str

    def __init__(self, *, browser_session_id: str, **kwargs: Any) -> None:
        self._scoped_session_id = browser_session_id
        super().__init__(**kwargs)

    async def _prepare_options(self, options: FinalRequestOptions) -> FinalRequestOptions:
        options = await super()._prepare_options(options)
        url = options.url
        if not isinstance(url, str):
            return options
        prefix = f"/browsers/{self._scoped_session_id}/"
        if not url.startswith(prefix):
            return options
        suffix = url[len(prefix) :].lstrip("/")
        new_url = f"/{suffix}" if suffix else "/"
        out = model_copy(options)
        out.url = new_url
        return cast(FinalRequestOptions, out)


def metro_kernel_from_browser(parent: Kernel, *, session_id: str, metro_base_url: str, jwt: str) -> _BrowserMetroKernel:
    """Build a sync metro-scoped client sharing the parent's httpx transport."""
    base_q = getattr(parent, "_custom_query", None) or {}
    dq = {str(k): v for k, v in dict(base_q).items()}
    dq["jwt"] = jwt
    return _BrowserMetroKernel(
        browser_session_id=session_id,
        api_key=parent.api_key,
        base_url=metro_base_url,
        timeout=parent.timeout,
        max_retries=parent.max_retries,
        http_client=parent._client,
        default_headers=dict(parent._custom_headers),
        default_query=dq,
        _strict_response_validation=getattr(parent, "_strict_response_validation", False),
    )


def metro_async_kernel_from_browser(
    parent: AsyncKernel, *, session_id: str, metro_base_url: str, jwt: str
) -> _BrowserMetroAsyncKernel:
    base_q = getattr(parent, "_custom_query", None) or {}
    dq = {str(k): v for k, v in dict(base_q).items()}
    dq["jwt"] = jwt
    return _BrowserMetroAsyncKernel(
        browser_session_id=session_id,
        api_key=parent.api_key,
        base_url=metro_base_url,
        timeout=parent.timeout,
        max_retries=parent.max_retries,
        http_client=parent._client,
        default_headers=dict(parent._custom_headers),
        default_query=dq,
        _strict_response_validation=getattr(parent, "_strict_response_validation", False),
    )
