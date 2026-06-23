# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ...types.browsers import telemetry_stream_params
from ...types.browsers.telemetry_stream_response import TelemetryStreamResponse

__all__ = ["TelemetryResource", "AsyncTelemetryResource"]


class TelemetryResource(SyncAPIResource):
    """Stream live telemetry events from a browser session."""

    @cached_property
    def with_raw_response(self) -> TelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return TelemetryResourceWithStreamingResponse(self)

    def stream(
        self,
        id: str,
        *,
        replay: str | Omit = omit,
        last_event_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[TelemetryStreamResponse]:
        """Streams browser telemetry events as a server-sent events (SSE) stream.

        The
        stream closes when the browser session terminates. Each event frame includes an
        id: field containing a monotonically increasing sequence number; pass it as
        Last-Event-ID on reconnect to resume without gaps. The event: field is never
        set; all frames carry JSON in the data: field. A keepalive comment frame is sent
        every 15 seconds when no events arrive. Returns 404 if the browser session does
        not exist. If telemetry was not enabled on the session, the stream opens but no
        events are delivered. Fresh connections only see new events; pass replay=all to
        start from the oldest retained event instead.

        Args:
          replay: Pass `all` to start from the oldest retained event instead of only new events;
              any other value is treated as from-now. The buffer is bounded, so the first
              event id may be greater than 1 if older events were evicted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Last-Event-ID": last_event_id}), **(extra_headers or {})}
        return self._get(
            path_template("/browsers/{id}/telemetry/stream", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"replay": replay}, telemetry_stream_params.TelemetryStreamParams),
            ),
            cast_to=TelemetryStreamResponse,
            stream=True,
            stream_cls=Stream[TelemetryStreamResponse],
        )


class AsyncTelemetryResource(AsyncAPIResource):
    """Stream live telemetry events from a browser session."""

    @cached_property
    def with_raw_response(self) -> AsyncTelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncTelemetryResourceWithStreamingResponse(self)

    async def stream(
        self,
        id: str,
        *,
        replay: str | Omit = omit,
        last_event_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[TelemetryStreamResponse]:
        """Streams browser telemetry events as a server-sent events (SSE) stream.

        The
        stream closes when the browser session terminates. Each event frame includes an
        id: field containing a monotonically increasing sequence number; pass it as
        Last-Event-ID on reconnect to resume without gaps. The event: field is never
        set; all frames carry JSON in the data: field. A keepalive comment frame is sent
        every 15 seconds when no events arrive. Returns 404 if the browser session does
        not exist. If telemetry was not enabled on the session, the stream opens but no
        events are delivered. Fresh connections only see new events; pass replay=all to
        start from the oldest retained event instead.

        Args:
          replay: Pass `all` to start from the oldest retained event instead of only new events;
              any other value is treated as from-now. The buffer is bounded, so the first
              event id may be greater than 1 if older events were evicted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Last-Event-ID": last_event_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/browsers/{id}/telemetry/stream", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"replay": replay}, telemetry_stream_params.TelemetryStreamParams),
            ),
            cast_to=TelemetryStreamResponse,
            stream=True,
            stream_cls=AsyncStream[TelemetryStreamResponse],
        )


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.stream = to_raw_response_wrapper(
            telemetry.stream,
        )


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.stream = async_to_raw_response_wrapper(
            telemetry.stream,
        )


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.stream = to_streamed_response_wrapper(
            telemetry.stream,
        )


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.stream = async_to_streamed_response_wrapper(
            telemetry.stream,
        )
