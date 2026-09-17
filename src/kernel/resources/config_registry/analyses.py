# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
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
from ...types.config_registry import analysis_list_params
from ...types.analysis_summary import AnalysisSummary
from ...lib.config_registry_wait import (
    DEFAULT_CONFIG_REGISTRY_POLL_INTERVAL,
    poll_delay,
    poll_headers,
    analysis_finished,
    wait_timeout_error,
    validate_wait_options,
)
from ...types.config_registry_response import ConfigRegistryResponse

__all__ = ["AnalysesResource", "AsyncAnalysesResource"]


class AnalysesResource(SyncAPIResource):
    """Resolve browser and proxy recommendations for bot-protected sites."""

    @cached_property
    def with_raw_response(self) -> AnalysesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AnalysesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalysesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AnalysesResourceWithStreamingResponse(self)

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
    ) -> ConfigRegistryResponse:
        """
        Returns a project-scoped historical analysis and the recommendation outcome
        concluded by that run. Later knowledge does not change this response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/config-registry/analyses/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRegistryResponse,
        )

    def wait_for_result(
        self,
        id: str,
        *,
        poll_interval: float = DEFAULT_CONFIG_REGISTRY_POLL_INTERVAL,
        max_wait_seconds: float | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRegistryResponse:
        """Wait for an analysis to finish and return its complete result.

        The first retrieval happens immediately. ``max_wait_seconds`` is a soft
        polling deadline: an in-flight request and its normal retries may finish
        after it. Timing out does not cancel the remote analysis.
        """
        validate_wait_options(poll_interval, max_wait_seconds)
        started_at = time.monotonic()
        deadline = started_at + max_wait_seconds if max_wait_seconds is not None else None
        headers = poll_headers(extra_headers)
        polls = 0
        last_status: str | None = None

        while True:
            if polls > 0 and deadline is not None and time.monotonic() >= deadline:
                raise wait_timeout_error(id, polls, last_status, started_at)

            response = self.retrieve(
                id,
                extra_headers=headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            polls += 1
            finished, last_status = analysis_finished(response, id)
            if finished:
                return response

            delay = poll_delay(poll_interval)
            if deadline is not None:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise wait_timeout_error(id, polls, last_status, started_at)
                delay = min(delay, remaining)
            self._sleep(delay)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[AnalysisSummary]:
        """
        Lists analyses for the selected project, newest first.

        Args:
          search: Case-insensitive substring search over requested URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/config-registry/analyses",
            page=SyncOffsetPagination[AnalysisSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    analysis_list_params.AnalysisListParams,
                ),
            ),
            model=AnalysisSummary,
        )

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRegistryResponse:
        """Requests cancellation of a running project-scoped analysis.

        Cancellation is
        asynchronous; poll the analysis until its status becomes canceled. Repeating the
        request after the analysis reaches a terminal state returns the existing
        outcome.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/config-registry/analyses/{id}/cancel", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRegistryResponse,
        )


class AsyncAnalysesResource(AsyncAPIResource):
    """Resolve browser and proxy recommendations for bot-protected sites."""

    @cached_property
    def with_raw_response(self) -> AsyncAnalysesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalysesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalysesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncAnalysesResourceWithStreamingResponse(self)

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
    ) -> ConfigRegistryResponse:
        """
        Returns a project-scoped historical analysis and the recommendation outcome
        concluded by that run. Later knowledge does not change this response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/config-registry/analyses/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRegistryResponse,
        )

    async def wait_for_result(
        self,
        id: str,
        *,
        poll_interval: float = DEFAULT_CONFIG_REGISTRY_POLL_INTERVAL,
        max_wait_seconds: float | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRegistryResponse:
        """Wait for an analysis to finish and return its complete result.

        The first retrieval happens immediately. ``max_wait_seconds`` is a soft
        polling deadline: an in-flight request and its normal retries may finish
        after it. Timing out does not cancel the remote analysis. Cancelling the
        calling task stops the wait without cancelling the remote analysis.
        """
        validate_wait_options(poll_interval, max_wait_seconds)
        started_at = time.monotonic()
        deadline = started_at + max_wait_seconds if max_wait_seconds is not None else None
        headers = poll_headers(extra_headers)
        polls = 0
        last_status: str | None = None

        while True:
            if polls > 0 and deadline is not None and time.monotonic() >= deadline:
                raise wait_timeout_error(id, polls, last_status, started_at)

            response = await self.retrieve(
                id,
                extra_headers=headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            polls += 1
            finished, last_status = analysis_finished(response, id)
            if finished:
                return response

            delay = poll_delay(poll_interval)
            if deadline is not None:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise wait_timeout_error(id, polls, last_status, started_at)
                delay = min(delay, remaining)
            await self._sleep(delay)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AnalysisSummary, AsyncOffsetPagination[AnalysisSummary]]:
        """
        Lists analyses for the selected project, newest first.

        Args:
          search: Case-insensitive substring search over requested URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/config-registry/analyses",
            page=AsyncOffsetPagination[AnalysisSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    analysis_list_params.AnalysisListParams,
                ),
            ),
            model=AnalysisSummary,
        )

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRegistryResponse:
        """Requests cancellation of a running project-scoped analysis.

        Cancellation is
        asynchronous; poll the analysis until its status becomes canceled. Repeating the
        request after the analysis reaches a terminal state returns the existing
        outcome.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/config-registry/analyses/{id}/cancel", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRegistryResponse,
        )


class AnalysesResourceWithRawResponse:
    def __init__(self, analyses: AnalysesResource) -> None:
        self._analyses = analyses

        self.retrieve = to_raw_response_wrapper(
            analyses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            analyses.list,
        )
        self.cancel = to_raw_response_wrapper(
            analyses.cancel,
        )


class AsyncAnalysesResourceWithRawResponse:
    def __init__(self, analyses: AsyncAnalysesResource) -> None:
        self._analyses = analyses

        self.retrieve = async_to_raw_response_wrapper(
            analyses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            analyses.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            analyses.cancel,
        )


class AnalysesResourceWithStreamingResponse:
    def __init__(self, analyses: AnalysesResource) -> None:
        self._analyses = analyses

        self.retrieve = to_streamed_response_wrapper(
            analyses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            analyses.list,
        )
        self.cancel = to_streamed_response_wrapper(
            analyses.cancel,
        )


class AsyncAnalysesResourceWithStreamingResponse:
    def __init__(self, analyses: AsyncAnalysesResource) -> None:
        self._analyses = analyses

        self.retrieve = async_to_streamed_response_wrapper(
            analyses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            analyses.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            analyses.cancel,
        )
