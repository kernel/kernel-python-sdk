from __future__ import annotations

import asyncio
from typing import Any
from collections.abc import Iterator

import httpx
import pytest

from kernel import Kernel, AsyncKernel
from kernel._exceptions import KernelError


def analysis_response(
    status: str,
    *,
    analysis_id: str = "analysis-1",
    finished_at: str | None = None,
) -> dict[str, Any]:
    return {
        "analysis": {
            "id": analysis_id,
            "created_at": "2026-09-16T00:00:00Z",
            "expires_at": "2026-09-16T00:45:00Z",
            "failure": None,
            "finished_at": finished_at,
            "status": status,
            "intent": None,
        },
        "recommendation": None,
        "target": {
            "domain": "example.com",
            "host": "example.com",
            "normalized": "https://example.com/",
        },
        "working_configurations": [],
        "guidance": None,
        "workload_outcome": None,
    }


def response_sequence(payloads: list[dict[str, Any]]) -> tuple[httpx.MockTransport, list[httpx.Request]]:
    remaining: Iterator[dict[str, Any]] = iter(payloads)
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=next(remaining))

    return httpx.MockTransport(handler), requests


def test_wait_for_result_polls_unknown_unfinished_status_until_finished() -> None:
    transport, requests = response_sequence(
        [
            analysis_response("running"),
            analysis_response("queued"),
            analysis_response("archived", finished_at="2026-09-16T00:01:00Z"),
        ]
    )

    with httpx.Client(transport=transport) as http_client:
        client = Kernel(api_key="test", base_url="https://api.example", http_client=http_client)
        result = client.config_registry.analyses.wait_for_result(
            "analysis-1",
            poll_interval=0.001,
            extra_headers={"X-Test": "preserved", "X-Stainless-Poll-Helper": "caller"},
        )

    assert result.analysis is not None
    assert result.analysis.status == "archived"
    assert len(requests) == 3
    assert all(request.headers["X-Test"] == "preserved" for request in requests)
    assert all(request.headers["X-Stainless-Poll-Helper"] == "true" for request in requests)


@pytest.mark.parametrize("status", ["completed", "failed", "canceled", "expired"])
def test_wait_for_result_returns_known_terminal_status_without_finished_at(status: str) -> None:
    transport, requests = response_sequence([analysis_response(status)])

    with httpx.Client(transport=transport) as http_client:
        client = Kernel(api_key="test", base_url="https://api.example", http_client=http_client)
        result = client.config_registry.analyses.wait_for_result("analysis-1")

    assert result.analysis is not None
    assert result.analysis.status == status
    assert len(requests) == 1


def test_wait_for_result_zero_max_wait_reads_once_then_times_out() -> None:
    transport, requests = response_sequence([analysis_response("running")])

    with httpx.Client(transport=transport) as http_client:
        client = Kernel(api_key="test", base_url="https://api.example", http_client=http_client)
        with pytest.raises(TimeoutError, match="analysis-1"):
            client.config_registry.analyses.wait_for_result("analysis-1", max_wait_seconds=0)

    assert len(requests) == 1


@pytest.mark.parametrize(
    "payload, message",
    [
        ({"analysis": None}, "missing an analysis"),
        (analysis_response("running", analysis_id="analysis-2"), "analysis-2"),
    ],
)
def test_wait_for_result_rejects_invalid_analysis_response(payload: dict[str, Any], message: str) -> None:
    transport, _ = response_sequence([payload])

    with httpx.Client(transport=transport) as http_client:
        client = Kernel(api_key="test", base_url="https://api.example", http_client=http_client)
        with pytest.raises(KernelError, match=message):
            client.config_registry.analyses.wait_for_result("analysis-1")


def test_wait_for_result_rejects_missing_finished_at() -> None:
    payload = analysis_response("running")
    analysis = payload["analysis"]
    assert isinstance(analysis, dict)
    del analysis["finished_at"]
    transport, _ = response_sequence([payload])

    with httpx.Client(transport=transport) as http_client:
        client = Kernel(api_key="test", base_url="https://api.example", http_client=http_client)
        with pytest.raises(KernelError, match="finished_at"):
            client.config_registry.analyses.wait_for_result("analysis-1")


@pytest.mark.parametrize(
    "kwargs",
    [
        {"poll_interval": 0},
        {"poll_interval": float("nan")},
        {"max_wait_seconds": -1},
        {"max_wait_seconds": float("inf")},
    ],
)
def test_wait_for_result_rejects_invalid_timing_options(kwargs: dict[str, float]) -> None:
    client = Kernel(api_key="test", base_url="https://api.example")

    with pytest.raises(ValueError):
        client.config_registry.analyses.wait_for_result("analysis-1", **kwargs)  # type: ignore[arg-type]


async def test_async_wait_for_result_matches_sync_behavior() -> None:
    transport, requests = response_sequence(
        [
            analysis_response("running"),
            analysis_response("completed", finished_at="2026-09-16T00:01:00Z"),
        ]
    )

    async with httpx.AsyncClient(transport=transport) as http_client:
        client = AsyncKernel(api_key="test", base_url="https://api.example", http_client=http_client)
        result = await client.config_registry.analyses.wait_for_result("analysis-1", poll_interval=0.001)

    assert result.analysis is not None
    assert result.analysis.status == "completed"
    assert len(requests) == 2


async def test_async_wait_for_result_is_cancellable_during_poll_sleep() -> None:
    first_request = asyncio.Event()
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        first_request.set()
        return httpx.Response(200, json=analysis_response("running"))

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http_client:
        client = AsyncKernel(api_key="test", base_url="https://api.example", http_client=http_client)
        task = asyncio.create_task(client.config_registry.analyses.wait_for_result("analysis-1", poll_interval=60))
        await first_request.wait()
        await asyncio.sleep(0)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task

    assert len(requests) == 1
