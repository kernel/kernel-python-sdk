from __future__ import annotations

import os

import httpx
import respx
import pytest

from kernel import Kernel, AsyncKernel, NotFoundError
from kernel.lib.browser_pools import Acquired, TimedOut, acquire, acquire_async

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "sk-123"


def _browser_payload() -> dict[str, object]:
    return {
        "session_id": "sess-1",
        "base_url": "http://browser-session.test/browser/kernel",
        "cdp_ws_url": "wss://browser-session.test/browser/cdp?jwt=t",
        "webdriver_ws_url": "wss://x",
        "created_at": "2020-01-01T00:00:00Z",
        "headless": True,
        "stealth": False,
        "timeout_seconds": 60,
    }


@respx.mock
def test_acquire_returns_acquired_on_200() -> None:
    respx.post(f"{base_url}/browser_pools/my-pool/acquire").mock(
        return_value=httpx.Response(200, json=_browser_payload())
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        result = acquire(client, "my-pool")

    assert isinstance(result, Acquired)
    assert result.browser.session_id == "sess-1"


@respx.mock
def test_acquire_returns_timed_out_on_204() -> None:
    respx.post(f"{base_url}/browser_pools/my-pool/acquire").mock(return_value=httpx.Response(204))
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        result = acquire(client, "my-pool")

    assert isinstance(result, TimedOut)


@respx.mock
def test_acquire_raises_not_found_on_404() -> None:
    respx.post(f"{base_url}/browser_pools/missing/acquire").mock(
        return_value=httpx.Response(404, json={"code": "not_found", "message": "pool not found"})
    )
    with Kernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        with pytest.raises(NotFoundError):
            acquire(client, "missing")


@pytest.mark.asyncio
@respx.mock
async def test_acquire_async_returns_timed_out_on_204() -> None:
    respx.post(f"{base_url}/browser_pools/my-pool/acquire").mock(return_value=httpx.Response(204))
    async with AsyncKernel(base_url=base_url, api_key=api_key, _strict_response_validation=True) as client:
        result = await acquire_async(client, "my-pool")

    assert isinstance(result, TimedOut)
