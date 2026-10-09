import httpx
import pytest

from kernel import Kernel, AsyncKernel, NotFoundError, APIResponseValidationError


def test_acquire_returns_browser() -> None:
    browser = {
        "cdp_ws_url": "wss://example.test/cdp",
        "created_at": "2026-10-09T00:00:00Z",
        "headless": True,
        "memory": "1GiB",
        "region": "us-east",
        "session_id": "session-1",
        "stealth": False,
        "webdriver_ws_url": "wss://example.test/webdriver",
    }
    with Kernel(
        api_key="test",
        http_client=httpx.Client(transport=httpx.MockTransport(lambda _request: httpx.Response(200, json=browser))),
    ) as client:
        result = client.browser_pools.acquire("pool")
        assert result is not None
        assert result.session_id == "session-1"


def test_acquire_returns_none_on_poll_timeout() -> None:
    calls = 0

    def handle(_request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(204)

    with Kernel(api_key="test", http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
        assert client.browser_pools.acquire("pool") is None
        response = client.browser_pools.with_raw_response.acquire("pool")
        assert response.status_code == 204
        assert response.parse() is None
        assert response.parse(to=str) == ""
        assert response.parse(to=bytes) == b""
        assert response.parse(to=httpx.Response) is response.http_response
        assert calls == 2


async def test_async_acquire_returns_none_on_poll_timeout() -> None:
    async with AsyncKernel(
        api_key="test",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(lambda _request: httpx.Response(204))),
    ) as client:
        assert await client.browser_pools.acquire("pool") is None


def test_acquire_still_raises_not_found() -> None:
    with Kernel(
        api_key="test",
        http_client=httpx.Client(transport=httpx.MockTransport(lambda _request: httpx.Response(404, json={}))),
    ) as client:
        with pytest.raises(NotFoundError):
            client.browser_pools.acquire("missing")


def test_unexpected_204_still_fails_strict_validation() -> None:
    with Kernel(
        api_key="test",
        _strict_response_validation=True,
        http_client=httpx.Client(transport=httpx.MockTransport(lambda _request: httpx.Response(204))),
    ) as client:
        with pytest.raises(APIResponseValidationError):
            client.browser_pools.retrieve("pool")
