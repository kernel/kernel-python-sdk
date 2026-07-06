# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

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
from ...pagination import SyncOffsetPagination, AsyncOffsetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.browsers import telemetry_events_params, telemetry_stream_params
from ...types.browsers.telemetry_events_response import TelemetryEventsResponse
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

    def events(
        self,
        id: str,
        *,
        category: List[
            Literal[
                "console",
                "network",
                "page",
                "interaction",
                "control",
                "connection",
                "system",
                "screenshot",
                "captcha",
                "monitor",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: str | Omit = omit,
        since: str | Omit = omit,
        until: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[TelemetryEventsResponse]:
        """Reads a page of telemetry events for the browser session.

        To page through
        results, pass the X-Next-Offset value from the previous response as offset and
        repeat while X-Has-More is true. Returns an empty list when telemetry data is
        unavailable.

        Args:
          category: Restrict results to these event categories. Repeat the parameter for multiple
              values.

          limit: Maximum number of events per page. Defaults to 20.

          offset: Opaque pagination cursor: pass the X-Next-Offset value from the previous
              response to fetch the next page. When set, paging continues from this cursor and
              since is ignored, while until still bounds the page. It is not an event's seq
              field, so do not derive it from the response body.

          order: Read direction. asc (default) reads oldest first, starting from since or the
              offset cursor. desc reads newest first: each request returns one page of up to
              limit records ending at the offset cursor (or until, or the newest archived
              event); combining desc with since is rejected with a 400. In either direction
              the category filter applies within the page, so a filtered page may be empty
              while X-Has-More is true.

          since: Start of the window: an RFC-3339 timestamp, or a duration like 5m meaning that
              long ago. Defaults to 5m. Ignored when offset is set.

          until: End of the window (exclusive): an RFC-3339 timestamp, or a duration like 5m
              meaning that long ago.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/browsers/{id}/telemetry/events", id=id),
            page=SyncOffsetPagination[TelemetryEventsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "since": since,
                        "until": until,
                    },
                    telemetry_events_params.TelemetryEventsParams,
                ),
            ),
            model=TelemetryEventsResponse,
        )

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

    def events(
        self,
        id: str,
        *,
        category: List[
            Literal[
                "console",
                "network",
                "page",
                "interaction",
                "control",
                "connection",
                "system",
                "screenshot",
                "captcha",
                "monitor",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: str | Omit = omit,
        since: str | Omit = omit,
        until: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TelemetryEventsResponse, AsyncOffsetPagination[TelemetryEventsResponse]]:
        """Reads a page of telemetry events for the browser session.

        To page through
        results, pass the X-Next-Offset value from the previous response as offset and
        repeat while X-Has-More is true. Returns an empty list when telemetry data is
        unavailable.

        Args:
          category: Restrict results to these event categories. Repeat the parameter for multiple
              values.

          limit: Maximum number of events per page. Defaults to 20.

          offset: Opaque pagination cursor: pass the X-Next-Offset value from the previous
              response to fetch the next page. When set, paging continues from this cursor and
              since is ignored, while until still bounds the page. It is not an event's seq
              field, so do not derive it from the response body.

          order: Read direction. asc (default) reads oldest first, starting from since or the
              offset cursor. desc reads newest first: each request returns one page of up to
              limit records ending at the offset cursor (or until, or the newest archived
              event); combining desc with since is rejected with a 400. In either direction
              the category filter applies within the page, so a filtered page may be empty
              while X-Has-More is true.

          since: Start of the window: an RFC-3339 timestamp, or a duration like 5m meaning that
              long ago. Defaults to 5m. Ignored when offset is set.

          until: End of the window (exclusive): an RFC-3339 timestamp, or a duration like 5m
              meaning that long ago.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/browsers/{id}/telemetry/events", id=id),
            page=AsyncOffsetPagination[TelemetryEventsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "since": since,
                        "until": until,
                    },
                    telemetry_events_params.TelemetryEventsParams,
                ),
            ),
            model=TelemetryEventsResponse,
        )

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

        self.events = to_raw_response_wrapper(
            telemetry.events,
        )
        self.stream = to_raw_response_wrapper(
            telemetry.stream,
        )


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.events = async_to_raw_response_wrapper(
            telemetry.events,
        )
        self.stream = async_to_raw_response_wrapper(
            telemetry.stream,
        )


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.events = to_streamed_response_wrapper(
            telemetry.events,
        )
        self.stream = to_streamed_response_wrapper(
            telemetry.stream,
        )


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.events = async_to_streamed_response_wrapper(
            telemetry.events,
        )
        self.stream = async_to_streamed_response_wrapper(
            telemetry.stream,
        )
