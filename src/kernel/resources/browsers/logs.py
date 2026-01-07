# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.browsers import log_stream_params
from ...types.shared.log_event import LogEvent

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def stream(
        self,
        id: str,
        *,
        source: Literal["path", "supervisor"],
        follow: bool | Omit = omit,
        path: str | Omit = omit,
        supervisor_process: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[LogEvent]:
        """
        Stream log files on the browser instance via SSE

        Args:
          path: only required if source is path

          supervisor_process: only required if source is supervisor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            f"/browsers/{id}/logs/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "source": source,
                        "follow": follow,
                        "path": path,
                        "supervisor_process": supervisor_process,
                    },
                    log_stream_params.LogStreamParams,
                ),
            ),
            cast_to=LogEvent,
            stream=True,
            stream_cls=Stream[LogEvent],
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    async def stream(
        self,
        id: str,
        *,
        source: Literal["path", "supervisor"],
        follow: bool | Omit = omit,
        path: str | Omit = omit,
        supervisor_process: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[LogEvent]:
        """
        Stream log files on the browser instance via SSE

        Args:
          path: only required if source is path

          supervisor_process: only required if source is supervisor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            f"/browsers/{id}/logs/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "source": source,
                        "follow": follow,
                        "path": path,
                        "supervisor_process": supervisor_process,
                    },
                    log_stream_params.LogStreamParams,
                ),
            ),
            cast_to=LogEvent,
            stream=True,
            stream_cls=AsyncStream[LogEvent],
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.stream = to_raw_response_wrapper(
            logs.stream,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.stream = async_to_raw_response_wrapper(
            logs.stream,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.stream = to_streamed_response_wrapper(
            logs.stream,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.stream = async_to_streamed_response_wrapper(
            logs.stream,
        )
