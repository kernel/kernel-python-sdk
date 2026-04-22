from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, cast

import httpx

from ..._compat import model_copy
from ..._models import FinalRequestOptions
from ..._types import Headers
from .util import base_url_from_browser_like, jwt_from_cdp_ws_url, cdp_ws_url_from_browser_like, session_id_from_browser_like


@dataclass
class BrowserRoute:
    session_id: str
    base_url: str
    jwt: str | None = None


@dataclass
class BrowserRoutingConfig:
    enabled: bool = False
    direct_to_vm_subresources: tuple[str, ...] = field(default_factory=tuple)


class BrowserRouteCache:
    def __init__(self) -> None:
        self._routes: dict[str, BrowserRoute] = {}

    def get(self, session_id: str) -> BrowserRoute | None:
        return self._routes.get(session_id)

    def set(self, route: BrowserRoute) -> None:
        self._routes[route.session_id] = BrowserRoute(
            session_id=route.session_id.strip(),
            base_url=route.base_url.strip().rstrip("/") + "/",
            jwt=route.jwt.strip() if isinstance(route.jwt, str) and route.jwt.strip() else None,
        )

    def delete(self, session_id: str) -> None:
        self._routes.pop(session_id, None)

    def prime(self, browser: Any) -> BrowserRoute:
        session_id = session_id_from_browser_like(browser)
        base_url = base_url_from_browser_like(browser)
        if not base_url:
            raise ValueError("browser.base_url is required to prime the browser route cache")
        jwt = None
        try:
            jwt = jwt_from_cdp_ws_url(cdp_ws_url_from_browser_like(browser))
        except Exception:
            jwt = None
        route = BrowserRoute(session_id=session_id, base_url=base_url, jwt=jwt)
        self.set(route)
        return route

    def values(self) -> list[BrowserRoute]:
        return list(self._routes.values())


def rewrite_direct_vm_options(
    options: FinalRequestOptions,
    *,
    cache: BrowserRouteCache,
    config: BrowserRoutingConfig | None,
) -> FinalRequestOptions:
    if config is None or not config.enabled:
        return options

    match = match_direct_vm_path(options.url)
    if match is None:
        return options

    session_id, subresource, suffix = match
    if subresource not in set(config.direct_to_vm_subresources):
        return options

    route = cache.get(session_id)
    if route is None:
        return options

    rewritten = model_copy(options)
    rewritten.url = f"{route.base_url.rstrip('/')}/{subresource}{suffix}"

    params: dict[str, object] = {}
    if isinstance(options.params, Mapping):
        params.update(cast(Mapping[str, object], options.params))
    if route.jwt:
        params["jwt"] = route.jwt
    rewritten.params = params or options.params
    return rewritten


def strip_direct_vm_auth(request: httpx.Request, *, cache: BrowserRouteCache) -> None:
    raw = str(request.url)
    for route in cache.values():
        if raw.startswith(route.base_url.rstrip("/") + "/"):
            request.headers.pop("Authorization", None)
            return


def match_direct_vm_path(path: str) -> tuple[str, str, str] | None:
    if "://" in path:
        return None

    parts = [part for part in path.strip("/").split("/") if part]
    for index in range(len(parts) - 2):
        if parts[index] != "browsers":
            continue
        session_id = parts[index + 1]
        subresource = parts[index + 2]
        if not session_id or not subresource:
            return None
        suffix = ""
        if index + 3 < len(parts):
            suffix = "/" + "/".join(parts[index + 3 :])
        return session_id, subresource, suffix
    return None


def build_direct_vm_headers(headers: Mapping[str, str] | None) -> Headers | None:
    if headers is None:
        return {"Authorization": None}
    out: dict[str, str | None] = {"Authorization": None}
    out.update(headers)
    return out
