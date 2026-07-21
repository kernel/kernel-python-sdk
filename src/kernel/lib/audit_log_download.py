from __future__ import annotations

import time
import hashlib
import inspect
from typing import BinaryIO, Callable, Optional, Protocol, Awaitable, ContextManager, AsyncContextManager
from dataclasses import dataclass

import anyio
import httpx
from anyio import to_thread

from .._exceptions import KernelError

_DEFAULT_MAX_TRANSFER_RETRIES = 6
_MAX_CHUNK_ROWS = 50_000
_MAX_RETRY_DELAY = 8.0


class AuditLogDownloadError(KernelError):
    pass


@dataclass(frozen=True)
class AuditLogDownloadResult:
    bytes_written: int
    chunks: int
    rows: int


@dataclass(frozen=True)
class AuditLogDownloadProgress(AuditLogDownloadResult):
    chunk_rows: int


class _SyncChunkResponse(Protocol):
    @property
    def headers(self) -> httpx.Headers: ...

    def read(self) -> bytes: ...

    def close(self) -> None: ...


class _AsyncChunkResponse(Protocol):
    @property
    def headers(self) -> httpx.Headers: ...

    async def read(self) -> bytes: ...

    async def close(self) -> None: ...


SyncFetchChunk = Callable[[Optional[str]], ContextManager[_SyncChunkResponse]]
AsyncFetchChunk = Callable[[Optional[str]], AsyncContextManager[_AsyncChunkResponse]]
ProgressCallback = Callable[[AuditLogDownloadProgress], None]
AsyncProgressCallback = Callable[[AuditLogDownloadProgress], Optional[Awaitable[None]]]


def download_audit_logs(
    fetch_chunk: SyncFetchChunk,
    destination: BinaryIO,
    *,
    on_progress: ProgressCallback | None = None,
    max_transfer_retries: int = _DEFAULT_MAX_TRANSFER_RETRIES,
) -> AuditLogDownloadResult:
    if not callable(getattr(destination, "write", None)):
        raise TypeError("audit log download destination must provide write()")
    _validate_max_transfer_retries(max_transfer_retries)

    cursor: str | None = None
    result = AuditLogDownloadResult(bytes_written=0, chunks=0, rows=0)
    seen_cursors: set[str] = set()
    while True:
        body, headers = _fetch_verified_chunk(fetch_chunk, cursor, max_transfer_retries)
        chunk_rows, next_cursor, has_more = _parse_chunk_headers(headers, cursor)
        if has_more and next_cursor is not None:
            if next_cursor in seen_cursors:
                raise AuditLogDownloadError("response repeated X-Next-Cursor header")
            seen_cursors.add(next_cursor)
        _write_chunk(destination, body)

        cursor = next_cursor
        result = AuditLogDownloadResult(
            bytes_written=result.bytes_written + len(body),
            chunks=result.chunks + 1,
            rows=result.rows + chunk_rows,
        )
        if on_progress is not None:
            on_progress(
                AuditLogDownloadProgress(
                    bytes_written=result.bytes_written,
                    chunks=result.chunks,
                    rows=result.rows,
                    chunk_rows=chunk_rows,
                )
            )
        if not has_more:
            return result


async def async_download_audit_logs(
    fetch_chunk: AsyncFetchChunk,
    destination: BinaryIO,
    *,
    on_progress: AsyncProgressCallback | None = None,
    max_transfer_retries: int = _DEFAULT_MAX_TRANSFER_RETRIES,
) -> AuditLogDownloadResult:
    if not callable(getattr(destination, "write", None)):
        raise TypeError("audit log download destination must provide write()")
    _validate_max_transfer_retries(max_transfer_retries)

    cursor: str | None = None
    result = AuditLogDownloadResult(bytes_written=0, chunks=0, rows=0)
    seen_cursors: set[str] = set()
    while True:
        body, headers = await _async_fetch_verified_chunk(fetch_chunk, cursor, max_transfer_retries)
        chunk_rows, next_cursor, has_more = _parse_chunk_headers(headers, cursor)
        if has_more and next_cursor is not None:
            if next_cursor in seen_cursors:
                raise AuditLogDownloadError("response repeated X-Next-Cursor header")
            seen_cursors.add(next_cursor)
        await to_thread.run_sync(_write_chunk, destination, body)

        cursor = next_cursor
        result = AuditLogDownloadResult(
            bytes_written=result.bytes_written + len(body),
            chunks=result.chunks + 1,
            rows=result.rows + chunk_rows,
        )
        if on_progress is not None:
            callback_result = on_progress(
                AuditLogDownloadProgress(
                    bytes_written=result.bytes_written,
                    chunks=result.chunks,
                    rows=result.rows,
                    chunk_rows=chunk_rows,
                )
            )
            if inspect.isawaitable(callback_result):
                await callback_result
        if not has_more:
            return result


def _fetch_verified_chunk(
    fetch_chunk: SyncFetchChunk, cursor: str | None, max_transfer_retries: int
) -> tuple[bytes, httpx.Headers]:
    for retries in range(max_transfer_retries + 1):
        transfer_error: Exception | None = None
        with fetch_chunk(cursor) as response:
            try:
                body = response.read()
                headers = httpx.Headers(response.headers)
                _verify_checksum(body, headers)
            except Exception as error:
                transfer_error = error
            else:
                return body, headers
        assert transfer_error is not None
        if retries == max_transfer_retries:
            raise transfer_error
        time.sleep(min(2**retries, _MAX_RETRY_DELAY))
    raise AssertionError("unreachable")


async def _async_fetch_verified_chunk(
    fetch_chunk: AsyncFetchChunk, cursor: str | None, max_transfer_retries: int
) -> tuple[bytes, httpx.Headers]:
    for retries in range(max_transfer_retries + 1):
        transfer_error: Exception | None = None
        async with fetch_chunk(cursor) as response:
            try:
                body = await response.read()
                headers = httpx.Headers(response.headers)
                await to_thread.run_sync(_verify_checksum, body, headers)
            except Exception as error:
                transfer_error = error
            else:
                return body, headers
        assert transfer_error is not None
        if retries == max_transfer_retries:
            raise transfer_error
        await anyio.sleep(min(2**retries, _MAX_RETRY_DELAY))
    raise AssertionError("unreachable")


def _verify_checksum(body: bytes, headers: httpx.Headers) -> None:
    expected = headers.get("x-content-sha256")
    if not expected:
        raise AuditLogDownloadError("response missing X-Content-Sha256 header")
    actual = hashlib.sha256(body).hexdigest()
    if actual != expected:
        raise AuditLogDownloadError(f"audit log chunk checksum mismatch (got {actual}, want {expected})")


def _parse_chunk_headers(headers: httpx.Headers, current_cursor: str | None) -> tuple[int, str | None, bool]:
    has_more_value = headers.get("x-has-more")
    if has_more_value not in {"true", "false"}:
        raise AuditLogDownloadError("response missing or invalid X-Has-More header")
    has_more = has_more_value == "true"

    row_count = headers.get("x-row-count")
    if row_count is None or not row_count.isascii() or not row_count.isdecimal():
        raise AuditLogDownloadError("response missing or invalid X-Row-Count header")
    normalized_row_count = row_count.lstrip("0") or "0"
    if len(normalized_row_count) > len(str(_MAX_CHUNK_ROWS)):
        raise AuditLogDownloadError("response missing or invalid X-Row-Count header")
    rows = int(normalized_row_count)
    if rows > _MAX_CHUNK_ROWS:
        raise AuditLogDownloadError("response missing or invalid X-Row-Count header")

    next_cursor = headers.get("x-next-cursor") or None
    if has_more and (not next_cursor or next_cursor == current_cursor):
        raise AuditLogDownloadError("response has invalid X-Next-Cursor header")
    if not has_more and next_cursor:
        raise AuditLogDownloadError("response returned a cursor after the final chunk")
    return rows, next_cursor, has_more


def _write_chunk(destination: BinaryIO, body: bytes) -> None:
    remaining = memoryview(body)
    while remaining:
        written = destination.write(remaining)
        if type(written) is not int or written <= 0 or written > len(remaining):
            raise AuditLogDownloadError("audit log download destination performed a short write")
        remaining = remaining[written:]


def _validate_max_transfer_retries(max_transfer_retries: int) -> None:
    if type(max_transfer_retries) is not int or max_transfer_retries < 0:
        raise ValueError("max_transfer_retries must be a non-negative integer")
