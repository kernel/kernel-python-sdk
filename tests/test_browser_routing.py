from __future__ import annotations

import os
from typing import Any, cast

import httpx
import respx
import pytest

from kernel import Kernel, AsyncKernel
from kernel.lib.browser_routing.util import jwt_from_cdp_ws_url
from kernel.lib.browser_routing.routing import (
    BrowserRoute,
    BrowserRouteCache,
    browser_route_from_browser,
    browser_routing_config_from_env,
)

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
def test_routes_allowlisted_browser_subresources_directly_to_vm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "process")
    route = respx.post("http://browser-session.test/browser/kernel/process/exec").mock(
        return_value=httpx.Response(200, json={"exit_code": 0, "stdout_b64": "", "stderr_b64": ""})
    )
    with Kernel(
        base_url=base_url,
        api_key=api_key,
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
def test_skips_direct_vm_routing_outside_allowlist(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "computer")
    route = respx.post(f"{base_url}/browsers/sess-1/process/exec").mock(
        return_value=httpx.Response(200, json={"exit_code": 0, "stdout_b64": "", "stderr_b64": ""})
    )
    with Kernel(
        base_url=base_url,
        api_key=api_key,
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


@respx.mock
def test_browser_create_warms_route_cache() -> None:
    create_route = respx.post(f"{base_url}/browsers").mock(return_value=httpx.Response(200, json=_fake_browser()))
    routed_request = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        browser = client.browsers.create()
        routed = client.browsers.request(browser.session_id, "GET", "https://example.com")

    assert create_route.called
    assert browser.session_id == "sess-1"
    assert routed.status_code == 200
    assert routed_request.called


@respx.mock
def test_raw_browser_create_warms_route_cache() -> None:
    create_route = respx.post(f"{base_url}/browsers").mock(return_value=httpx.Response(200, json=_fake_browser()))
    routed_request = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        response = client.browsers.with_raw_response.create()
        routed = client.browsers.request("sess-1", "GET", "https://example.com")

    assert create_route.called
    assert response.is_closed is True
    assert routed.status_code == 200
    assert routed.content == b"ok"
    request = cast(httpx.Request, cast(Any, routed_request.calls[0]).request)
    assert request.url.params.get("jwt") == "token-abc"


@pytest.mark.asyncio
@respx.mock
async def test_async_raw_browser_create_warms_route_cache() -> None:
    create_route = respx.post(f"{base_url}/browsers").mock(return_value=httpx.Response(200, json=_fake_browser()))
    routed_request = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    async with AsyncKernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        response = await client.browsers.with_raw_response.create()
        routed = await client.browsers.request("sess-1", "GET", "https://example.com")

    assert create_route.called
    assert response.is_closed is True
    assert routed.status_code == 200
    assert routed.content == b"ok"
    request = cast(httpx.Request, cast(Any, routed_request.calls[0]).request)
    assert request.url.params.get("jwt") == "token-abc"


@respx.mock
def test_only_browser_metadata_endpoints_warm_route_cache() -> None:
    projects_route = respx.get(f"{base_url}/projects").mock(return_value=httpx.Response(200, json=_fake_browser()))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        response = client.projects.with_raw_response.list()
        with pytest.raises(ValueError, match="route cache"):
            client.browsers.request("sess-1", "GET", "https://example.com")

    assert projects_route.called
    assert response.is_closed is True


def test_browser_route_cache_normalizes_session_id_keys() -> None:
    cache = BrowserRouteCache()
    cache.set(
        BrowserRoute(
            session_id="  sess-1  ",
            base_url=" http://browser-session.test/browser/kernel/ ",
            jwt=" token-abc ",
        )
    )

    route = cache.get("sess-1")
    assert route is not None
    assert route.session_id == "sess-1"
    assert route.base_url == "http://browser-session.test/browser/kernel/"
    assert route.jwt == "token-abc"

    cache.delete("sess-1")
    assert cache.get("sess-1") is None


def test_browser_route_from_browser_requires_base_url_and_jwt() -> None:
    assert browser_route_from_browser({**_fake_browser(), "base_url": None}) is None
    assert browser_route_from_browser({**_fake_browser(), "cdp_ws_url": None}) is None


def test_browser_routing_config_from_env_defaults_to_curl(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    assert browser_routing_config_from_env().subresources == ("curl",)


def test_browser_routing_config_from_env_empty_string_disables_routing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "")
    assert browser_routing_config_from_env().subresources == ()
