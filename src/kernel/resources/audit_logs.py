# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, BinaryIO
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import audit_log_list_params, audit_log_export_chunk_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..pagination import SyncPageTokenPagination, AsyncPageTokenPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.audit_log_entry import AuditLogEntry
from ..lib.audit_log_download import (
    ProgressCallback,
    AsyncProgressCallback,
    AuditLogDownloadResult,
    download_audit_logs,
    async_download_audit_logs,
)

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    """Read audit log records for the authenticated organization."""

    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end: Union[str, datetime],
        start: Union[str, datetime],
        auth_strategy: str | Omit = omit,
        exclude_method: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        method: str | Omit = omit,
        page_token: str | Omit = omit,
        search: str | Omit = omit,
        search_user_id: SequenceNotStr[str] | Omit = omit,
        service: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageTokenPagination[AuditLogEntry]:
        """API for searching audit logs.

        Limited to at most 30 day search, returns up to
        100 records per page. Not recommended for bulk export.

        Args:
          end: Upper bound (exclusive) for the audit record timestamp.

          start: Lower bound (inclusive) for the audit record timestamp.

          auth_strategy: Filter by authentication strategy.

          exclude_method: Filter out results by HTTP method.

          limit: Maximum number of results to return.

          method: Filter by HTTP method.

          page_token: Opaque page token from X-Next-Page-Token for the next page of older records.

          search: Free-text search over path, user ID, email, client IP, and status.

          search_user_id: Additional user IDs to OR into free-text search.

          service: Filter by service name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/audit-logs",
            page=SyncPageTokenPagination[AuditLogEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "auth_strategy": auth_strategy,
                        "exclude_method": exclude_method,
                        "limit": limit,
                        "method": method,
                        "page_token": page_token,
                        "search": search,
                        "search_user_id": search_user_id,
                        "service": service,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogEntry,
        )

    def export_chunk(
        self,
        *,
        end: Union[str, datetime],
        start: Union[str, datetime],
        auth_strategy: str | Omit = omit,
        cursor: str | Omit = omit,
        exclude_method: SequenceNotStr[str] | Omit = omit,
        format: Literal["jsonl", "jsonl.gz"] | Omit = omit,
        limit: int | Omit = omit,
        method: str | Omit = omit,
        search: str | Omit = omit,
        search_user_id: SequenceNotStr[str] | Omit = omit,
        service: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download an organization's audit log records for a time range as a file, for
        archival, compliance, or offline analysis. For interactive browsing, use GET
        /audit-logs.

        Args:
          end: Upper bound (exclusive) for the audit record timestamp.

          start: Lower bound (inclusive) for the audit record timestamp.

          auth_strategy: Filter by authentication strategy.

          cursor: Opaque cursor from X-Next-Cursor for the next chunk of older records.

          exclude_method: Filter out results by HTTP method.

          format: Encoding for the returned chunk.

          limit: Maximum number of records to return in this chunk.

          method: Filter by HTTP method.

          search: Free-text search over path, user ID, email, client IP, and status.

          search_user_id: Additional user IDs to OR into free-text search.

          service: Filter by service name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            "/audit-logs/export/chunk",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "auth_strategy": auth_strategy,
                        "cursor": cursor,
                        "exclude_method": exclude_method,
                        "format": format,
                        "limit": limit,
                        "method": method,
                        "search": search,
                        "search_user_id": search_user_id,
                        "service": service,
                    },
                    audit_log_export_chunk_params.AuditLogExportChunkParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def download(
        self,
        *,
        to: BinaryIO,
        end: Union[str, datetime],
        start: Union[str, datetime],
        auth_strategy: str | Omit = omit,
        exclude_method: SequenceNotStr[str] | Omit = omit,
        format: Literal["jsonl", "jsonl.gz"] | Omit = omit,
        limit: int | Omit = omit,
        method: str | Omit = omit,
        search: str | Omit = omit,
        search_user_id: SequenceNotStr[str] | Omit = omit,
        service: str | Omit = omit,
        on_progress: ProgressCallback | None = None,
        max_transfer_retries: int = 6,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditLogDownloadResult:
        """Download a complete audit log export to a writable binary destination.

        The SDK verifies every chunk and retries transient transfer failures. It
        does not close the destination. If the download fails, the destination
        may contain a partial export; use a temporary file and atomic rename
        when the completed export must be published atomically.
        """

        def fetch_chunk(cursor: str | None) -> BinaryAPIResponse:
            return self.export_chunk(
                end=end,
                start=start,
                auth_strategy=auth_strategy,
                cursor=cursor if cursor is not None else omit,
                exclude_method=exclude_method,
                format=format,
                limit=limit,
                method=method,
                search=search,
                search_user_id=search_user_id,
                service=service,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

        return download_audit_logs(
            fetch_chunk,
            to,
            on_progress=on_progress,
            max_transfer_retries=max_transfer_retries,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    """Read audit log records for the authenticated organization."""

    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end: Union[str, datetime],
        start: Union[str, datetime],
        auth_strategy: str | Omit = omit,
        exclude_method: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        method: str | Omit = omit,
        page_token: str | Omit = omit,
        search: str | Omit = omit,
        search_user_id: SequenceNotStr[str] | Omit = omit,
        service: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditLogEntry, AsyncPageTokenPagination[AuditLogEntry]]:
        """API for searching audit logs.

        Limited to at most 30 day search, returns up to
        100 records per page. Not recommended for bulk export.

        Args:
          end: Upper bound (exclusive) for the audit record timestamp.

          start: Lower bound (inclusive) for the audit record timestamp.

          auth_strategy: Filter by authentication strategy.

          exclude_method: Filter out results by HTTP method.

          limit: Maximum number of results to return.

          method: Filter by HTTP method.

          page_token: Opaque page token from X-Next-Page-Token for the next page of older records.

          search: Free-text search over path, user ID, email, client IP, and status.

          search_user_id: Additional user IDs to OR into free-text search.

          service: Filter by service name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/audit-logs",
            page=AsyncPageTokenPagination[AuditLogEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "auth_strategy": auth_strategy,
                        "exclude_method": exclude_method,
                        "limit": limit,
                        "method": method,
                        "page_token": page_token,
                        "search": search,
                        "search_user_id": search_user_id,
                        "service": service,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogEntry,
        )

    async def export_chunk(
        self,
        *,
        end: Union[str, datetime],
        start: Union[str, datetime],
        auth_strategy: str | Omit = omit,
        cursor: str | Omit = omit,
        exclude_method: SequenceNotStr[str] | Omit = omit,
        format: Literal["jsonl", "jsonl.gz"] | Omit = omit,
        limit: int | Omit = omit,
        method: str | Omit = omit,
        search: str | Omit = omit,
        search_user_id: SequenceNotStr[str] | Omit = omit,
        service: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download an organization's audit log records for a time range as a file, for
        archival, compliance, or offline analysis. For interactive browsing, use GET
        /audit-logs.

        Args:
          end: Upper bound (exclusive) for the audit record timestamp.

          start: Lower bound (inclusive) for the audit record timestamp.

          auth_strategy: Filter by authentication strategy.

          cursor: Opaque cursor from X-Next-Cursor for the next chunk of older records.

          exclude_method: Filter out results by HTTP method.

          format: Encoding for the returned chunk.

          limit: Maximum number of records to return in this chunk.

          method: Filter by HTTP method.

          search: Free-text search over path, user ID, email, client IP, and status.

          search_user_id: Additional user IDs to OR into free-text search.

          service: Filter by service name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            "/audit-logs/export/chunk",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "auth_strategy": auth_strategy,
                        "cursor": cursor,
                        "exclude_method": exclude_method,
                        "format": format,
                        "limit": limit,
                        "method": method,
                        "search": search,
                        "search_user_id": search_user_id,
                        "service": service,
                    },
                    audit_log_export_chunk_params.AuditLogExportChunkParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def download(
        self,
        *,
        to: BinaryIO,
        end: Union[str, datetime],
        start: Union[str, datetime],
        auth_strategy: str | Omit = omit,
        exclude_method: SequenceNotStr[str] | Omit = omit,
        format: Literal["jsonl", "jsonl.gz"] | Omit = omit,
        limit: int | Omit = omit,
        method: str | Omit = omit,
        search: str | Omit = omit,
        search_user_id: SequenceNotStr[str] | Omit = omit,
        service: str | Omit = omit,
        on_progress: AsyncProgressCallback | None = None,
        max_transfer_retries: int = 6,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditLogDownloadResult:
        """Download a complete audit log export to a writable binary destination.

        The SDK verifies every chunk and retries transient transfer failures. It
        does not close the destination. If the download fails, the destination
        may contain a partial export; use a temporary file and atomic rename
        when the completed export must be published atomically.
        """

        async def fetch_chunk(cursor: str | None) -> AsyncBinaryAPIResponse:
            return await self.export_chunk(
                end=end,
                start=start,
                auth_strategy=auth_strategy,
                cursor=cursor if cursor is not None else omit,
                exclude_method=exclude_method,
                format=format,
                limit=limit,
                method=method,
                search=search,
                search_user_id=search_user_id,
                service=service,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

        return await async_download_audit_logs(
            fetch_chunk,
            to,
            on_progress=on_progress,
            max_transfer_retries=max_transfer_retries,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )
        self.export_chunk = to_custom_raw_response_wrapper(
            audit_logs.export_chunk,
            BinaryAPIResponse,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )
        self.export_chunk = async_to_custom_raw_response_wrapper(
            audit_logs.export_chunk,
            AsyncBinaryAPIResponse,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )
        self.export_chunk = to_custom_streamed_response_wrapper(
            audit_logs.export_chunk,
            StreamedBinaryAPIResponse,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
        self.export_chunk = async_to_custom_streamed_response_wrapper(
            audit_logs.export_chunk,
            AsyncStreamedBinaryAPIResponse,
        )
