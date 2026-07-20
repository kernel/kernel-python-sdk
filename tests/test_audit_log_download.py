from __future__ import annotations

import hashlib
from io import BytesIO

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel, AuditLogDownloadError
from kernel.lib import audit_log_download


def chunk_response(body: bytes, *, rows: int, has_more: bool, next_cursor: str | None = None) -> httpx.Response:
    headers = {
        "x-content-sha256": hashlib.sha256(body).hexdigest(),
        "x-has-more": str(has_more).lower(),
        "x-row-count": str(rows),
    }
    if next_cursor is not None:
        headers["x-next-cursor"] = next_cursor
    return httpx.Response(200, content=body, headers=headers)


def test_download_writes_verified_chunks(client: Kernel, respx_mock: MockRouter) -> None:
    responses = iter(
        [
            chunk_response(b"first", rows=2, has_more=True, next_cursor="next"),
            chunk_response(b"second", rows=1, has_more=False),
        ]
    )
    cursors: list[str | None] = []

    def respond(request: httpx.Request) -> httpx.Response:
        cursors.append(request.url.params.get("cursor"))
        return next(responses)

    respx_mock.get("/audit-logs/export/chunk").mock(side_effect=respond)
    destination = BytesIO()
    progress: list[tuple[int, int, int, int]] = []

    result = client.audit_logs.download(
        to=destination,
        start="2026-06-01T00:00:00Z",
        end="2026-06-02T00:00:00Z",
        format="jsonl.gz",
        on_progress=lambda update: progress.append(
            (update.bytes_written, update.chunks, update.rows, update.chunk_rows)
        ),
    )

    assert destination.getvalue() == b"firstsecond"
    assert result.bytes_written == 11
    assert result.chunks == 2
    assert result.rows == 3
    assert progress == [(5, 1, 2, 2), (11, 2, 3, 1)]
    assert cursors == [None, "next"]


async def test_async_download_writes_verified_chunks(async_client: AsyncKernel, respx_mock: MockRouter) -> None:
    respx_mock.get("/audit-logs/export/chunk").mock(
        side_effect=[
            chunk_response(b"first", rows=2, has_more=True, next_cursor="next"),
            chunk_response(b"second", rows=1, has_more=False),
        ]
    )
    destination = BytesIO()

    result = await async_client.audit_logs.download(
        to=destination,
        start="2026-06-01T00:00:00Z",
        end="2026-06-02T00:00:00Z",
    )

    assert destination.getvalue() == b"firstsecond"
    assert result.bytes_written == 11
    assert result.chunks == 2
    assert result.rows == 3


def test_download_retries_checksum_mismatch(
    client: Kernel, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    def no_sleep(_: float) -> None:
        pass

    monkeypatch.setattr(audit_log_download.time, "sleep", no_sleep)
    bad = chunk_response(b"bad", rows=1, has_more=False)
    bad.headers["x-content-sha256"] = hashlib.sha256(b"good").hexdigest()
    route = respx_mock.get("/audit-logs/export/chunk").mock(
        side_effect=[bad, chunk_response(b"good", rows=1, has_more=False)]
    )
    destination = BytesIO()

    client.audit_logs.download(
        to=destination,
        start="2026-06-01T00:00:00Z",
        end="2026-06-02T00:00:00Z",
    )

    assert destination.getvalue() == b"good"
    assert route.call_count == 2


def test_download_owns_http_retries(client: Kernel, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
    delays: list[float] = []
    monkeypatch.setattr(audit_log_download.time, "sleep", delays.append)
    route = respx_mock.get("/audit-logs/export/chunk").mock(
        side_effect=[
            httpx.Response(500, json={"message": "temporary failure"}),
            chunk_response(b"good", rows=1, has_more=False),
        ]
    )

    client.audit_logs.download(
        to=BytesIO(),
        start="2026-06-01T00:00:00Z",
        end="2026-06-02T00:00:00Z",
    )

    assert route.call_count == 2
    assert delays == [1]


def test_download_rejects_invalid_cursor_before_writing(client: Kernel, respx_mock: MockRouter) -> None:
    respx_mock.get("/audit-logs/export/chunk").mock(return_value=chunk_response(b"chunk", rows=1, has_more=True))
    destination = BytesIO()

    with pytest.raises(AuditLogDownloadError, match="response has invalid X-Next-Cursor header"):
        client.audit_logs.download(
            to=destination,
            start="2026-06-01T00:00:00Z",
            end="2026-06-02T00:00:00Z",
        )

    assert destination.getvalue() == b""
