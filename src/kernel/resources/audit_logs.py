# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import audit_log_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPageTokenPagination, AsyncPageTokenPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.audit_log_entry import AuditLogEntry

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
        exclude_method: str | Omit = omit,
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
        exclude_method: str | Omit = omit,
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


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
