from __future__ import annotations

import os
from typing import Any, cast

import httpx
import respx
import pytest

from kernel import (
    Kernel,
    AsyncKernel,
    NotFoundError,
    APIConnectionError,
    InternalServerError,
)
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
def test_telemetry_stream_routes_directly_to_vm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    route = respx.get("http://browser-session.test/browser/kernel/telemetry/stream").mock(
        return_value=httpx.Response(
            200,
            headers={"content-type": "text/event-stream"},
            content=b'id: 1\ndata: {"category":"api"}\n\n',
        )
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        stream = client.browsers.telemetry.stream("sess-1")
        stream.close()

    assert route.called
    request = cast(httpx.Request, cast(Any, route.calls[0]).request)
    assert request.url.path == "/browser/kernel/telemetry/stream"
    assert request.url.params.get("jwt") == "token-abc"
    assert request.headers.get("Authorization") is None


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
    projects_route = respx.get(f"{base_url}/org/projects").mock(return_value=httpx.Response(200, json=_fake_browser()))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        response = client.projects.with_raw_response.list()
        with pytest.raises(ValueError, match="route cache"):
            client.browsers.request("sess-1", "GET", "https://example.com")

    assert projects_route.called
    assert response.is_closed is True


@respx.mock
def test_browser_pool_acquire_warms_route_cache() -> None:
    acquire_route = respx.post(f"{base_url}/browser_pools/pool-1/acquire").mock(
        return_value=httpx.Response(200, json=_fake_browser())
    )
    routed_request = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        response = client.browser_pools.with_raw_response.acquire("pool-1")
        routed = client.browsers.request("sess-1", "GET", "https://example.com")

    assert acquire_route.called
    assert response.is_closed is True
    assert routed.status_code == 200
    assert routed_request.called


@respx.mock
def test_browser_delete_by_id_evicts_route_cache() -> None:
    delete_route = respx.delete(f"{base_url}/browsers/sess-1").mock(return_value=httpx.Response(204))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        response = client.browsers.with_raw_response.delete_by_id("sess-1")
        with pytest.raises(ValueError, match="route cache"):
            client.browsers.request("sess-1", "GET", "https://example.com")

    assert delete_route.called
    assert response.is_closed is True


@respx.mock
def test_browser_pool_release_evicts_route_cache() -> None:
    release_route = respx.post(f"{base_url}/browser_pools/pool-1/release").mock(return_value=httpx.Response(204))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        response = client.browser_pools.with_raw_response.release("pool-1", session_id="sess-1")
        with pytest.raises(ValueError, match="route cache"):
            client.browsers.request("sess-1", "GET", "https://example.com")

    assert release_route.called
    assert response.is_closed is True


@respx.mock
def test_failed_browser_delete_by_id_keeps_route_cache() -> None:
    delete_route = respx.delete(f"{base_url}/browsers/sess-1").mock(
        return_value=httpx.Response(500, json={"error": "boom"})
    )
    routed_request = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(InternalServerError):
            client.browsers.delete_by_id("sess-1")
        routed = client.browsers.request("sess-1", "GET", "https://example.com")

    assert delete_route.called
    assert routed.status_code == 200
    assert routed_request.called


@respx.mock
def test_failed_browser_pool_release_keeps_route_cache() -> None:
    release_route = respx.post(f"{base_url}/browser_pools/pool-1/release").mock(
        return_value=httpx.Response(500, json={"error": "boom"})
    )
    routed_request = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(InternalServerError):
            client.browser_pools.release("pool-1", session_id="sess-1")
        routed = client.browsers.request("sess-1", "GET", "https://example.com")

    assert release_route.called
    assert routed.status_code == 200
    assert routed_request.called


@pytest.mark.asyncio
@respx.mock
async def test_async_browser_pool_release_evicts_route_cache() -> None:
    release_route = respx.post(f"{base_url}/browser_pools/pool-1/release").mock(return_value=httpx.Response(204))
    async with AsyncKernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        response = await client.browser_pools.with_raw_response.release("pool-1", session_id="sess-1")
        with pytest.raises(ValueError, match="route cache"):
            await client.browsers.request("sess-1", "GET", "https://example.com")

    assert release_route.called
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
    assert browser_routing_config_from_env().subresources == ("curl", "telemetry")


def test_browser_routing_config_from_env_empty_string_disables_routing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "")
    assert browser_routing_config_from_env().subresources == ()


# ---------------------------------------------------------------------------
# Control-plane fallback (browser_gone 404) — see kernel#2317.
#
# The prospective eligible endpoint is GET /browsers/{id}/telemetry/events.
# That SDK method does not exist yet, so these tests exercise the routed GET
# via the low-level `client.get(...)` against that exact path. `telemetry`
# routing is enabled locally/explicitly per test (the default-subresources
# constant is intentionally NOT modified by this PR).
# ---------------------------------------------------------------------------

_EVENTS_PATH = "/browsers/sess-1/telemetry/events"
_VM_EVENTS_URL = "http://browser-session.test/browser/kernel/telemetry/events"
_GONE_BODY = {"code": "browser_gone", "message": "browser not found"}


def test_telemetry_events_is_fallback_eligible() -> None:
    from kernel.lib.browser_routing.routing import is_fallback_eligible_routed_path

    assert is_fallback_eligible_routed_path("telemetry", "/events") is True
    assert is_fallback_eligible_routed_path("telemetry", "/stream") is False
    assert is_fallback_eligible_routed_path("process", "/exec") is False


@respx.mock
def test_eligible_get_browser_gone_falls_back_to_control_plane(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get(_VM_EVENTS_URL).mock(return_value=httpx.Response(404, json=_GONE_BODY))
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(200, json={"events": []}))

    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        response = client.get(_EVENTS_PATH, cast_to=httpx.Response)

    # VM hit exactly once, control plane hit exactly once (no loop).
    assert vm_route.call_count == 1
    assert cp_route.call_count == 1
    assert response.status_code == 200
    assert response.json() == {"events": []}

    # Control-plane re-issue restores Authorization and drops the jwt param.
    cp_request = cast(httpx.Request, cast(Any, cp_route.calls[0]).request)
    assert cp_request.headers.get("Authorization") == f"Bearer {api_key}"
    assert cp_request.url.params.get("jwt") is None

    # The dead route is evicted authoritatively.
    assert client.browser_route_cache.get("sess-1") is None


@respx.mock
def test_eligible_get_browser_gone_then_cp_errors_returns_as_is_no_loop(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get(_VM_EVENTS_URL).mock(return_value=httpx.Response(404, json=_GONE_BODY))
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(500, json={"error": "boom"}))

    with Kernel(base_url=base_url, api_key=api_key, max_retries=0, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(InternalServerError):
            client.get(_EVENTS_PATH, cast_to=httpx.Response)

    # VM once, control plane once — the CP error is surfaced, never retried/looped.
    assert vm_route.call_count == 1
    assert cp_route.call_count == 1


@respx.mock
def test_non_eligible_path_browser_gone_does_not_fall_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get("http://browser-session.test/browser/kernel/telemetry/stream").mock(
        return_value=httpx.Response(404, json=_GONE_BODY)
    )
    cp_route = respx.get(f"{base_url}/browsers/sess-1/telemetry/stream").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )

    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(NotFoundError):
            client.get("/browsers/sess-1/telemetry/stream", cast_to=httpx.Response)

    # The VM 404 propagates unchanged; no control-plane fallback; route kept.
    assert vm_route.call_count == 1
    assert cp_route.call_count == 0
    assert client.browser_route_cache.get("sess-1") is not None


@respx.mock
def test_eligible_get_transient_5xx_does_not_fall_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get(_VM_EVENTS_URL).mock(return_value=httpx.Response(502, json={"error": "bad gateway"}))
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(200, json={"events": []}))

    with Kernel(base_url=base_url, api_key=api_key, max_retries=0, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(InternalServerError):
            client.get(_EVENTS_PATH, cast_to=httpx.Response)

    # Transient 5xx is just returned; we do NOT retry the dead VM then fall back.
    assert vm_route.call_count == 1
    assert cp_route.call_count == 0
    assert client.browser_route_cache.get("sess-1") is not None


@respx.mock
def test_eligible_get_connection_error_does_not_fall_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get(_VM_EVENTS_URL).mock(side_effect=httpx.ConnectError("nope"))
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(200, json={"events": []}))

    with Kernel(base_url=base_url, api_key=api_key, max_retries=0, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(APIConnectionError):
            client.get(_EVENTS_PATH, cast_to=httpx.Response)

    assert vm_route.call_count == 1
    assert cp_route.call_count == 0


@respx.mock
def test_eligible_get_success_does_not_fall_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get(_VM_EVENTS_URL).mock(return_value=httpx.Response(200, json={"events": [1, 2]}))
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(200, json={"events": []}))

    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        response = client.get(_EVENTS_PATH, cast_to=httpx.Response)

    assert vm_route.call_count == 1
    assert cp_route.call_count == 0
    assert response.json() == {"events": [1, 2]}
    assert client.browser_route_cache.get("sess-1") is not None


@respx.mock
def test_eligible_but_post_does_not_fall_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.post(_VM_EVENTS_URL).mock(return_value=httpx.Response(404, json=_GONE_BODY))
    cp_route = respx.post(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(200, json={"events": []}))

    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(NotFoundError):
            client.post(_EVENTS_PATH, cast_to=httpx.Response, body={})

    # POST is not GET: browser_gone 404 propagates, no fallback.
    assert vm_route.call_count == 1
    assert cp_route.call_count == 0


@respx.mock
def test_eligible_get_plain_404_without_browser_gone_does_not_fall_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get(_VM_EVENTS_URL).mock(
        return_value=httpx.Response(404, json={"code": "not_found", "message": "nope"})
    )
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(200, json={"events": []}))

    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(NotFoundError):
            client.get(_EVENTS_PATH, cast_to=httpx.Response)

    # A live VM's own 404 (no browser_gone code) propagates unchanged.
    assert vm_route.call_count == 1
    assert cp_route.call_count == 0
    assert client.browser_route_cache.get("sess-1") is not None


@respx.mock
def test_non_routed_request_untouched_on_browser_gone(monkeypatch: pytest.MonkeyPatch) -> None:
    # No cached route -> request is never routed to a VM. Even a verbatim
    # browser_gone 404 from the control plane must NOT trigger any fallback loop.
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(404, json=_GONE_BODY))

    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        with pytest.raises(NotFoundError):
            client.get(_EVENTS_PATH, cast_to=httpx.Response)

    assert cp_route.call_count == 1


@pytest.mark.asyncio
@respx.mock
async def test_async_eligible_get_browser_gone_falls_back_to_control_plane(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get(_VM_EVENTS_URL).mock(return_value=httpx.Response(404, json=_GONE_BODY))
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(200, json={"events": []}))

    async with AsyncKernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        response = await client.get(_EVENTS_PATH, cast_to=httpx.Response)

    assert vm_route.call_count == 1
    assert cp_route.call_count == 1
    assert response.json() == {"events": []}
    cp_request = cast(httpx.Request, cast(Any, cp_route.calls[0]).request)
    assert cp_request.headers.get("Authorization") == f"Bearer {api_key}"
    assert cp_request.url.params.get("jwt") is None
    assert client.browser_route_cache.get("sess-1") is None


@pytest.mark.asyncio
@respx.mock
async def test_async_eligible_get_transient_5xx_does_not_fall_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry")
    vm_route = respx.get(_VM_EVENTS_URL).mock(return_value=httpx.Response(503, json={"error": "unavailable"}))
    cp_route = respx.get(f"{base_url}{_EVENTS_PATH}").mock(return_value=httpx.Response(200, json={"events": []}))

    async with AsyncKernel(
        base_url=base_url, api_key=api_key, max_retries=0, _strict_response_validation=True
    ) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        with pytest.raises(InternalServerError):
            await client.get(_EVENTS_PATH, cast_to=httpx.Response)

    assert vm_route.call_count == 1
    assert cp_route.call_count == 0
    assert client.browser_route_cache.get("sess-1") is not None
