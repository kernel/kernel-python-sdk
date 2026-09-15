from __future__ import annotations

import httpx
import pytest

from kernel import Kernel, AsyncKernel, APIStatusError, APIConnectionError


@pytest.mark.parametrize("failure", ["connection", 409, 429, 500])
def test_fill_does_not_retry(failure: str | int) -> None:
    calls = 0

    def handle(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if isinstance(failure, str):
            raise httpx.ReadError("connection lost", request=request)
        return httpx.Response(failure, json={})

    with Kernel(
        api_key="test", max_retries=1, http_client=httpx.Client(transport=httpx.MockTransport(handle))
    ) as client:
        with pytest.raises((APIConnectionError, APIStatusError)):
            client.vaults.items.perform_operation(
                "login",
                id_or_name="vault",
                type="fill",
                browser_id="browser",
                fields=[{"field": "password", "selector": "#password"}],
            )
        assert calls == 1
        assert client.max_retries == 1


@pytest.mark.parametrize("failure", ["connection", 409, 429, 500])
async def test_async_fill_does_not_retry(failure: str | int) -> None:
    calls = 0

    def handle(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if isinstance(failure, str):
            raise httpx.ReadError("connection lost", request=request)
        return httpx.Response(failure, json={})

    async with AsyncKernel(
        api_key="test", max_retries=1, http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))
    ) as client:
        with pytest.raises((APIConnectionError, APIStatusError)):
            await client.vaults.items.perform_operation(
                "login",
                id_or_name="vault",
                type="fill",
                browser_id="browser",
                fields=[{"field": "password", "selector": "#password"}],
            )
        assert calls == 1
        assert client.max_retries == 1


def test_reads_keep_client_retries() -> None:
    calls = 0

    def handle(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        raise httpx.ReadError("connection lost", request=request)

    with Kernel(
        api_key="test", max_retries=1, http_client=httpx.Client(transport=httpx.MockTransport(handle))
    ) as client:
        with pytest.raises(APIConnectionError):
            client.vaults.items.retrieve("login", id_or_name="vault")
    assert calls == 2
