from __future__ import annotations

import os
import json

import httpx
import respx
import pytest

from kernel import Kernel
from kernel.lib.browser_scoped.util import jwt_from_cdp_ws_url

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "sk-123"


def _fake_browser() -> dict[str, str]:
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


def test_jwt_from_cdp_ws_url() -> None:
    assert jwt_from_cdp_ws_url("wss://h/browser/cdp?jwt=abc%2Fdef&x=1") == "abc/def"


@respx.mock
def test_for_browser_process_exec_routes_to_session_base() -> None:
    route = respx.post("http://browser-session.test/browser/kernel/process/exec?jwt=token-abc").mock(
        return_value=httpx.Response(
            200,
            json={
                "exit_code": 0,
                "stdout_b64": "",
                "stderr_b64": "",
            },
        )
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        b = client.for_browser(_fake_browser())
        out = b.process.exec(command="echo", args=["hi"])
    assert route.called
    sent = route.calls[0].request.read().decode()
    body = json.loads(sent)
    assert body["command"] == "echo"
    assert body["args"] == ["hi"]
    assert out.exit_code == 0


@respx.mock
def test_browser_request_uses_curl_raw() -> None:
    route = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        b = client.for_browser(_fake_browser())
        r = b.request("GET", "https://example.com", params={"timeout_ms": 5000})
    assert r.status_code == 200
    assert r.content == b"ok"
    assert route.called
    assert "curl/raw" in str(route.calls[0].request.url)
    assert "jwt=token-abc" in str(route.calls[0].request.url)


@respx.mock
def test_browser_request_params_cannot_override_target_url_or_jwt() -> None:
    route = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"ok")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        b = client.for_browser(_fake_browser())
        b.request(
            "GET",
            "https://example.com",
            params={"url": "https://evil.example", "jwt": "other", "timeout_ms": 1},
        )
    assert route.called
    req_url = route.calls[0].request.url
    assert str(req_url.params.get("url")) == "https://example.com"
    assert str(req_url.params.get("jwt")) == "token-abc"
    assert str(req_url.params.get("timeout_ms")) == "1"


@respx.mock
def test_browser_stream_params_cannot_override_target_url_or_jwt() -> None:
    route = respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"streamed")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        b = client.for_browser(_fake_browser())
        with b.stream(
            "GET",
            "https://example.com",
            params={"url": "https://evil.example", "jwt": "other"},
        ) as resp:
            assert resp.status_code == 200
            assert resp.read() == b"streamed"
    assert route.called
    req_url = route.calls[0].request.url
    assert str(req_url.params.get("url")) == "https://example.com"
    assert str(req_url.params.get("jwt")) == "token-abc"


@respx.mock
def test_browser_stream_reads_body() -> None:
    respx.get("http://browser-session.test/browser/kernel/curl/raw").mock(
        return_value=httpx.Response(200, content=b"streamed")
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        b = client.for_browser(_fake_browser())
        with b.stream("GET", "https://example.com") as resp:
            assert resp.status_code == 200
            assert resp.read() == b"streamed"


def test_for_browser_requires_base_url() -> None:
    bad = {**_fake_browser(), "base_url": None}
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        with pytest.raises(ValueError, match="base_url"):
            client.for_browser(bad)
