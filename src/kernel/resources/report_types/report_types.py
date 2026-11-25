# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import report_type_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPagination, AsyncOffsetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.report_type import ReportType
from ...types.report_type_summary import ReportTypeSummary

__all__ = ["ReportTypesResource", "AsyncReportTypesResource"]


class ReportTypesResource(SyncAPIResource):
    """Discover report types and submit typed reports against tasks."""

    @cached_property
    def versions(self) -> VersionsResource:
        """Discover report types and submit typed reports against tasks."""
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReportTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ReportTypesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportType:
        """
        Retrieve a report type, its versions, and the JSON Schema of its latest version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return self._get(
            path_template("/report_types/{type}", type=type),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportType,
        )

    def list(
        self,
        *,
        task_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ReportTypeSummary]:
        """List the report types agents can submit for a task.

        Retrieve a type for the JSON
        Schema of its data.

        Args:
          task_id: Task the agent is finding a report type for.

          limit: Limit the number of report types to return.

          offset: Offset the number of report types to return.

          query: What the agent wants to report, in its own words. Types are ranked by how
              closely their meaning matches, most relevant first; they need not share any
              words. Only this text affects the ranking, not the task. Without it, or if
              ranking is unavailable, types are listed by name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/report_types",
            page=SyncOffsetPagination[ReportTypeSummary],
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
                        "query": query,
                    },
                    report_type_list_params.ReportTypeListParams,
                ),
            ),
            model=ReportTypeSummary,
        )


class AsyncReportTypesResource(AsyncAPIResource):
    """Discover report types and submit typed reports against tasks."""

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """Discover report types and submit typed reports against tasks."""
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReportTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncReportTypesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportType:
        """
        Retrieve a report type, its versions, and the JSON Schema of its latest version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return await self._get(
            path_template("/report_types/{type}", type=type),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportType,
        )

    def list(
        self,
        *,
        task_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ReportTypeSummary, AsyncOffsetPagination[ReportTypeSummary]]:
        """List the report types agents can submit for a task.

        Retrieve a type for the JSON
        Schema of its data.

        Args:
          task_id: Task the agent is finding a report type for.

          limit: Limit the number of report types to return.

          offset: Offset the number of report types to return.

          query: What the agent wants to report, in its own words. Types are ranked by how
              closely their meaning matches, most relevant first; they need not share any
              words. Only this text affects the ranking, not the task. Without it, or if
              ranking is unavailable, types are listed by name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/report_types",
            page=AsyncOffsetPagination[ReportTypeSummary],
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
                        "query": query,
                    },
                    report_type_list_params.ReportTypeListParams,
                ),
            ),
            model=ReportTypeSummary,
        )


class ReportTypesResourceWithRawResponse:
    def __init__(self, report_types: ReportTypesResource) -> None:
        self._report_types = report_types

        self.retrieve = to_raw_response_wrapper(
            report_types.retrieve,
        )
        self.list = to_raw_response_wrapper(
            report_types.list,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """Discover report types and submit typed reports against tasks."""
        return VersionsResourceWithRawResponse(self._report_types.versions)


class AsyncReportTypesResourceWithRawResponse:
    def __init__(self, report_types: AsyncReportTypesResource) -> None:
        self._report_types = report_types

        self.retrieve = async_to_raw_response_wrapper(
            report_types.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            report_types.list,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """Discover report types and submit typed reports against tasks."""
        return AsyncVersionsResourceWithRawResponse(self._report_types.versions)


class ReportTypesResourceWithStreamingResponse:
    def __init__(self, report_types: ReportTypesResource) -> None:
        self._report_types = report_types

        self.retrieve = to_streamed_response_wrapper(
            report_types.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            report_types.list,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """Discover report types and submit typed reports against tasks."""
        return VersionsResourceWithStreamingResponse(self._report_types.versions)


class AsyncReportTypesResourceWithStreamingResponse:
    def __init__(self, report_types: AsyncReportTypesResource) -> None:
        self._report_types = report_types

        self.retrieve = async_to_streamed_response_wrapper(
            report_types.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            report_types.list,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """Discover report types and submit typed reports against tasks."""
        return AsyncVersionsResourceWithStreamingResponse(self._report_types.versions)
