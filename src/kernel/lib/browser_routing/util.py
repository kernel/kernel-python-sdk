from __future__ import annotations

from typing import Any, Mapping, cast
from urllib.parse import parse_qs, urlparse

# Query keys reserved for /curl/raw; user-supplied `params` must not override these.
CURL_RAW_RESERVED_QUERY_KEYS: frozenset[str] = frozenset({"url", "jwt"})


def sanitize_curl_raw_params(params: Mapping[str, object] | None) -> dict[str, object]:
    """Drop reserved keys from user params so they cannot override the target URL or auth."""
    if not params:
        return {}
    return {k: v for k, v in dict(params).items() if k not in CURL_RAW_RESERVED_QUERY_KEYS}


def jwt_from_cdp_ws_url(cdp_ws_url: str) -> str | None:
    parsed = urlparse(cdp_ws_url)
    values = parse_qs(parsed.query).get("jwt")
    if not values:
        return None
    return values[0]


def session_id_from_browser_like(browser: Any) -> str:
    sid = getattr(browser, "session_id", None)
    if isinstance(sid, str) and sid:
        return sid
    if isinstance(browser, Mapping):
        mapping = cast(Mapping[str, object], browser)
        value = mapping.get("session_id")
        if isinstance(value, str) and value:
            return value
    raise TypeError("browser object must have a non-empty session_id")


def base_url_from_browser_like(browser: Any) -> str | None:
    base_url = getattr(browser, "base_url", None)
    if isinstance(base_url, str) and base_url.strip():
        return base_url.strip().rstrip("/") + "/"
    if isinstance(browser, Mapping):
        mapping = cast(Mapping[str, object], browser)
        value = mapping.get("base_url")
        if isinstance(value, str) and value.strip():
            return value.strip().rstrip("/") + "/"
    return None


def cdp_ws_url_from_browser_like(browser: Any) -> str:
    cdp_ws_url = getattr(browser, "cdp_ws_url", None)
    if isinstance(cdp_ws_url, str) and cdp_ws_url:
        return cdp_ws_url
    if isinstance(browser, Mapping):
        mapping = cast(Mapping[str, object], browser)
        value = mapping.get("cdp_ws_url")
        if isinstance(value, str) and value:
            return value
    raise TypeError("browser object must have a non-empty cdp_ws_url")
