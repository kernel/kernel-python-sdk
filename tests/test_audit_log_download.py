from __future__ import annotations

import hashlib
import threading
from io import BytesIO
from typing import BinaryIO, cast

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel, InternalServerError, AuditLogDownloadError
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


async def test_async_download_writes_verified_chunks(
    async_client: AsyncKernel, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    respx_mock.get("/audit-logs/export/chunk").mock(
        side_effect=[
            chunk_response(b"first", rows=2, has_more=True, next_cursor="next"),
            chunk_response(b"second", rows=1, has_more=False),
        ]
    )
    thread_ids: list[int] = []
    write_chunk = audit_log_download._write_chunk

    def record_write(destination: BinaryIO, body: bytes) -> None:
        thread_ids.append(threading.get_ident())
        write_chunk(destination, body)

    monkeypatch.setattr(audit_log_download, "_write_chunk", record_write)
    destination = BytesIO()
    progress_called = False

    async def on_progress(_: object) -> None:
        nonlocal progress_called
        progress_called = True

    result = await async_client.audit_logs.download(
        to=destination,
        start="2026-06-01T00:00:00Z",
        end="2026-06-02T00:00:00Z",
        on_progress=on_progress,
    )

    assert destination.getvalue() == b"firstsecond"
    assert result.bytes_written == 11
    assert result.chunks == 2
    assert result.rows == 3
    assert progress_called
    assert thread_ids and all(thread_id != threading.get_ident() for thread_id in thread_ids)


async def test_async_download_retries_checksum_mismatch(
    async_client: AsyncKernel, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    async def no_sleep(_: float) -> None:
        pass

    monkeypatch.setattr(audit_log_download.anyio, "sleep", no_sleep)
    bad = chunk_response(b"bad", rows=1, has_more=False)
    bad.headers["x-content-sha256"] = hashlib.sha256(b"good").hexdigest()
    route = respx_mock.get("/audit-logs/export/chunk").mock(
        side_effect=[bad, chunk_response(b"good", rows=1, has_more=False)]
    )
    destination = BytesIO()

    await async_client.audit_logs.download(
        to=destination,
        start="2026-06-01T00:00:00Z",
        end="2026-06-02T00:00:00Z",
    )

    assert destination.getvalue() == b"good"
    assert route.call_count == 2


async def test_async_download_uses_client_http_retries(async_client: AsyncKernel, respx_mock: MockRouter) -> None:
    route = respx_mock.get("/audit-logs/export/chunk").mock(
        side_effect=[
            httpx.Response(500, json={"message": "temporary failure"}),
            chunk_response(b"good", rows=1, has_more=False),
        ]
    )

    await async_client.audit_logs.download(
        to=BytesIO(),
        start="2026-06-01T00:00:00Z",
        end="2026-06-02T00:00:00Z",
    )

    assert route.call_count == 2


async def test_async_download_respects_disabled_http_retries(async_client: AsyncKernel, respx_mock: MockRouter) -> None:
    route = respx_mock.get("/audit-logs/export/chunk").mock(
        return_value=httpx.Response(500, json={"message": "temporary failure"})
    )

    with pytest.raises(InternalServerError, match="500"):
        await async_client.with_options(max_retries=0).audit_logs.download(
            to=BytesIO(),
            start="2026-06-01T00:00:00Z",
            end="2026-06-02T00:00:00Z",
        )

    assert route.call_count == 1


@pytest.mark.parametrize("row_count", ["", "1.0", "50001"])
def test_download_rejects_invalid_row_count(row_count: str, client: Kernel, respx_mock: MockRouter) -> None:
    response = chunk_response(b"chunk", rows=1, has_more=False)
    response.headers["x-row-count"] = row_count
    respx_mock.get("/audit-logs/export/chunk").mock(return_value=response)
    destination = BytesIO()

    with pytest.raises(AuditLogDownloadError, match="response missing or invalid X-Row-Count header"):
        client.audit_logs.download(
            to=destination,
            start="2026-06-01T00:00:00Z",
            end="2026-06-02T00:00:00Z",
        )

    assert destination.getvalue() == b""


class InvalidWriteDestination:
    def __init__(self, result: object) -> None:
        self.result = result

    def write(self, _: object) -> object:
        return self.result


@pytest.mark.parametrize("write_result", [float("nan"), 0.5, True])
def test_download_rejects_invalid_write_result(write_result: object, client: Kernel, respx_mock: MockRouter) -> None:
    respx_mock.get("/audit-logs/export/chunk").mock(return_value=chunk_response(b"chunk", rows=1, has_more=False))

    with pytest.raises(AuditLogDownloadError, match="audit log download destination performed a short write"):
        client.audit_logs.download(
            to=cast(BinaryIO, InvalidWriteDestination(write_result)),
            start="2026-06-01T00:00:00Z",
            end="2026-06-02T00:00:00Z",
        )


@pytest.mark.parametrize("max_transfer_retries", [True, 1.5])
def test_download_rejects_invalid_transfer_retry_count(max_transfer_retries: object, client: Kernel) -> None:
    with pytest.raises(ValueError, match="max_transfer_retries must be a non-negative integer"):
        client.audit_logs.download(
            to=BytesIO(),
            start="2026-06-01T00:00:00Z",
            end="2026-06-02T00:00:00Z",
            max_transfer_retries=cast(int, max_transfer_retries),
        )


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


def test_download_uses_client_http_retries(client: Kernel, respx_mock: MockRouter) -> None:
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


def test_download_respects_disabled_http_retries(client: Kernel, respx_mock: MockRouter) -> None:
    route = respx_mock.get("/audit-logs/export/chunk").mock(
        return_value=httpx.Response(500, json={"message": "temporary failure"})
    )

    with pytest.raises(InternalServerError, match="500"):
        client.with_options(max_retries=0).audit_logs.download(
            to=BytesIO(),
            start="2026-06-01T00:00:00Z",
            end="2026-06-02T00:00:00Z",
        )

    assert route.call_count == 1


def test_download_respects_transfer_retry_limit(client: Kernel, respx_mock: MockRouter) -> None:
    bad = chunk_response(b"bad", rows=1, has_more=False)
    bad.headers["x-content-sha256"] = hashlib.sha256(b"good").hexdigest()
    route = respx_mock.get("/audit-logs/export/chunk").mock(return_value=bad)

    with pytest.raises(AuditLogDownloadError, match="checksum mismatch"):
        client.audit_logs.download(
            to=BytesIO(),
            start="2026-06-01T00:00:00Z",
            end="2026-06-02T00:00:00Z",
            max_transfer_retries=0,
        )

    assert route.call_count == 1


def test_download_rejects_cursor_cycle(client: Kernel, respx_mock: MockRouter) -> None:
    respx_mock.get("/audit-logs/export/chunk").mock(
        side_effect=[
            chunk_response(b"first", rows=1, has_more=True, next_cursor="a"),
            chunk_response(b"second", rows=1, has_more=True, next_cursor="b"),
            chunk_response(b"duplicate", rows=1, has_more=True, next_cursor="a"),
        ]
    )
    destination = BytesIO()

    with pytest.raises(AuditLogDownloadError, match="response repeated X-Next-Cursor header"):
        client.audit_logs.download(
            to=destination,
            start="2026-06-01T00:00:00Z",
            end="2026-06-02T00:00:00Z",
        )

    assert destination.getvalue() == b"firstsecond"


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
