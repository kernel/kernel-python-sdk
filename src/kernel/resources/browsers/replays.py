# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ..._base_client import make_request_options
from ...types.browsers import replay_start_params
from ...types.browsers.replay_list_response import ReplayListResponse
from ...types.browsers.replay_start_response import ReplayStartResponse

__all__ = ["ReplaysResource", "AsyncReplaysResource"]


class ReplaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReplaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReplaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReplaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ReplaysResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplayListResponse:
        """
        List all replays for the specified browser session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/browsers/{id}/replays",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplayListResponse,
        )

    def download(
        self,
        replay_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download or stream the specified replay recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not replay_id:
            raise ValueError(f"Expected a non-empty value for `replay_id` but received {replay_id!r}")
        extra_headers = {"Accept": "video/mp4", **(extra_headers or {})}
        return self._get(
            f"/browsers/{id}/replays/{replay_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def start(
        self,
        id: str,
        *,
        framerate: int | Omit = omit,
        max_duration_in_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplayStartResponse:
        """
        Start recording the browser session and return a replay ID.

        Args:
          framerate: Recording framerate in fps.

          max_duration_in_seconds: Maximum recording duration in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/browsers/{id}/replays",
            body=maybe_transform(
                {
                    "framerate": framerate,
                    "max_duration_in_seconds": max_duration_in_seconds,
                },
                replay_start_params.ReplayStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplayStartResponse,
        )

    def stop(
        self,
        replay_id: str,
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
        Stop the specified replay recording and persist the video.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not replay_id:
            raise ValueError(f"Expected a non-empty value for `replay_id` but received {replay_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/browsers/{id}/replays/{replay_id}/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncReplaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReplaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReplaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReplaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncReplaysResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplayListResponse:
        """
        List all replays for the specified browser session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/browsers/{id}/replays",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplayListResponse,
        )

    async def download(
        self,
        replay_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download or stream the specified replay recording.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not replay_id:
            raise ValueError(f"Expected a non-empty value for `replay_id` but received {replay_id!r}")
        extra_headers = {"Accept": "video/mp4", **(extra_headers or {})}
        return await self._get(
            f"/browsers/{id}/replays/{replay_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def start(
        self,
        id: str,
        *,
        framerate: int | Omit = omit,
        max_duration_in_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplayStartResponse:
        """
        Start recording the browser session and return a replay ID.

        Args:
          framerate: Recording framerate in fps.

          max_duration_in_seconds: Maximum recording duration in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/browsers/{id}/replays",
            body=await async_maybe_transform(
                {
                    "framerate": framerate,
                    "max_duration_in_seconds": max_duration_in_seconds,
                },
                replay_start_params.ReplayStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplayStartResponse,
        )

    async def stop(
        self,
        replay_id: str,
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
        Stop the specified replay recording and persist the video.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not replay_id:
            raise ValueError(f"Expected a non-empty value for `replay_id` but received {replay_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/browsers/{id}/replays/{replay_id}/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ReplaysResourceWithRawResponse:
    def __init__(self, replays: ReplaysResource) -> None:
        self._replays = replays

        self.list = to_raw_response_wrapper(
            replays.list,
        )
        self.download = to_custom_raw_response_wrapper(
            replays.download,
            BinaryAPIResponse,
        )
        self.start = to_raw_response_wrapper(
            replays.start,
        )
        self.stop = to_raw_response_wrapper(
            replays.stop,
        )


class AsyncReplaysResourceWithRawResponse:
    def __init__(self, replays: AsyncReplaysResource) -> None:
        self._replays = replays

        self.list = async_to_raw_response_wrapper(
            replays.list,
        )
        self.download = async_to_custom_raw_response_wrapper(
            replays.download,
            AsyncBinaryAPIResponse,
        )
        self.start = async_to_raw_response_wrapper(
            replays.start,
        )
        self.stop = async_to_raw_response_wrapper(
            replays.stop,
        )


class ReplaysResourceWithStreamingResponse:
    def __init__(self, replays: ReplaysResource) -> None:
        self._replays = replays

        self.list = to_streamed_response_wrapper(
            replays.list,
        )
        self.download = to_custom_streamed_response_wrapper(
            replays.download,
            StreamedBinaryAPIResponse,
        )
        self.start = to_streamed_response_wrapper(
            replays.start,
        )
        self.stop = to_streamed_response_wrapper(
            replays.stop,
        )


class AsyncReplaysResourceWithStreamingResponse:
    def __init__(self, replays: AsyncReplaysResource) -> None:
        self._replays = replays

        self.list = async_to_streamed_response_wrapper(
            replays.list,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            replays.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.start = async_to_streamed_response_wrapper(
            replays.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            replays.stop,
        )
