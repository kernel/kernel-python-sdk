from __future__ import annotations

from typing import Any, Mapping
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
        m = browser.get("session_id")
        if isinstance(m, str) and m:
            return m
    raise TypeError("browser object must have a non-empty session_id")


def base_url_from_browser_like(browser: Any) -> str | None:
    bu = getattr(browser, "base_url", None)
    if isinstance(bu, str) and bu.strip():
        return bu.strip().rstrip("/") + "/"
    if isinstance(browser, Mapping):
        raw = browser.get("base_url")
        if isinstance(raw, str) and raw.strip():
            return raw.strip().rstrip("/") + "/"
    return None


def cdp_ws_url_from_browser_like(browser: Any) -> str:
    u = getattr(browser, "cdp_ws_url", None)
    if isinstance(u, str) and u:
        return u
    if isinstance(browser, Mapping):
        m = browser.get("cdp_ws_url")
        if isinstance(m, str) and m:
            return m
    raise TypeError("browser object must have a non-empty cdp_ws_url")
