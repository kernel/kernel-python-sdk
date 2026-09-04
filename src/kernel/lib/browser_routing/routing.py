from __future__ import annotations

import os
import re
import json
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


_EVICTION_HOOK_CACHE_ATTR = "_kernel_browser_route_cache"


_BROWSER_ROUTE_CACHEABLE_PATH = re.compile(r"^/(?:v\d+/)?browsers(?:/[^/]+)?/?$")
_BROWSER_DELETE_BY_ID_PATH = re.compile(r"^/(?:v\d+/)?browsers/([^/]+)/?$")
_BROWSER_POOL_ACQUIRE_PATH = re.compile(r"^/(?:v\d+/)?browser_pools/[^/]+/acquire/?$")
_BROWSER_POOL_RELEASE_PATH = re.compile(r"^/(?:v\d+/)?browser_pools/[^/]+/release/?$")


def browser_routing_config_from_env() -> BrowserRoutingConfig:
    raw = os.environ.get("KERNEL_BROWSER_ROUTING_SUBRESOURCES")
    if raw is None:
        # Path prefixes eligible for direct-to-VM routing. "telemetry/stream" is
        # the live SSE endpoint (VM); "telemetry/events" is a historical read
        # served by the control plane (S2) and must NOT be here.
        return BrowserRoutingConfig(
            subresources=(
                "curl",
                "telemetry/stream",
                "computer",
                "playwright",
                "process",
                "fs",
                "logs/stream",
            )
        )
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

    def delete_if_jwt(self, session_id: str, jwt: str) -> bool:
        key = _normalize_session_id(session_id)
        route = self._routes.get(key)
        if route is None or route.jwt != jwt.strip():
            return False
        del self._routes[key]
        return True

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


def maybe_evict_browser_route_from_response(response: httpx.Response, *, cache: BrowserRouteCache) -> None:
    if response.is_success:
        session_id = _session_id_to_evict_from_response(response)
        if session_id:
            cache.delete(session_id)
        return

    if not is_stale_direct_vm_auth_response(response):
        return

    jwt = str(response.request.url.params.get("jwt") or "").strip()
    session_id = _session_id_from_direct_vm_response(response, cache=cache)
    if session_id and jwt:
        cache.delete_if_jwt(session_id, jwt)


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

    path = response.request.url.path
    return bool(_BROWSER_ROUTE_CACHEABLE_PATH.match(path) or _BROWSER_POOL_ACQUIRE_PATH.match(path))


def _session_id_to_evict_from_response(response: httpx.Response) -> str | None:
    method = response.request.method.upper()
    path = response.request.url.path

    if method == "DELETE":
        return _session_id_from_browser_delete_path(path)

    if method == "POST":
        return _session_id_from_browser_pool_release_request(response.request, path)

    return None


def _session_id_from_direct_vm_response(response: httpx.Response, *, cache: BrowserRouteCache) -> str | None:
    raw = str(response.request.url)
    for route in cache.values():
        if raw.startswith(route.base_url.rstrip("/") + "/"):
            return route.session_id
    return None


def is_stale_direct_vm_auth_response(response: httpx.Response) -> bool:
    if response.status_code not in {401, 403}:
        return False
    return bool(response.request.url.params.get("jwt"))


def install_stale_direct_vm_auth_eviction(client: httpx.Client, *, cache: BrowserRouteCache) -> None:
    """Evict stale direct-to-VM routes as soon as the response status is known.

    httpx reads the body of a non-streamed response inside `send()`, so a caller
    that only inspects the returned response never learns the status of a 401/403
    whose body read fails — the read error surfaces from `send()` instead and the
    dead route would stay cached, wedging every later call for that session. A
    response event hook runs after the status is known and before any body is
    read, which keeps eviction independent of the body. For a caller-supplied
    `http_client`, the hook is installed into that client's `event_hooks` and
    prepended so an existing hook cannot pre-empt eviction by reading a failing
    body or raising.
    """
    hooks = client.event_hooks.setdefault("response", [])
    if _has_eviction_hook(hooks, cache):
        return

    def evict(response: httpx.Response) -> None:
        if is_stale_direct_vm_auth_response(response):
            maybe_evict_browser_route_from_response(response, cache=cache)

    setattr(evict, _EVICTION_HOOK_CACHE_ATTR, cache)
    hooks.insert(0, evict)


def install_async_stale_direct_vm_auth_eviction(client: httpx.AsyncClient, *, cache: BrowserRouteCache) -> None:
    """Async counterpart of `install_stale_direct_vm_auth_eviction`."""
    hooks = client.event_hooks.setdefault("response", [])
    if _has_eviction_hook(hooks, cache):
        return

    async def evict(response: httpx.Response) -> None:
        if is_stale_direct_vm_auth_response(response):
            maybe_evict_browser_route_from_response(response, cache=cache)

    setattr(evict, _EVICTION_HOOK_CACHE_ATTR, cache)
    hooks.insert(0, evict)


def _has_eviction_hook(hooks: list[Any], cache: BrowserRouteCache) -> bool:
    # A copied client shares both the httpx client and the route cache, so the
    # hook is registered once per cache instead of once per client.
    return any(getattr(hook, _EVICTION_HOOK_CACHE_ATTR, None) is cache for hook in hooks)


def should_retry_stale_direct_vm_auth(response: httpx.Response) -> bool:
    """Whether a stale direct-to-VM auth failure can be retried on the control plane.

    A retry rebuilds the request from the original options, so it is only safe when
    the body can be serialized again byte for byte. Streamed bodies (e.g. a file
    object passed to fs.write_file) are consumed by the direct request, so retrying
    would send a truncated or empty body to the control plane.
    """
    if not is_stale_direct_vm_auth_response(response):
        return False
    return direct_vm_request_body_is_replayable(response.request)


def direct_vm_request_body_is_replayable(request: httpx.Request) -> bool:
    try:
        _ = request.content
    except httpx.RequestNotRead:
        pass
    else:
        # httpx already buffered the body, so rebuilding it yields the same bytes.
        return True

    # httpx encodes multipart bodies as a stream of fields it re-renders per attempt.
    fields = getattr(request.stream, "fields", None)
    if fields is None:
        # A streamed body (file object, iterator or async iterator) cannot be replayed.
        return False
    return all(_multipart_field_is_replayable(field) for field in cast("list[Any]", fields))


def _multipart_field_is_replayable(field: Any) -> bool:
    file = getattr(field, "file", None)
    if file is None:
        # A data field renders from an in-memory value.
        return True
    if isinstance(file, (bytes, str)):
        return True
    if getattr(file, "closed", False):
        return False
    return _rewind_succeeds(file)


def _rewind_succeeds(file: Any) -> bool:
    """Whether the file field can actually be rewound for another render.

    `seekable()` is not proof: a wrapper can report True and still raise from
    `seek()`, which would render the field as an empty part on the retry. The
    only reliable check is to perform the rewind httpx would perform.
    """
    seek = getattr(file, "seek", None)
    if not callable(seek):
        return False

    position: object = None
    tell = getattr(file, "tell", None)
    if callable(tell):
        try:
            position = tell()
        except Exception:
            position = None

    try:
        seek(0)
    except Exception:
        return False

    if isinstance(position, int) and position > 0:
        try:
            seek(position)
        except Exception:
            # The field is left rewound, which is where httpx renders it from anyway.
            pass
    return True


def _session_id_from_browser_delete_path(path: str) -> str | None:
    match = _BROWSER_DELETE_BY_ID_PATH.match(path)
    if match is None:
        return None

    session_id = unquote(match.group(1)).strip()
    return session_id or None


def _session_id_from_browser_pool_release_request(request: httpx.Request, path: str) -> str | None:
    if _BROWSER_POOL_RELEASE_PATH.match(path) is None:
        return None

    content_type = request.headers.get("content-type", "").lower()
    if "application/json" not in content_type:
        return None

    try:
        body = json.loads(request.content.decode("utf-8"))
    except Exception:
        return None

    session_id = body.get("session_id")
    if not isinstance(session_id, str):
        return None

    normalized = session_id.strip()
    return normalized or None


def _matches_direct_vm_prefix(tail: str, prefixes: tuple[str, ...]) -> bool:
    """Whether tail (the path after browsers/{id}/) is covered by an allow prefix,
    matching on segment boundaries: "telemetry/stream" matches "telemetry/stream"
    and "telemetry/stream/...", but not "telemetry/events" or "telemetry/streamfoo".
    Keeps historical control-plane reads (e.g. telemetry/events, served from S2)
    off the VM.
    """
    tail = tail.strip("/")
    for prefix in prefixes:
        prefix = prefix.strip("/")
        if prefix and (tail == prefix or tail.startswith(prefix + "/")):
            return True
    return False


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
    if not _matches_direct_vm_prefix(f"{subresource}{suffix}", config.subresources):
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
