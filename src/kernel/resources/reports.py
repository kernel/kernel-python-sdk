# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime

import httpx

from ..types import report_list_params, report_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.report import Report

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    """Discover report types and submit typed reports against tasks."""

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data: Dict[str, object],
        task_id: str,
        type: str,
        occurred_at: Union[str, datetime] | Omit = omit,
        schema_version: int | Omit = omit,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Report:
        """Submit a typed report against a task.

        The data is validated against the report
        type's schema; a validation failure returns 400 with one detail per invalid
        field. A task can have at most 500 reports.

        Args:
          data: Report data. It must match the schema of the report type's version and encode to
              at most 16 KB of JSON.

          task_id: ID of the task to report against.

          type: Report type name. List report types to see the available types and their
              schemas.

          occurred_at: When the reported event happened. Defaults to the time the report is submitted.
              Must be no more than 5 minutes in the future or 30 days in the past.

          schema_version: Version of the report type's schema to validate data against. Defaults to the
              type's latest version, which the response returns.

          session_id: ID of the browser the report was observed in. It must belong to the task's
              project; deleted browsers are accepted. The browser is linked to the task if it
              is not already.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/reports",
            body=maybe_transform(
                {
                    "data": data,
                    "task_id": task_id,
                    "type": type,
                    "occurred_at": occurred_at,
                    "schema_version": schema_version,
                    "session_id": session_id,
                },
                report_create_params.ReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Report,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieve a report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/reports/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def list(
        self,
        *,
        task_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[Report]:
        """
        List a task's reports in the order they were submitted, oldest first.

        Args:
          task_id: Task whose reports to list.

          limit: Limit the number of reports to return.

          offset: Offset the number of reports to return.

          type: Only return reports of this type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/reports",
            page=SyncOffsetPagination[Report],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "task_id": task_id,
                        "limit": limit,
                        "offset": offset,
                        "type": type,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            model=Report,
        )


class AsyncReportsResource(AsyncAPIResource):
    """Discover report types and submit typed reports against tasks."""

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data: Dict[str, object],
        task_id: str,
        type: str,
        occurred_at: Union[str, datetime] | Omit = omit,
        schema_version: int | Omit = omit,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Report:
        """Submit a typed report against a task.

        The data is validated against the report
        type's schema; a validation failure returns 400 with one detail per invalid
        field. A task can have at most 500 reports.

        Args:
          data: Report data. It must match the schema of the report type's version and encode to
              at most 16 KB of JSON.

          task_id: ID of the task to report against.

          type: Report type name. List report types to see the available types and their
              schemas.

          occurred_at: When the reported event happened. Defaults to the time the report is submitted.
              Must be no more than 5 minutes in the future or 30 days in the past.

          schema_version: Version of the report type's schema to validate data against. Defaults to the
              type's latest version, which the response returns.

          session_id: ID of the browser the report was observed in. It must belong to the task's
              project; deleted browsers are accepted. The browser is linked to the task if it
              is not already.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/reports",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "task_id": task_id,
                    "type": type,
                    "occurred_at": occurred_at,
                    "schema_version": schema_version,
                    "session_id": session_id,
                },
                report_create_params.ReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Report,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieve a report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/reports/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def list(
        self,
        *,
        task_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Report, AsyncOffsetPagination[Report]]:
        """
        List a task's reports in the order they were submitted, oldest first.

        Args:
          task_id: Task whose reports to list.

          limit: Limit the number of reports to return.

          offset: Offset the number of reports to return.

          type: Only return reports of this type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/reports",
            page=AsyncOffsetPagination[Report],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "task_id": task_id,
                        "limit": limit,
                        "offset": offset,
                        "type": type,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            model=Report,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.create = to_raw_response_wrapper(
            reports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            reports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            reports.list,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.create = async_to_raw_response_wrapper(
            reports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            reports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            reports.list,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.create = to_streamed_response_wrapper(
            reports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            reports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            reports.list,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.create = async_to_streamed_response_wrapper(
            reports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            reports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            reports.list,
        )
