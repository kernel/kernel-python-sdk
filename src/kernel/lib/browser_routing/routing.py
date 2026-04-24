from __future__ import annotations

import os
import re
from typing import Any, Mapping, cast
from dataclasses import field, dataclass
from urllib.parse import unquote

import httpx

from .util import (
    jwt_from_cdp_ws_url,
    base_url_from_browser_like,
    cdp_ws_url_from_browser_like,
    session_id_from_browser_like,
)
from ..._compat import model_copy
from ..._models import FinalRequestOptions
from ..._constants import RAW_RESPONSE_HEADER


@dataclass
class BrowserRoute:
    session_id: str
    base_url: str
    jwt: str


@dataclass
class BrowserRoutingConfig:
    subresources: tuple[str, ...] = field(default_factory=tuple)


_BROWSER_ROUTE_CACHEABLE_PATH = re.compile(r"^/(?:v\d+/)?browsers(?:/[^/]+)?/?$")
_BROWSER_DELETE_BY_ID_PATH = re.compile(r"^/(?:v\d+/)?browsers/([^/]+)/?$")


def browser_routing_config_from_env() -> BrowserRoutingConfig:
    raw = os.environ.get("KERNEL_BROWSER_ROUTING_SUBRESOURCES")
    if raw is None:
        return BrowserRoutingConfig(subresources=("curl",))
    if raw.strip() == "":
        return BrowserRoutingConfig()

    return BrowserRoutingConfig(subresources=tuple(part.strip() for part in raw.split(",") if part.strip()))


class BrowserRouteCache:
    def __init__(self) -> None:
        self._routes: dict[str, BrowserRoute] = {}

    def get(self, session_id: str) -> BrowserRoute | None:
        return self._routes.get(_normalize_session_id(session_id))

    def set(self, route: BrowserRoute) -> None:
        normalized_session_id = _normalize_session_id(route.session_id)
        self._routes[normalized_session_id] = BrowserRoute(
            session_id=normalized_session_id,
            base_url=route.base_url.strip().rstrip("/") + "/",
            jwt=route.jwt.strip(),
        )

    def delete(self, session_id: str) -> None:
        self._routes.pop(_normalize_session_id(session_id), None)

    def values(self) -> list[BrowserRoute]:
        return list(self._routes.values())


def browser_route_from_browser(browser: Any) -> BrowserRoute | None:
    try:
        session_id = session_id_from_browser_like(browser)
    except TypeError:
        return None

    base_url = base_url_from_browser_like(browser)
    if not base_url:
        return None

    jwt = None
    try:
        jwt = jwt_from_cdp_ws_url(cdp_ws_url_from_browser_like(browser))
    except Exception:
        jwt = None
    if not jwt:
        return None

    return BrowserRoute(session_id=session_id, base_url=base_url, jwt=jwt)


def _normalize_session_id(session_id: str) -> str:
    return session_id.strip()


def maybe_populate_browser_route_cache_from_response(response: httpx.Response, *, cache: BrowserRouteCache) -> None:
    if not _should_populate_browser_route_cache(response):
        return

    try:
        populate_browser_route_cache_from_value(response.json(), cache=cache)
    except Exception:
        # Ignore malformed JSON in routing cache population.
        return


def maybe_evict_deleted_browser_route_from_response(response: httpx.Response, *, cache: BrowserRouteCache) -> None:
    if not response.is_success or response.request.method.upper() != "DELETE":
        return

    match = _BROWSER_DELETE_BY_ID_PATH.match(response.request.url.path)
    if match is None:
        return

    session_id = unquote(match.group(1)).strip()
    if not session_id:
        return

    cache.delete(session_id)


def populate_browser_route_cache_from_value(value: object, *, cache: BrowserRouteCache) -> None:
    if isinstance(value, Mapping):
        mapping = cast(Mapping[object, object], value)
        route = browser_route_from_browser(mapping)
        if route is not None:
            cache.set(route)

        for child in mapping.values():
            populate_browser_route_cache_from_value(child, cache=cache)
        return

    if isinstance(value, list):
        for item in cast(list[object], value):
            populate_browser_route_cache_from_value(item, cache=cache)


def _should_populate_browser_route_cache(response: httpx.Response) -> bool:
    if response.request.headers.get(RAW_RESPONSE_HEADER) == "stream":
        return False

    content_type = response.headers.get("content-type", "").lower()
    if "application/json" not in content_type:
        return False

    return bool(_BROWSER_ROUTE_CACHEABLE_PATH.match(response.request.url.path))


def rewrite_direct_vm_options(
    options: FinalRequestOptions,
    *,
    cache: BrowserRouteCache,
    config: BrowserRoutingConfig,
) -> FinalRequestOptions:
    match = match_direct_vm_path(options.url)
    if match is None:
        return options

    session_id, subresource, suffix = match
    if subresource not in set(config.subresources):
        return options

    route = cache.get(session_id)
    if route is None:
        return options

    rewritten = model_copy(options)
    rewritten.url = f"{route.base_url.rstrip('/')}/{subresource}{suffix}"

    params: dict[str, object] = {}
    params.update(options.params)
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
