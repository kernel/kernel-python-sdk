"""Internal Kernel clones for browser session HTTP (base_url + /browser/kernel paths)."""

from __future__ import annotations

from typing import Any, Mapping, cast
from typing_extensions import override

from ..._client import Kernel, AsyncKernel
from ..._compat import model_copy
from ..._models import FinalRequestOptions


class _BrowserSessionKernel(Kernel):
    """Kernel clone whose HTTP base is the browser session; strips /browsers/{id} from paths."""

    _scoped_session_id: str

    def __init__(self, *, browser_session_id: str, **kwargs: Any) -> None:
        self._scoped_session_id = browser_session_id
        super().__init__(**kwargs)

    @override
    def _prepare_options(self, options: FinalRequestOptions) -> FinalRequestOptions:
        options = super()._prepare_options(options)
        url = options.url
        prefix = f"/browsers/{self._scoped_session_id}/"
        if not url.startswith(prefix):
            return options
        suffix = url[len(prefix) :].lstrip("/")
        new_url = f"/{suffix}" if suffix else "/"
        out = model_copy(options)
        out.url = new_url
        return out


class _BrowserSessionAsyncKernel(AsyncKernel):
    _scoped_session_id: str

    def __init__(self, *, browser_session_id: str, **kwargs: Any) -> None:
        self._scoped_session_id = browser_session_id
        super().__init__(**kwargs)

    @override
    async def _prepare_options(self, options: FinalRequestOptions) -> FinalRequestOptions:
        options = await super()._prepare_options(options)
        url = options.url
        prefix = f"/browsers/{self._scoped_session_id}/"
        if not url.startswith(prefix):
            return options
        suffix = url[len(prefix) :].lstrip("/")
        new_url = f"/{suffix}" if suffix else "/"
        out = model_copy(options)
        out.url = new_url
        return out


def build_browser_session_kernel(
    parent: Kernel, *, session_id: str, session_base_url: str, jwt: str
) -> _BrowserSessionKernel:
    """Build a sync client sharing the parent's httpx transport; requests use session_base_url."""
    base_q_raw = getattr(parent, "_custom_query", None)
    if isinstance(base_q_raw, Mapping):
        base_q = {str(k): v for k, v in cast(Mapping[str, object], base_q_raw).items()}
    else:
        base_q = {}
    dq = dict(base_q)
    dq["jwt"] = jwt
    return _BrowserSessionKernel(
        browser_session_id=session_id,
        api_key=parent.api_key,
        base_url=session_base_url,
        timeout=parent.timeout,
        max_retries=parent.max_retries,
        http_client=parent._client,
        default_headers=dict(parent._custom_headers),
        default_query=dq,
        _strict_response_validation=getattr(parent, "_strict_response_validation", False),
    )


def build_async_browser_session_kernel(
    parent: AsyncKernel, *, session_id: str, session_base_url: str, jwt: str
) -> _BrowserSessionAsyncKernel:
    base_q_raw = getattr(parent, "_custom_query", None)
    if isinstance(base_q_raw, Mapping):
        base_q = {str(k): v for k, v in cast(Mapping[str, object], base_q_raw).items()}
    else:
        base_q = {}
    dq = dict(base_q)
    dq["jwt"] = jwt
    return _BrowserSessionAsyncKernel(
        browser_session_id=session_id,
        api_key=parent.api_key,
        base_url=session_base_url,
        timeout=parent.timeout,
        max_retries=parent.max_retries,
        http_client=parent._client,
        default_headers=dict(parent._custom_headers),
        default_query=dq,
        _strict_response_validation=getattr(parent, "_strict_response_validation", False),
    )
