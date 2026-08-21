from __future__ import annotations

import os
import asyncio
from typing import Any, AsyncIterator, cast
from typing_extensions import override

import httpx
import respx
import pytest

from kernel import Kernel, AsyncKernel, InternalServerError
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
        "memory": "8GiB",
        "timeout_seconds": 60,
        "region": "us-east",
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
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry/stream")
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


@pytest.mark.asyncio
async def test_async_telemetry_stream_cancellation_reaches_transport(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "telemetry/stream")
    read_started = asyncio.Event()
    transport_cancelled = asyncio.Event()
    chunks: asyncio.Queue[bytes] = asyncio.Queue()

    class BlockingSSEStream(httpx.AsyncByteStream):
        @override
        async def __aiter__(self) -> AsyncIterator[bytes]:
            read_started.set()
            try:
                while True:
                    yield await chunks.get()
            except asyncio.CancelledError:
                transport_cancelled.set()
                raise

        @override
        async def aclose(self) -> None:
            pass

    async def handle_request(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            headers={"content-type": "text/event-stream"},
            stream=BlockingSSEStream(),
        )

    http_client = httpx.AsyncClient(transport=httpx.MockTransport(handle_request))
    async with AsyncKernel(
        base_url=base_url,
        api_key=api_key,
        http_client=http_client,
        _strict_response_validation=True,
    ) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        stream = await client.browsers.telemetry.stream("sess-1")
        consumer = asyncio.create_task(stream.__anext__())
        await asyncio.wait_for(read_started.wait(), timeout=1)

        consumer.cancel()
        with pytest.raises(asyncio.CancelledError):
            await asyncio.wait_for(consumer, timeout=1)
        await asyncio.wait_for(transport_cancelled.wait(), timeout=1)


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


def test_browser_routing_config_from_env_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    assert browser_routing_config_from_env().subresources == (
        "curl",
        "telemetry/stream",
        "computer",
        "playwright",
    )


def test_direct_vm_routing_allowlist_segment_boundary() -> None:
    # Pins the fix: telemetry/stream (live SSE) routes to the VM; telemetry/events
    # (historical, served by the control plane from S2) does NOT; and a
    # stream-prefixed-but-different path is not matched.
    from kernel.lib.browser_routing.routing import _matches_direct_vm_prefix

    prefixes = ("curl", "telemetry/stream", "computer", "playwright")
    assert _matches_direct_vm_prefix("telemetry/stream", prefixes) is True
    assert _matches_direct_vm_prefix("telemetry/stream/x", prefixes) is True
    assert _matches_direct_vm_prefix("telemetry/events", prefixes) is False
    assert _matches_direct_vm_prefix("telemetry/streaming-config", prefixes) is False
    assert _matches_direct_vm_prefix("telemetry", prefixes) is False
    assert _matches_direct_vm_prefix("curl/raw", prefixes) is True
    assert _matches_direct_vm_prefix("computer/screenshot", prefixes) is True
    assert _matches_direct_vm_prefix("playwright/execute", prefixes) is True
    assert _matches_direct_vm_prefix("process/exec", prefixes) is False
    assert _matches_direct_vm_prefix("fs/read", prefixes) is False


def test_rewrite_direct_vm_options_keeps_telemetry_events_on_control_plane() -> None:
    # Integration through the real routing hook: telemetry/events (historical,
    # control-plane/S2) must NOT be rewritten to the VM, while telemetry/stream
    # (live SSE) must be.
    from kernel._models import FinalRequestOptions
    from kernel.lib.browser_routing.routing import (
        BrowserRoute,
        BrowserRouteCache,
        BrowserRoutingConfig,
        rewrite_direct_vm_options,
    )

    cache = BrowserRouteCache()
    cache.set(BrowserRoute(session_id="sess-1", base_url="http://browser-session.test/browser/kernel", jwt="token-abc"))
    config = BrowserRoutingConfig(subresources=("curl", "telemetry/stream", "computer", "playwright"))

    events = rewrite_direct_vm_options(
        FinalRequestOptions(method="get", url="/browsers/sess-1/telemetry/events"), cache=cache, config=config
    )
    assert events.url == "/browsers/sess-1/telemetry/events"  # unchanged -> control plane

    stream = rewrite_direct_vm_options(
        FinalRequestOptions(method="get", url="/browsers/sess-1/telemetry/stream"), cache=cache, config=config
    )
    assert str(stream.url).startswith("http://browser-session.test/browser/kernel/telemetry/stream")

    screenshot = rewrite_direct_vm_options(
        FinalRequestOptions(method="post", url="/browsers/sess-1/computer/screenshot"), cache=cache, config=config
    )
    assert str(screenshot.url).startswith("http://browser-session.test/browser/kernel/computer/screenshot")

    execute = rewrite_direct_vm_options(
        FinalRequestOptions(method="post", url="/browsers/sess-1/playwright/execute"), cache=cache, config=config
    )
    assert str(execute.url).startswith("http://browser-session.test/browser/kernel/playwright/execute")

    process = rewrite_direct_vm_options(
        FinalRequestOptions(method="post", url="/browsers/sess-1/process/exec"), cache=cache, config=config
    )
    assert process.url == "/browsers/sess-1/process/exec"

    fs_read = rewrite_direct_vm_options(
        FinalRequestOptions(method="get", url="/browsers/sess-1/fs/read_file"), cache=cache, config=config
    )
    assert fs_read.url == "/browsers/sess-1/fs/read_file"


def test_browser_routing_config_from_env_empty_string_disables_routing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "")
    assert browser_routing_config_from_env().subresources == ()


@respx.mock
def test_computer_screenshot_and_playwright_execute_route_to_vm_by_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    screenshot = respx.post("http://browser-session.test/browser/kernel/computer/screenshot").mock(
        return_value=httpx.Response(200, content=b"png", headers={"content-type": "image/png"})
    )
    execute = respx.post("http://browser-session.test/browser/kernel/playwright/execute").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.computer.capture_screenshot("sess-1")
        out = client.browsers.playwright.execute("sess-1", code="return 1")

    assert screenshot.called
    screenshot_req = cast(httpx.Request, cast(Any, screenshot.calls[0]).request)
    assert screenshot_req.url.params.get("jwt") == "token-abc"
    assert screenshot_req.headers.get("Authorization") is None
    assert execute.called
    execute_req = cast(httpx.Request, cast(Any, execute.calls[0]).request)
    assert execute_req.url.params.get("jwt") == "token-abc"
    assert execute_req.headers.get("Authorization") is None
    assert out.success is True


@respx.mock
def test_process_fs_and_telemetry_events_stay_on_api_origin_by_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    process = respx.post(f"{base_url}/browsers/sess-1/process/exec").mock(
        return_value=httpx.Response(200, json={"exit_code": 0, "stdout_b64": "", "stderr_b64": ""})
    )
    fs_read = respx.get(f"{base_url}/browsers/sess-1/fs/read_file").mock(
        return_value=httpx.Response(200, content=b"x", headers={"content-type": "application/octet-stream"})
    )
    events = respx.get(f"{base_url}/browsers/sess-1/telemetry/events").mock(return_value=httpx.Response(200, json=[]))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.process.exec("sess-1", command="echo")
        client.browsers.fs.read_file("sess-1", path="/tmp/x")
        client.browsers.telemetry.events("sess-1")

    assert process.called
    assert fs_read.called
    assert events.called


@respx.mock
def test_stale_direct_vm_jwt_evicts_cache_and_retries_control_plane(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)

    def _skip_retry_sleep(_self: object, **_kwargs: object) -> None:
        return None

    monkeypatch.setattr("kernel._base_client.SyncAPIClient._sleep_for_retry", _skip_retry_sleep)
    vm = respx.post("http://browser-session.test/browser/kernel/computer/screenshot").mock(
        return_value=httpx.Response(401, text="Invalid JWT")
    )
    api = respx.post(f"{base_url}/browsers/sess-1/computer/screenshot").mock(
        return_value=httpx.Response(200, content=b"png", headers={"content-type": "image/png"})
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.computer.capture_screenshot("sess-1")
        assert client.browser_route_cache.get("sess-1") is None

    assert vm.called
    assert api.called
    api_req = cast(httpx.Request, cast(Any, api.calls[0]).request)
    assert api_req.headers.get("Authorization") == f"Bearer {api_key}"


def test_stale_direct_vm_jwt_does_not_evict_refreshed_route() -> None:
    from kernel.lib.browser_routing.routing import maybe_evict_browser_route_from_response

    cache = BrowserRouteCache()
    cache.set(
        BrowserRoute(
            session_id="sess-1",
            base_url="http://browser-session.test/browser/kernel",
            jwt="token-abc",
        )
    )
    cache.set(
        BrowserRoute(
            session_id="sess-1",
            base_url="http://browser-session.test/browser/kernel",
            jwt="jwt-FRESH",
        )
    )
    request = httpx.Request(
        "POST",
        "http://browser-session.test/browser/kernel/computer/screenshot?jwt=token-abc",
    )
    maybe_evict_browser_route_from_response(
        httpx.Response(401, text="Invalid JWT", request=request),
        cache=cache,
    )
    route = cache.get("sess-1")
    assert route is not None
    assert route.jwt == "jwt-FRESH"


def test_stale_direct_vm_auth_retry_does_not_require_cached_route() -> None:
    from kernel.lib.browser_routing.routing import should_retry_stale_direct_vm_auth

    request = httpx.Request(
        "POST",
        "http://browser-session.test/browser/kernel/computer/screenshot?jwt=token-abc",
    )
    response = httpx.Response(401, text="Invalid JWT", request=request)
    empty = BrowserRouteCache()
    assert should_retry_stale_direct_vm_auth(response) is True
    assert empty.get("sess-1") is None
