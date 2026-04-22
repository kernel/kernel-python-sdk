from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
import respx

from kernel import Kernel
from kernel.lib.browser_scoped.routing import BrowserRoutingConfig, browser_route_from_browser
from kernel.lib.browser_scoped.util import jwt_from_cdp_ws_url

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "sk-123"


def _fake_browser() -> dict[str, object]:
    return {
        "session_id": "sess-1",
        "base_url": "http://browser-session.test/browser/kernel",
        "cdp_ws_url": "wss://browser-session.test/browser/cdp?jwt=token-abc",
        "webdriver_ws_url": "wss://x",
        "created_at": "2020-01-01T00:00:00Z",
        "headless": True,
        "stealth": False,
        "timeout_seconds": 60,
    }


def _cache_browser(client: Kernel) -> None:
    route = browser_route_from_browser(_fake_browser())
    assert route is not None
    client.browser_route_cache.set(route)


def test_jwt_from_cdp_ws_url() -> None:
    assert jwt_from_cdp_ws_url("wss://h/browser/cdp?jwt=abc%2Fdef&x=1") == "abc/def"


@respx.mock
def test_routes_allowlisted_browser_subresources_directly_to_vm() -> None:
    route = respx.post("http://browser-session.test/browser/kernel/process/exec").mock(
        return_value=httpx.Response(200, json={"exit_code": 0, "stdout_b64": "", "stderr_b64": ""})
    )
    with Kernel(
        base_url=base_url,
        api_key=api_key,
        browser_routing=BrowserRoutingConfig(enabled=True, direct_to_vm_subresources=("process",)),
        _strict_response_validation=True,
    ) as client:
        _cache_browser(client)
        out = client.browsers.process.exec("sess-1", command="echo", args=["hi"])

    assert route.called
    request = cast(httpx.Request, cast(Any, route.calls[0]).request)
    assert request.url.params.get("jwt") == "token-abc"
    assert request.headers.get("Authorization") is None
    assert out.exit_code == 0


@respx.mock
def test_skips_direct_vm_routing_outside_allowlist() -> None:
    route = respx.post(f"{base_url}/browsers/sess-1/process/exec").mock(
        return_value=httpx.Response(200, json={"exit_code": 0, "stdout_b64": "", "stderr_b64": ""})
    )
    with Kernel(
        base_url=base_url,
        api_key=api_key,
        browser_routing=BrowserRoutingConfig(enabled=True, direct_to_vm_subresources=("computer",)),
        _strict_response_validation=True,
    ) as client:
        _cache_browser(client)
        client.browsers.process.exec("sess-1", command="echo", args=["hi"])

    assert route.called


@respx.mock
def test_browser_request_uses_curl_raw() -> None:
    route = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        response = client.browsers.request("sess-1", "GET", "https://example.com", params={"timeout_ms": 5000})

    assert response.status_code == 200
    assert response.content == b"ok"
    request = cast(httpx.Request, cast(Any, route.calls[0]).request)
    assert "curl/raw" in str(request.url)
    assert request.url.params.get("jwt") == "token-abc"


@respx.mock
def test_browser_request_params_cannot_override_target_url_or_jwt() -> None:
    route = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.request(
            "sess-1",
            "GET",
            "https://example.com",
            params={"url": "https://evil.example", "jwt": "other", "timeout_ms": 1},
        )

    request = cast(httpx.Request, cast(Any, route.calls[0]).request)
    assert str(request.url.params.get("url")) == "https://example.com"
    assert str(request.url.params.get("jwt")) == "token-abc"
    assert str(request.url.params.get("timeout_ms")) == "1"


def test_browser_request_requires_cached_route() -> None:
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browser_route_cache.delete("sess-1")
        with pytest.raises(ValueError, match="route cache"):
            client.browsers.request("sess-1", "GET", "https://example.com")


def test_browser_route_from_browser_requires_base_url_and_jwt() -> None:
    assert browser_route_from_browser({**_fake_browser(), "base_url": None}) is None
    assert browser_route_from_browser({**_fake_browser(), "cdp_ws_url": None}) is None
