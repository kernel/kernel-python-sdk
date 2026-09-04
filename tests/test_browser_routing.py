from __future__ import annotations

import io
import os
import asyncio
from typing import Any, Iterator, AsyncIterator, cast
from pathlib import Path
from typing_extensions import override

import httpx
import respx
import pytest

from kernel import (
    Kernel,
    AsyncKernel,
    APIConnectionError,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
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
        "memory": "8GiB",
        "timeout_seconds": 60,
        "region": "us-east",
    }


def _skip_retry_sleep(_self: object, **_kwargs: object) -> None:
    return None


class _UnseekableFile(io.RawIOBase):
    """A file-like upload body that cannot be rewound, e.g. a pipe.

    `claims_seekable` reproduces a wrapper whose `seekable()` says True while
    `seek()` still raises, which would otherwise render as an empty part.
    """

    name = "one.txt"

    def __init__(self, content: bytes, *, claims_seekable: bool = False) -> None:
        self._content = content
        self._claims_seekable = claims_seekable

    @override
    def readable(self) -> bool:
        return True

    @override
    def read(self, size: int = -1) -> bytes:
        chunk = self._content if size < 0 else self._content[:size]
        self._content = b"" if size < 0 else self._content[size:]
        return chunk

    @override
    def tell(self) -> int:
        return 0

    @override
    def seekable(self) -> bool:
        return self._claims_seekable

    @override
    def seek(self, _offset: int, _whence: int = 0) -> int:
        raise io.UnsupportedOperation("not seekable")


class _NoSeekableAttrFile(io.RawIOBase):
    """A file-like upload body whose `seek()` raises and reports no seekability."""

    name = "one.txt"

    def __init__(self, content: bytes) -> None:
        self._content = content

    @override
    def readable(self) -> bool:
        return True

    @override
    def read(self, size: int = -1) -> bytes:
        chunk = self._content if size < 0 else self._content[:size]
        self._content = b"" if size < 0 else self._content[size:]
        return chunk

    @override
    def seek(self, _offset: int, _whence: int = 0) -> int:
        raise OSError("not seekable")


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
        "process",
        "fs",
        "logs/stream",
    )


def test_direct_vm_routing_allowlist_segment_boundary() -> None:
    # Pins the fix: telemetry/stream (live SSE) routes to the VM; telemetry/events
    # (historical, served by the control plane from S2) does NOT; and a
    # stream-prefixed-but-different path is not matched.
    from kernel.lib.browser_routing.routing import _matches_direct_vm_prefix

    prefixes = ("curl", "telemetry/stream", "computer", "playwright", "process", "fs", "logs/stream")
    assert _matches_direct_vm_prefix("telemetry/stream", prefixes) is True
    assert _matches_direct_vm_prefix("telemetry/stream/x", prefixes) is True
    assert _matches_direct_vm_prefix("telemetry/events", prefixes) is False
    assert _matches_direct_vm_prefix("telemetry/streaming-config", prefixes) is False
    assert _matches_direct_vm_prefix("telemetry", prefixes) is False
    assert _matches_direct_vm_prefix("curl/raw", prefixes) is True
    assert _matches_direct_vm_prefix("computer/screenshot", prefixes) is True
    assert _matches_direct_vm_prefix("playwright/execute", prefixes) is True
    assert _matches_direct_vm_prefix("process/exec", prefixes) is True
    assert _matches_direct_vm_prefix("process/proc-1/stdout/stream", prefixes) is True
    assert _matches_direct_vm_prefix("fs/read_file", prefixes) is True
    assert _matches_direct_vm_prefix("fs/watch/watch-1/events", prefixes) is True
    assert _matches_direct_vm_prefix("fsx/read_file", prefixes) is False
    assert _matches_direct_vm_prefix("logs/stream", prefixes) is True
    assert _matches_direct_vm_prefix("logs/stream/x", prefixes) is True
    assert _matches_direct_vm_prefix("logs", prefixes) is False
    assert _matches_direct_vm_prefix("logs/history", prefixes) is False
    assert _matches_direct_vm_prefix("logstream", prefixes) is False
    assert _matches_direct_vm_prefix("extensions", prefixes) is False
    assert _matches_direct_vm_prefix("replays/rec-1", prefixes) is False


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
    config = BrowserRoutingConfig(
        subresources=("curl", "telemetry/stream", "computer", "playwright", "process", "fs", "logs/stream")
    )

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
    assert str(process.url).startswith("http://browser-session.test/browser/kernel/process/exec")

    fs_read = rewrite_direct_vm_options(
        FinalRequestOptions(method="get", url="/browsers/sess-1/fs/read_file"), cache=cache, config=config
    )
    assert str(fs_read.url).startswith("http://browser-session.test/browser/kernel/fs/read_file")

    logs_stream = rewrite_direct_vm_options(
        FinalRequestOptions(method="get", url="/browsers/sess-1/logs/stream"), cache=cache, config=config
    )
    assert str(logs_stream.url).startswith("http://browser-session.test/browser/kernel/logs/stream")

    logs_root = rewrite_direct_vm_options(
        FinalRequestOptions(method="get", url="/browsers/sess-1/logs"), cache=cache, config=config
    )
    assert logs_root.url == "/browsers/sess-1/logs"

    logs_history = rewrite_direct_vm_options(
        FinalRequestOptions(method="get", url="/browsers/sess-1/logs/history"), cache=cache, config=config
    )
    assert logs_history.url == "/browsers/sess-1/logs/history"

    extensions = rewrite_direct_vm_options(
        FinalRequestOptions(method="post", url="/browsers/sess-1/extensions"), cache=cache, config=config
    )
    assert extensions.url == "/browsers/sess-1/extensions"

    replays = rewrite_direct_vm_options(
        FinalRequestOptions(method="get", url="/browsers/sess-1/replays"), cache=cache, config=config
    )
    assert replays.url == "/browsers/sess-1/replays"


def test_browser_routing_config_from_env_empty_string_disables_routing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "")
    assert browser_routing_config_from_env().subresources == ()


@respx.mock
def test_default_browser_subresources_route_to_vm(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    screenshot = respx.post("http://browser-session.test/browser/kernel/computer/screenshot").mock(
        return_value=httpx.Response(200, content=b"png", headers={"content-type": "image/png"})
    )
    execute = respx.post("http://browser-session.test/browser/kernel/playwright/execute").mock(
        return_value=httpx.Response(200, json={"success": True})
    )
    process = respx.post("http://browser-session.test/browser/kernel/process/exec").mock(
        return_value=httpx.Response(200, json={"exit_code": 0, "stdout_b64": "", "stderr_b64": ""})
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.computer.capture_screenshot("sess-1")
        out = client.browsers.playwright.execute("sess-1", code="return 1")
        process_out = client.browsers.process.exec("sess-1", command="echo")

    assert screenshot.called
    screenshot_req = cast(httpx.Request, cast(Any, screenshot.calls[0]).request)
    assert screenshot_req.url.params.get("jwt") == "token-abc"
    assert screenshot_req.headers.get("Authorization") is None
    assert execute.called
    execute_req = cast(httpx.Request, cast(Any, execute.calls[0]).request)
    assert execute_req.url.params.get("jwt") == "token-abc"
    assert execute_req.headers.get("Authorization") is None
    assert process.called
    process_req = cast(httpx.Request, cast(Any, process.calls[0]).request)
    assert process_req.url.params.get("jwt") == "token-abc"
    assert process_req.headers.get("Authorization") is None
    assert out.success is True
    assert process_out.exit_code == 0


@respx.mock
def test_control_plane_subresources_stay_on_api_origin_by_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    events = respx.get(f"{base_url}/browsers/sess-1/telemetry/events").mock(return_value=httpx.Response(200, json=[]))
    replays = respx.get(f"{base_url}/browsers/sess-1/replays").mock(return_value=httpx.Response(200, json=[]))
    extensions = respx.post(f"{base_url}/browsers/sess-1/extensions").mock(return_value=httpx.Response(204))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.telemetry.events("sess-1")
        client.browsers.replays.list("sess-1")
        client.browsers.load_extensions("sess-1", extensions=[{"name": "ext", "zip_file": b"zip"}])

    assert events.called
    assert replays.called
    assert extensions.called
    extensions_req = cast(httpx.Request, cast(Any, extensions.calls[0]).request)
    assert extensions_req.headers.get("Authorization") == f"Bearer {api_key}"


@respx.mock
def test_stale_direct_vm_jwt_evicts_cache_and_retries_control_plane(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
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


@respx.mock
def test_fs_json_endpoints_route_to_vm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    list_files = respx.get("http://browser-session.test/browser/kernel/fs/list_files").mock(
        return_value=httpx.Response(200, json=[])
    )
    move = respx.put("http://browser-session.test/browser/kernel/fs/move").mock(return_value=httpx.Response(204))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.fs.list_files("sess-1", path="/tmp")
        client.browsers.fs.move("sess-1", dest_path="/tmp/b", src_path="/tmp/a")

    list_req = cast(httpx.Request, cast(Any, list_files.calls[0]).request)
    assert list_req.url.params.get("path") == "/tmp"
    assert list_req.url.params.get("jwt") == "token-abc"
    assert list_req.headers.get("Authorization") is None

    move_req = cast(httpx.Request, cast(Any, move.calls[0]).request)
    assert move_req.url.path == "/browser/kernel/fs/move"
    assert move_req.url.params.get("jwt") == "token-abc"
    assert move_req.headers.get("Authorization") is None


@respx.mock
def test_fs_read_file_routes_binary_response_from_vm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    read_file = respx.get("http://browser-session.test/browser/kernel/fs/read_file").mock(
        return_value=httpx.Response(200, content=b"\x00binary", headers={"content-type": "application/octet-stream"})
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        response = client.browsers.fs.read_file("sess-1", path="/tmp/x")

    assert response.read() == b"\x00binary"
    request = cast(httpx.Request, cast(Any, read_file.calls[0]).request)
    assert request.url.params.get("path") == "/tmp/x"
    assert request.url.params.get("jwt") == "token-abc"
    assert request.headers.get("Authorization") is None


@respx.mock
def test_fs_write_file_routes_binary_body_to_vm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    write_file = respx.put("http://browser-session.test/browser/kernel/fs/write_file").mock(
        return_value=httpx.Response(201)
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.fs.write_file("sess-1", b"\x00payload", path="/tmp/x", mode="600")

    request = cast(httpx.Request, cast(Any, write_file.calls[0]).request)
    assert request.content == b"\x00payload"
    assert request.headers.get("content-type") == "application/octet-stream"
    assert request.url.params.get("path") == "/tmp/x"
    assert request.url.params.get("mode") == "600"
    assert request.url.params.get("jwt") == "token-abc"
    assert request.headers.get("Authorization") is None


@respx.mock
def test_fs_upload_routes_indexed_multipart_to_vm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    upload = respx.post("http://browser-session.test/browser/kernel/fs/upload").mock(return_value=httpx.Response(201))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.fs.upload(
            "sess-1",
            files=[
                {"dest_path": "/tmp/one", "file": b"one"},
                {"dest_path": "/tmp/two", "file": b"two"},
            ],
        )

    request = cast(httpx.Request, cast(Any, upload.calls[0]).request)
    assert request.url.params.get("jwt") == "token-abc"
    assert request.headers.get("Authorization") is None
    body = request.read()
    assert b'name="files[0][dest_path]"' in body
    assert b'name="files[0][file]"' in body
    assert b'name="files[1][dest_path]"' in body
    assert b'name="files[1][file]"' in body
    assert b"files[][" not in body


@respx.mock
def test_fs_watch_events_stream_routes_to_vm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    events = respx.get("http://browser-session.test/browser/kernel/fs/watch/watch-1/events").mock(
        return_value=httpx.Response(
            200,
            headers={"content-type": "text/event-stream"},
            content=b'data: {"type":"CREATE","path":"/tmp/x","is_dir":false,"name":"x"}\n\n',
        )
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        stream = client.browsers.fs.watch.events("watch-1", id_or_name="sess-1")
        first = next(iter(stream))
        stream.close()

    assert first.path == "/tmp/x"
    request = cast(httpx.Request, cast(Any, events.calls[0]).request)
    assert request.url.path == "/browser/kernel/fs/watch/watch-1/events"
    assert request.url.params.get("jwt") == "token-abc"
    assert request.headers.get("Authorization") is None


@respx.mock
def test_logs_stream_routes_to_vm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    logs = respx.get("http://browser-session.test/browser/kernel/logs/stream").mock(
        return_value=httpx.Response(
            200,
            headers={"content-type": "text/event-stream"},
            content=b'data: {"event":"log","message":"hello","timestamp":"2020-01-01T00:00:00Z"}\n\n',
        )
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        stream = client.browsers.logs.stream("sess-1", source="path", path="/var/log/x", follow=True)
        first = next(iter(stream))
        stream.close()

    assert first.message == "hello"
    request = cast(httpx.Request, cast(Any, logs.calls[0]).request)
    assert request.url.path == "/browser/kernel/logs/stream"
    assert request.url.params.get("source") == "path"
    assert request.url.params.get("path") == "/var/log/x"
    assert request.url.params.get("follow") == "true"
    assert request.url.params.get("jwt") == "token-abc"
    assert request.headers.get("Authorization") is None


@pytest.mark.asyncio
async def test_async_logs_stream_cancellation_reaches_transport(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    read_started = asyncio.Event()
    transport_cancelled = asyncio.Event()
    chunks: asyncio.Queue[bytes] = asyncio.Queue()
    requested: list[httpx.URL] = []

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

    async def handle_request(request: httpx.Request) -> httpx.Response:
        requested.append(request.url)
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
        stream = await client.browsers.logs.stream("sess-1", source="supervisor", supervisor_process="chromium")
        consumer = asyncio.create_task(stream.__anext__())
        await asyncio.wait_for(read_started.wait(), timeout=1)

        consumer.cancel()
        with pytest.raises(asyncio.CancelledError):
            await asyncio.wait_for(consumer, timeout=1)
        await asyncio.wait_for(transport_cancelled.wait(), timeout=1)

    assert requested
    assert requested[0].path == "/browser/kernel/logs/stream"


@respx.mock
def test_stale_direct_vm_jwt_replays_buffered_fs_body_on_control_plane(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    monkeypatch.setattr("kernel._base_client.SyncAPIClient._sleep_for_retry", _skip_retry_sleep)
    vm = respx.put("http://browser-session.test/browser/kernel/fs/write_file").mock(
        return_value=httpx.Response(401, text="Invalid JWT")
    )
    api = respx.put(f"{base_url}/browsers/sess-1/fs/write_file").mock(return_value=httpx.Response(201))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.fs.write_file("sess-1", b"payload", path="/tmp/x")
        assert client.browser_route_cache.get("sess-1") is None

    assert vm.called
    api_req = cast(httpx.Request, cast(Any, api.calls[0]).request)
    assert api_req.content == b"payload"
    assert api_req.url.params.get("path") == "/tmp/x"
    assert api_req.url.params.get("jwt") is None
    assert api_req.headers.get("Authorization") == f"Bearer {api_key}"


@respx.mock
def test_stale_direct_vm_jwt_does_not_replay_streamed_fs_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    monkeypatch.setattr("kernel._base_client.SyncAPIClient._sleep_for_retry", _skip_retry_sleep)
    vm = respx.put("http://browser-session.test/browser/kernel/fs/write_file").mock(
        return_value=httpx.Response(401, text="Invalid JWT")
    )
    api = respx.put(f"{base_url}/browsers/sess-1/fs/write_file").mock(return_value=httpx.Response(201))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(AuthenticationError):
            client.browsers.fs.write_file("sess-1", iter([b"chunk-one", b"chunk-two"]), path="/tmp/x")
        # The stale route is still evicted, so the caller's next attempt uses the control plane.
        assert client.browser_route_cache.get("sess-1") is None

    assert vm.call_count == 1
    assert not api.called


@pytest.mark.asyncio
@respx.mock
async def test_async_stale_direct_vm_jwt_does_not_replay_streamed_fs_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    monkeypatch.setattr("kernel._base_client.AsyncAPIClient._sleep_for_retry", _skip_retry_sleep)
    vm = respx.put("http://browser-session.test/browser/kernel/fs/write_file").mock(
        return_value=httpx.Response(401, text="Invalid JWT")
    )
    api = respx.put(f"{base_url}/browsers/sess-1/fs/write_file").mock(return_value=httpx.Response(201))

    async def _chunks() -> AsyncIterator[bytes]:
        yield b"chunk-one"
        yield b"chunk-two"

    async with AsyncKernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        with pytest.raises(AuthenticationError):
            await client.browsers.fs.write_file("sess-1", _chunks(), path="/tmp/x")
        assert client.browser_route_cache.get("sess-1") is None

    assert vm.call_count == 1
    assert not api.called


@respx.mock
def test_stale_direct_vm_jwt_replays_multipart_upload_on_control_plane(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    monkeypatch.setattr("kernel._base_client.SyncAPIClient._sleep_for_retry", _skip_retry_sleep)
    vm = respx.post("http://browser-session.test/browser/kernel/fs/upload").mock(
        return_value=httpx.Response(403, text="Invalid JWT")
    )
    api = respx.post(f"{base_url}/browsers/sess-1/fs/upload").mock(return_value=httpx.Response(201))
    upload = tmp_path / "one.txt"
    upload.write_bytes(b"file-bytes")

    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        with upload.open("rb") as handle:
            client.browsers.fs.upload("sess-1", files=[{"dest_path": "/tmp/one", "file": handle}])

    assert vm.called
    api_req = cast(httpx.Request, cast(Any, api.calls[0]).request)
    body = api_req.read()
    assert b"file-bytes" in body
    assert b'name="files[0][dest_path]"' in body
    assert api_req.headers.get("Authorization") == f"Bearer {api_key}"


def test_direct_vm_request_body_is_replayable_classification(tmp_path: Path) -> None:
    from kernel.lib.browser_routing.routing import direct_vm_request_body_is_replayable

    assert direct_vm_request_body_is_replayable(httpx.Request("GET", "http://vm.test/fs/read_file")) is True
    assert direct_vm_request_body_is_replayable(httpx.Request("PUT", "http://vm.test/fs/write_file", content=b"x"))
    assert (
        direct_vm_request_body_is_replayable(httpx.Request("PUT", "http://vm.test/fs/write_file", content=iter([b"x"])))
        is False
    )

    path = tmp_path / "one.txt"
    path.write_bytes(b"file-bytes")
    with path.open("rb") as handle:
        seekable = httpx.Request(
            "POST",
            "http://vm.test/fs/upload",
            data={"files[0][dest_path]": "/tmp/one"},
            files=[("files[0][file]", handle)],
        )
        assert direct_vm_request_body_is_replayable(seekable) is True

        unseekable = httpx.Request(
            "POST",
            "http://vm.test/fs/upload",
            files=[("files[0][file]", cast(Any, _UnseekableFile(b"file-bytes")))],
        )
        assert direct_vm_request_body_is_replayable(unseekable) is False

        # seekable() is not proof: the rewind itself has to succeed.
        lies_about_seekable = httpx.Request(
            "POST",
            "http://vm.test/fs/upload",
            files=[("files[0][file]", cast(Any, _UnseekableFile(b"file-bytes", claims_seekable=True)))],
        )
        assert direct_vm_request_body_is_replayable(lies_about_seekable) is False

        without_seekable_attr = httpx.Request(
            "POST",
            "http://vm.test/fs/upload",
            files=[("files[0][file]", cast(Any, _NoSeekableAttrFile(b"file-bytes")))],
        )
        assert direct_vm_request_body_is_replayable(without_seekable_attr) is False

        in_memory = io.BytesIO(b"file-bytes")
        buffered = httpx.Request("POST", "http://vm.test/fs/upload", files=[("files[0][file]", in_memory)])
        assert direct_vm_request_body_is_replayable(buffered) is True

        in_memory.close()
        assert direct_vm_request_body_is_replayable(buffered) is False


@respx.mock
def test_env_override_can_exclude_fs_and_logs(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "computer")
    fs_read = respx.get(f"{base_url}/browsers/sess-1/fs/read_file").mock(
        return_value=httpx.Response(200, content=b"x", headers={"content-type": "application/octet-stream"})
    )
    logs = respx.get(f"{base_url}/browsers/sess-1/logs/stream").mock(
        return_value=httpx.Response(
            200,
            headers={"content-type": "text/event-stream"},
            content=b'data: {"event":"log","message":"hello","timestamp":"2020-01-01T00:00:00Z"}\n\n',
        )
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.fs.read_file("sess-1", path="/tmp/x")
        client.browsers.logs.stream("sess-1", source="path", path="/var/log/x").close()

    assert fs_read.called
    assert logs.called


@respx.mock
def test_empty_env_disables_fs_and_logs_routing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", "")
    fs_read = respx.get(f"{base_url}/browsers/sess-1/fs/read_file").mock(
        return_value=httpx.Response(200, content=b"x", headers={"content-type": "application/octet-stream"})
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        response = client.browsers.fs.read_file("sess-1", path="/tmp/x")

    assert fs_read.called
    request = cast(httpx.Request, cast(Any, fs_read.calls[0]).request)
    assert request.url.params.get("jwt") is None
    assert request.headers.get("Authorization") == f"Bearer {api_key}"
    assert response.read() == b"x"


@respx.mock
def test_stale_direct_vm_jwt_does_not_replay_multipart_that_cannot_rewind(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    monkeypatch.setattr("kernel._base_client.SyncAPIClient._sleep_for_retry", _skip_retry_sleep)
    vm = respx.post("http://browser-session.test/browser/kernel/fs/upload").mock(
        return_value=httpx.Response(401, text="Invalid JWT")
    )
    api = respx.post(f"{base_url}/browsers/sess-1/fs/upload").mock(return_value=httpx.Response(201))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(AuthenticationError):
            client.browsers.fs.upload(
                "sess-1",
                files=[
                    {
                        "dest_path": "/tmp/one",
                        "file": cast(Any, _UnseekableFile(b"file-bytes", claims_seekable=True)),
                    }
                ],
            )
        assert client.browser_route_cache.get("sess-1") is None

    assert vm.call_count == 1
    assert not api.called


@pytest.mark.asyncio
@respx.mock
async def test_async_stale_direct_vm_jwt_does_not_replay_multipart_that_cannot_rewind(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    monkeypatch.setattr("kernel._base_client.AsyncAPIClient._sleep_for_retry", _skip_retry_sleep)
    vm = respx.post("http://browser-session.test/browser/kernel/fs/upload").mock(
        return_value=httpx.Response(403, text="Invalid JWT")
    )
    api = respx.post(f"{base_url}/browsers/sess-1/fs/upload").mock(return_value=httpx.Response(201))
    async with AsyncKernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        with pytest.raises(PermissionDeniedError):
            await client.browsers.fs.upload(
                "sess-1",
                files=[
                    {
                        "dest_path": "/tmp/one",
                        "file": cast(Any, _UnseekableFile(b"file-bytes", claims_seekable=True)),
                    }
                ],
            )
        assert client.browser_route_cache.get("sess-1") is None

    assert vm.call_count == 1
    assert not api.called


@respx.mock
def test_stale_direct_vm_jwt_evicts_route_without_retries_for_buffered_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    vm = respx.put("http://browser-session.test/browser/kernel/fs/write_file").mock(
        return_value=httpx.Response(401, text="Invalid JWT")
    )
    api = respx.put(f"{base_url}/browsers/sess-1/fs/write_file").mock(return_value=httpx.Response(201))
    with Kernel(base_url=base_url, api_key=api_key, max_retries=0, _strict_response_validation=True) as client:
        _cache_browser(client)
        with pytest.raises(AuthenticationError):
            client.browsers.fs.write_file("sess-1", b"payload", path="/tmp/x")
        assert client.browser_route_cache.get("sess-1") is None

        # The caller's next attempt goes to the control plane.
        client.browsers.fs.write_file("sess-1", b"payload", path="/tmp/x")

    assert vm.call_count == 1
    api_req = cast(httpx.Request, cast(Any, api.calls[0]).request)
    assert api_req.content == b"payload"
    assert api_req.url.params.get("jwt") is None
    assert api_req.headers.get("Authorization") == f"Bearer {api_key}"


@pytest.mark.asyncio
@respx.mock
async def test_async_stale_direct_vm_jwt_evicts_route_without_retries_for_streamed_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    vm = respx.put("http://browser-session.test/browser/kernel/fs/write_file").mock(
        return_value=httpx.Response(403, text="Invalid JWT")
    )
    api = respx.put(f"{base_url}/browsers/sess-1/fs/write_file").mock(return_value=httpx.Response(201))

    async def _chunks() -> AsyncIterator[bytes]:
        yield b"chunk-one"

    async with AsyncKernel(
        base_url=base_url, api_key=api_key, max_retries=0, _strict_response_validation=True
    ) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        with pytest.raises(PermissionDeniedError):
            await client.browsers.fs.write_file("sess-1", _chunks(), path="/tmp/x")
        assert client.browser_route_cache.get("sess-1") is None

        await client.browsers.fs.write_file("sess-1", b"payload", path="/tmp/x")

    assert vm.call_count == 1
    api_req = cast(httpx.Request, cast(Any, api.calls[0]).request)
    assert api_req.url.params.get("jwt") is None
    assert api_req.headers.get("Authorization") == f"Bearer {api_key}"


@respx.mock
def test_load_extensions_multipart_encoding_is_unchanged(monkeypatch: pytest.MonkeyPatch) -> None:
    # Indexed names are scoped to fs.upload; every other multipart endpoint keeps
    # the client's generic array encoding.
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    extensions = respx.post(f"{base_url}/browsers/sess-1/extensions").mock(return_value=httpx.Response(204))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        _cache_browser(client)
        client.browsers.load_extensions(
            "sess-1",
            extensions=[
                {"name": "one", "zip_file": b"zip-one"},
                {"name": "two", "zip_file": b"zip-two"},
            ],
        )

    body = cast(httpx.Request, cast(Any, extensions.calls[0]).request).read()
    assert b'name="extensions[][name]"' in body
    assert b'name="extensions[][zip_file]"' in body
    assert b"extensions[0]" not in body


def test_generic_multipart_array_encoding_is_unchanged() -> None:
    from kernel._models import FinalRequestOptions

    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        request = client._build_request(  # pyright: ignore[reportPrivateUsage]
            FinalRequestOptions.construct(
                method="post",
                url="/foo",
                headers={"Content-Type": "multipart/form-data; boundary=abc"},
                json_data={"array": ["foo", "bar"]},
                files=[("foo.txt", b"hello world")],
            )
        )

    body = request.read()
    assert b'name="array[]"' in body
    assert b'name="array[0]"' not in body


def test_indexed_multipart_body_flattens_only_given_values() -> None:
    from kernel._types import omit
    from kernel.lib.multipart import indexed_multipart_body

    assert indexed_multipart_body(
        {
            "files": [
                {"dest_path": "/tmp/one", "mode": omit},
                {"dest_path": "/tmp/two"},
            ],
            "flag": True,
            "skipped": omit,
        }
    ) == {
        "files[0][dest_path]": "/tmp/one",
        "files[1][dest_path]": "/tmp/two",
        "flag": True,
    }


class _FailingSyncStream(httpx.SyncByteStream):
    """A response body that fails while it is being read."""

    @override
    def __iter__(self) -> Iterator[bytes]:
        raise httpx.ReadError("connection reset while reading the error body")


class _FailingAsyncStream(httpx.AsyncByteStream):
    @override
    async def __aiter__(self) -> AsyncIterator[bytes]:
        raise httpx.ReadError("connection reset while reading the error body")
        yield b""  # pragma: no cover - unreachable, keeps this an async generator


def test_stale_direct_vm_jwt_evicts_route_when_error_body_read_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    requests: list[httpx.Request] = []

    def handle_request(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if "browser-session.test" in str(request.url):
            return httpx.Response(401, stream=_FailingSyncStream(), headers={"content-type": "text/plain"})
        return httpx.Response(200, content=b"png", headers={"content-type": "image/png"})

    http_client = httpx.Client(transport=httpx.MockTransport(handle_request))
    with Kernel(
        base_url=base_url,
        api_key=api_key,
        max_retries=0,
        http_client=http_client,
        _strict_response_validation=True,
    ) as client:
        _cache_browser(client)
        with pytest.raises(APIConnectionError):
            client.browsers.computer.capture_screenshot("sess-1")
        # The status was known before the body read failed, so the dead route is gone.
        assert client.browser_route_cache.get("sess-1") is None

        client.browsers.computer.capture_screenshot("sess-1")

    assert str(requests[0].url).startswith("http://browser-session.test/browser/kernel/computer/screenshot")
    assert requests[1].url == httpx.URL(f"{base_url}/browsers/sess-1/computer/screenshot")
    assert requests[1].url.params.get("jwt") is None
    assert requests[1].headers.get("Authorization") == f"Bearer {api_key}"


@pytest.mark.asyncio
async def test_async_stale_direct_vm_jwt_evicts_route_when_error_body_read_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    requests: list[httpx.Request] = []

    async def handle_request(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if "browser-session.test" in str(request.url):
            return httpx.Response(403, stream=_FailingAsyncStream(), headers={"content-type": "text/plain"})
        return httpx.Response(200, content=b"png", headers={"content-type": "image/png"})

    http_client = httpx.AsyncClient(transport=httpx.MockTransport(handle_request))
    async with AsyncKernel(
        base_url=base_url,
        api_key=api_key,
        max_retries=0,
        http_client=http_client,
        _strict_response_validation=True,
    ) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        with pytest.raises(APIConnectionError):
            await client.browsers.computer.capture_screenshot("sess-1")
        assert client.browser_route_cache.get("sess-1") is None

        await client.browsers.computer.capture_screenshot("sess-1")

    assert str(requests[0].url).startswith("http://browser-session.test/browser/kernel/computer/screenshot")
    assert requests[1].url == httpx.URL(f"{base_url}/browsers/sess-1/computer/screenshot")
    assert requests[1].url.params.get("jwt") is None
    assert requests[1].headers.get("Authorization") == f"Bearer {api_key}"


def test_copied_client_registers_one_route_eviction_hook() -> None:
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        copied = client.copy(api_key="sk-456")
        assert copied.browser_route_cache is client.browser_route_cache
        hooks = client._client.event_hooks["response"]  # pyright: ignore[reportPrivateUsage]
        assert len(hooks) == 1


def test_route_eviction_hook_runs_before_caller_response_hooks(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    requests: list[httpx.Request] = []
    caller_hook_statuses: list[int] = []

    def handle_request(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if "browser-session.test" in str(request.url):
            return httpx.Response(401, stream=_FailingSyncStream(), headers={"content-type": "text/plain"})
        return httpx.Response(200, content=b"png", headers={"content-type": "image/png"})

    def caller_hook(response: httpx.Response) -> None:
        caller_hook_statuses.append(response.status_code)
        if response.status_code in {401, 403}:
            # Reading a failing body raises out of the hook chain, which would
            # skip any eviction hook registered after this one.
            response.read()

    http_client = httpx.Client(
        transport=httpx.MockTransport(handle_request),
        event_hooks={"response": [caller_hook]},
    )
    with Kernel(
        base_url=base_url,
        api_key=api_key,
        max_retries=0,
        http_client=http_client,
        _strict_response_validation=True,
    ) as client:
        _cache_browser(client)
        assert http_client.event_hooks["response"][-1] is caller_hook
        with pytest.raises(APIConnectionError):
            client.browsers.computer.capture_screenshot("sess-1")
        assert caller_hook_statuses == [401]
        assert client.browser_route_cache.get("sess-1") is None

        client.browsers.computer.capture_screenshot("sess-1")

    assert str(requests[0].url).startswith("http://browser-session.test/browser/kernel/computer/screenshot")
    assert requests[1].url == httpx.URL(f"{base_url}/browsers/sess-1/computer/screenshot")
    assert requests[1].url.params.get("jwt") is None
    assert requests[1].headers.get("Authorization") == f"Bearer {api_key}"


@pytest.mark.asyncio
async def test_async_route_eviction_hook_runs_before_caller_response_hooks(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("KERNEL_BROWSER_ROUTING_SUBRESOURCES", raising=False)
    requests: list[httpx.Request] = []
    caller_hook_statuses: list[int] = []

    async def handle_request(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if "browser-session.test" in str(request.url):
            return httpx.Response(403, stream=_FailingAsyncStream(), headers={"content-type": "text/plain"})
        return httpx.Response(200, content=b"png", headers={"content-type": "image/png"})

    async def caller_hook(response: httpx.Response) -> None:
        caller_hook_statuses.append(response.status_code)
        if response.status_code in {401, 403}:
            await response.aread()

    http_client = httpx.AsyncClient(
        transport=httpx.MockTransport(handle_request),
        event_hooks={"response": [caller_hook]},
    )
    async with AsyncKernel(
        base_url=base_url,
        api_key=api_key,
        max_retries=0,
        http_client=http_client,
        _strict_response_validation=True,
    ) as client:
        route = browser_route_from_browser(_fake_browser())
        assert route is not None
        client.browser_route_cache.set(route)
        assert http_client.event_hooks["response"][-1] is caller_hook
        with pytest.raises(APIConnectionError):
            await client.browsers.computer.capture_screenshot("sess-1")
        assert caller_hook_statuses == [403]
        assert client.browser_route_cache.get("sess-1") is None

        await client.browsers.computer.capture_screenshot("sess-1")

    assert str(requests[0].url).startswith("http://browser-session.test/browser/kernel/computer/screenshot")
    assert requests[1].url == httpx.URL(f"{base_url}/browsers/sess-1/computer/screenshot")
    assert requests[1].url.params.get("jwt") is None
    assert requests[1].headers.get("Authorization") == f"Bearer {api_key}"


def test_route_eviction_hook_is_registered_once_before_caller_hooks() -> None:
    def caller_hook(_response: httpx.Response) -> None:  # pragma: no cover - never invoked
        return None

    http_client = httpx.Client(event_hooks={"response": [caller_hook]})
    with Kernel(
        base_url=base_url,
        api_key=api_key,
        http_client=http_client,
        _strict_response_validation=True,
    ) as client:
        client.copy(api_key="sk-456")
        hooks = http_client.event_hooks["response"]
        assert len(hooks) == 2
        assert hooks[1] is caller_hook
