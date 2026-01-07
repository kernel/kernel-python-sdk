# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._streaming import Stream, AsyncStream
from ...._base_client import make_request_options
from ....types.browsers.fs import watch_start_params
from ....types.browsers.fs.watch_start_response import WatchStartResponse
from ....types.browsers.fs.watch_events_response import WatchEventsResponse

__all__ = ["WatchResource", "AsyncWatchResource"]


class WatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return WatchResourceWithStreamingResponse(self)

    def events(
        self,
        watch_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[WatchEventsResponse]:
        """
        Stream filesystem events for a watch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not watch_id:
            raise ValueError(f"Expected a non-empty value for `watch_id` but received {watch_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            f"/browsers/{id}/fs/watch/{watch_id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchEventsResponse,
            stream=True,
            stream_cls=Stream[WatchEventsResponse],
        )

    def start(
        self,
        id: str,
        *,
        path: str,
        recursive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchStartResponse:
        """
        Watch a directory for changes

        Args:
          path: Directory to watch.

          recursive: Whether to watch recursively.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/browsers/{id}/fs/watch",
            body=maybe_transform(
                {
                    "path": path,
                    "recursive": recursive,
                },
                watch_start_params.WatchStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchStartResponse,
        )

    def stop(
        self,
        watch_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stop watching a directory

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not watch_id:
            raise ValueError(f"Expected a non-empty value for `watch_id` but received {watch_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/browsers/{id}/fs/watch/{watch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncWatchResourceWithStreamingResponse(self)

    async def events(
        self,
        watch_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[WatchEventsResponse]:
        """
        Stream filesystem events for a watch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not watch_id:
            raise ValueError(f"Expected a non-empty value for `watch_id` but received {watch_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            f"/browsers/{id}/fs/watch/{watch_id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchEventsResponse,
            stream=True,
            stream_cls=AsyncStream[WatchEventsResponse],
        )

    async def start(
        self,
        id: str,
        *,
        path: str,
        recursive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchStartResponse:
        """
        Watch a directory for changes

        Args:
          path: Directory to watch.

          recursive: Whether to watch recursively.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/browsers/{id}/fs/watch",
            body=await async_maybe_transform(
                {
                    "path": path,
                    "recursive": recursive,
                },
                watch_start_params.WatchStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchStartResponse,
        )

    async def stop(
        self,
        watch_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stop watching a directory

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not watch_id:
            raise ValueError(f"Expected a non-empty value for `watch_id` but received {watch_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/browsers/{id}/fs/watch/{watch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WatchResourceWithRawResponse:
    def __init__(self, watch: WatchResource) -> None:
        self._watch = watch

        self.events = to_raw_response_wrapper(
            watch.events,
        )
        self.start = to_raw_response_wrapper(
            watch.start,
        )
        self.stop = to_raw_response_wrapper(
            watch.stop,
        )


class AsyncWatchResourceWithRawResponse:
    def __init__(self, watch: AsyncWatchResource) -> None:
        self._watch = watch

        self.events = async_to_raw_response_wrapper(
            watch.events,
        )
        self.start = async_to_raw_response_wrapper(
            watch.start,
        )
        self.stop = async_to_raw_response_wrapper(
            watch.stop,
        )


class WatchResourceWithStreamingResponse:
    def __init__(self, watch: WatchResource) -> None:
        self._watch = watch

        self.events = to_streamed_response_wrapper(
            watch.events,
        )
        self.start = to_streamed_response_wrapper(
            watch.start,
        )
        self.stop = to_streamed_response_wrapper(
            watch.stop,
        )


class AsyncWatchResourceWithStreamingResponse:
    def __init__(self, watch: AsyncWatchResource) -> None:
        self._watch = watch

        self.events = async_to_streamed_response_wrapper(
            watch.events,
        )
        self.start = async_to_streamed_response_wrapper(
            watch.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            watch.stop,
        )
