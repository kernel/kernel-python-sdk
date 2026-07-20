from __future__ import annotations

import time
import hashlib
from typing import BinaryIO, Callable, Optional, Protocol, Awaitable
from dataclasses import dataclass

import anyio
import httpx

from .._exceptions import KernelError, APIStatusError

_DOWNLOAD_ATTEMPTS = 7
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


SyncFetchChunk = Callable[[Optional[str]], _SyncChunkResponse]
AsyncFetchChunk = Callable[[Optional[str]], Awaitable[_AsyncChunkResponse]]
ProgressCallback = Callable[[AuditLogDownloadProgress], None]


def download_audit_logs(
    fetch_chunk: SyncFetchChunk,
    destination: BinaryIO,
    *,
    on_progress: ProgressCallback | None = None,
) -> AuditLogDownloadResult:
    if not callable(getattr(destination, "write", None)):
        raise TypeError("audit log download destination must provide write()")

    cursor: str | None = None
    result = AuditLogDownloadResult(bytes_written=0, chunks=0, rows=0)
    while True:
        body, headers = _fetch_verified_chunk(fetch_chunk, cursor)
        chunk_rows, next_cursor, has_more = _parse_chunk_headers(headers, cursor)
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
    on_progress: ProgressCallback | None = None,
) -> AuditLogDownloadResult:
    if not callable(getattr(destination, "write", None)):
        raise TypeError("audit log download destination must provide write()")

    cursor: str | None = None
    result = AuditLogDownloadResult(bytes_written=0, chunks=0, rows=0)
    while True:
        body, headers = await _async_fetch_verified_chunk(fetch_chunk, cursor)
        chunk_rows, next_cursor, has_more = _parse_chunk_headers(headers, cursor)
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


def _fetch_verified_chunk(fetch_chunk: SyncFetchChunk, cursor: str | None) -> tuple[bytes, httpx.Headers]:
    for attempt in range(1, _DOWNLOAD_ATTEMPTS + 1):
        try:
            response = fetch_chunk(cursor)
            try:
                body = response.read()
                headers = httpx.Headers(response.headers)
            finally:
                response.close()
            _verify_checksum(body, headers)
            return body, headers
        except Exception as error:
            if attempt == _DOWNLOAD_ATTEMPTS or not _is_retryable(error):
                raise
            time.sleep(min(2 ** (attempt - 1), _MAX_RETRY_DELAY))
    raise AssertionError("unreachable")


async def _async_fetch_verified_chunk(fetch_chunk: AsyncFetchChunk, cursor: str | None) -> tuple[bytes, httpx.Headers]:
    for attempt in range(1, _DOWNLOAD_ATTEMPTS + 1):
        try:
            response = await fetch_chunk(cursor)
            try:
                body = await response.read()
                headers = httpx.Headers(response.headers)
            finally:
                await response.close()
            _verify_checksum(body, headers)
            return body, headers
        except Exception as error:
            if attempt == _DOWNLOAD_ATTEMPTS or not _is_retryable(error):
                raise
            await anyio.sleep(min(2 ** (attempt - 1), _MAX_RETRY_DELAY))
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
    try:
        rows = int(row_count) if row_count is not None else -1
    except ValueError as error:
        raise AuditLogDownloadError("response missing or invalid X-Row-Count header") from error
    if rows < 0:
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
        if written <= 0 or written > len(remaining):
            raise AuditLogDownloadError("audit log download destination performed a short write")
        remaining = remaining[written:]


def _is_retryable(error: Exception) -> bool:
    if isinstance(error, APIStatusError):
        return error.status_code == 429 or error.status_code >= 500
    return True
