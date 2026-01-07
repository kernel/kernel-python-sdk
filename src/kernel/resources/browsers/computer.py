# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.browsers import (
    computer_scroll_params,
    computer_press_key_params,
    computer_type_text_params,
    computer_drag_mouse_params,
    computer_move_mouse_params,
    computer_click_mouse_params,
    computer_capture_screenshot_params,
    computer_set_cursor_visibility_params,
)
from ...types.browsers.computer_set_cursor_visibility_response import ComputerSetCursorVisibilityResponse

__all__ = ["ComputerResource", "AsyncComputerResource"]


class ComputerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ComputerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ComputerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComputerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ComputerResourceWithStreamingResponse(self)

    def capture_screenshot(
        self,
        id: str,
        *,
        region: computer_capture_screenshot_params.Region | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Capture a screenshot of the browser instance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return self._post(
            f"/browsers/{id}/computer/screenshot",
            body=maybe_transform(
                {"region": region}, computer_capture_screenshot_params.ComputerCaptureScreenshotParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def click_mouse(
        self,
        id: str,
        *,
        x: int,
        y: int,
        button: Literal["left", "right", "middle", "back", "forward"] | Omit = omit,
        click_type: Literal["down", "up", "click"] | Omit = omit,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        num_clicks: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Simulate a mouse click action on the browser instance

        Args:
          x: X coordinate of the click position

          y: Y coordinate of the click position

          button: Mouse button to interact with

          click_type: Type of click action

          hold_keys: Modifier keys to hold during the click

          num_clicks: Number of times to repeat the click

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/browsers/{id}/computer/click_mouse",
            body=maybe_transform(
                {
                    "x": x,
                    "y": y,
                    "button": button,
                    "click_type": click_type,
                    "hold_keys": hold_keys,
                    "num_clicks": num_clicks,
                },
                computer_click_mouse_params.ComputerClickMouseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def drag_mouse(
        self,
        id: str,
        *,
        path: Iterable[Iterable[int]],
        button: Literal["left", "middle", "right"] | Omit = omit,
        delay: int | Omit = omit,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        step_delay_ms: int | Omit = omit,
        steps_per_segment: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Drag the mouse along a path

        Args:
          path: Ordered list of [x, y] coordinate pairs to move through while dragging. Must
              contain at least 2 points.

          button: Mouse button to drag with

          delay: Delay in milliseconds between button down and starting to move along the path.

          hold_keys: Modifier keys to hold during the drag

          step_delay_ms: Delay in milliseconds between relative steps while dragging (not the initial
              delay).

          steps_per_segment: Number of relative move steps per segment in the path. Minimum 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/browsers/{id}/computer/drag_mouse",
            body=maybe_transform(
                {
                    "path": path,
                    "button": button,
                    "delay": delay,
                    "hold_keys": hold_keys,
                    "step_delay_ms": step_delay_ms,
                    "steps_per_segment": steps_per_segment,
                },
                computer_drag_mouse_params.ComputerDragMouseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def move_mouse(
        self,
        id: str,
        *,
        x: int,
        y: int,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move the mouse cursor to the specified coordinates on the browser instance

        Args:
          x: X coordinate to move the cursor to

          y: Y coordinate to move the cursor to

          hold_keys: Modifier keys to hold during the move

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/browsers/{id}/computer/move_mouse",
            body=maybe_transform(
                {
                    "x": x,
                    "y": y,
                    "hold_keys": hold_keys,
                },
                computer_move_mouse_params.ComputerMoveMouseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def press_key(
        self,
        id: str,
        *,
        keys: SequenceNotStr[str],
        duration: int | Omit = omit,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Press one or more keys on the host computer

        Args:
          keys: List of key symbols to press. Each item should be a key symbol supported by
              xdotool (see X11 keysym definitions). Examples include "Return", "Shift",
              "Ctrl", "Alt", "F5". Items in this list could also be combinations, e.g.
              "Ctrl+t" or "Ctrl+Shift+Tab".

          duration: Duration to hold the keys down in milliseconds. If omitted or 0, keys are
              tapped.

          hold_keys: Optional modifier keys to hold during the key press sequence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/browsers/{id}/computer/press_key",
            body=maybe_transform(
                {
                    "keys": keys,
                    "duration": duration,
                    "hold_keys": hold_keys,
                },
                computer_press_key_params.ComputerPressKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def scroll(
        self,
        id: str,
        *,
        x: int,
        y: int,
        delta_x: int | Omit = omit,
        delta_y: int | Omit = omit,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Scroll the mouse wheel at a position on the host computer

        Args:
          x: X coordinate at which to perform the scroll

          y: Y coordinate at which to perform the scroll

          delta_x: Horizontal scroll amount. Positive scrolls right, negative scrolls left.

          delta_y: Vertical scroll amount. Positive scrolls down, negative scrolls up.

          hold_keys: Modifier keys to hold during the scroll

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/browsers/{id}/computer/scroll",
            body=maybe_transform(
                {
                    "x": x,
                    "y": y,
                    "delta_x": delta_x,
                    "delta_y": delta_y,
                    "hold_keys": hold_keys,
                },
                computer_scroll_params.ComputerScrollParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set_cursor_visibility(
        self,
        id: str,
        *,
        hidden: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComputerSetCursorVisibilityResponse:
        """
        Set cursor visibility

        Args:
          hidden: Whether the cursor should be hidden or visible

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/browsers/{id}/computer/cursor",
            body=maybe_transform(
                {"hidden": hidden}, computer_set_cursor_visibility_params.ComputerSetCursorVisibilityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComputerSetCursorVisibilityResponse,
        )

    def type_text(
        self,
        id: str,
        *,
        text: str,
        delay: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Type text on the browser instance

        Args:
          text: Text to type on the browser instance

          delay: Delay in milliseconds between keystrokes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/browsers/{id}/computer/type",
            body=maybe_transform(
                {
                    "text": text,
                    "delay": delay,
                },
                computer_type_text_params.ComputerTypeTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncComputerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncComputerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncComputerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComputerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncComputerResourceWithStreamingResponse(self)

    async def capture_screenshot(
        self,
        id: str,
        *,
        region: computer_capture_screenshot_params.Region | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Capture a screenshot of the browser instance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return await self._post(
            f"/browsers/{id}/computer/screenshot",
            body=await async_maybe_transform(
                {"region": region}, computer_capture_screenshot_params.ComputerCaptureScreenshotParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def click_mouse(
        self,
        id: str,
        *,
        x: int,
        y: int,
        button: Literal["left", "right", "middle", "back", "forward"] | Omit = omit,
        click_type: Literal["down", "up", "click"] | Omit = omit,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        num_clicks: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Simulate a mouse click action on the browser instance

        Args:
          x: X coordinate of the click position

          y: Y coordinate of the click position

          button: Mouse button to interact with

          click_type: Type of click action

          hold_keys: Modifier keys to hold during the click

          num_clicks: Number of times to repeat the click

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/browsers/{id}/computer/click_mouse",
            body=await async_maybe_transform(
                {
                    "x": x,
                    "y": y,
                    "button": button,
                    "click_type": click_type,
                    "hold_keys": hold_keys,
                    "num_clicks": num_clicks,
                },
                computer_click_mouse_params.ComputerClickMouseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def drag_mouse(
        self,
        id: str,
        *,
        path: Iterable[Iterable[int]],
        button: Literal["left", "middle", "right"] | Omit = omit,
        delay: int | Omit = omit,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        step_delay_ms: int | Omit = omit,
        steps_per_segment: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Drag the mouse along a path

        Args:
          path: Ordered list of [x, y] coordinate pairs to move through while dragging. Must
              contain at least 2 points.

          button: Mouse button to drag with

          delay: Delay in milliseconds between button down and starting to move along the path.

          hold_keys: Modifier keys to hold during the drag

          step_delay_ms: Delay in milliseconds between relative steps while dragging (not the initial
              delay).

          steps_per_segment: Number of relative move steps per segment in the path. Minimum 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/browsers/{id}/computer/drag_mouse",
            body=await async_maybe_transform(
                {
                    "path": path,
                    "button": button,
                    "delay": delay,
                    "hold_keys": hold_keys,
                    "step_delay_ms": step_delay_ms,
                    "steps_per_segment": steps_per_segment,
                },
                computer_drag_mouse_params.ComputerDragMouseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def move_mouse(
        self,
        id: str,
        *,
        x: int,
        y: int,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move the mouse cursor to the specified coordinates on the browser instance

        Args:
          x: X coordinate to move the cursor to

          y: Y coordinate to move the cursor to

          hold_keys: Modifier keys to hold during the move

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/browsers/{id}/computer/move_mouse",
            body=await async_maybe_transform(
                {
                    "x": x,
                    "y": y,
                    "hold_keys": hold_keys,
                },
                computer_move_mouse_params.ComputerMoveMouseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def press_key(
        self,
        id: str,
        *,
        keys: SequenceNotStr[str],
        duration: int | Omit = omit,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Press one or more keys on the host computer

        Args:
          keys: List of key symbols to press. Each item should be a key symbol supported by
              xdotool (see X11 keysym definitions). Examples include "Return", "Shift",
              "Ctrl", "Alt", "F5". Items in this list could also be combinations, e.g.
              "Ctrl+t" or "Ctrl+Shift+Tab".

          duration: Duration to hold the keys down in milliseconds. If omitted or 0, keys are
              tapped.

          hold_keys: Optional modifier keys to hold during the key press sequence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/browsers/{id}/computer/press_key",
            body=await async_maybe_transform(
                {
                    "keys": keys,
                    "duration": duration,
                    "hold_keys": hold_keys,
                },
                computer_press_key_params.ComputerPressKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def scroll(
        self,
        id: str,
        *,
        x: int,
        y: int,
        delta_x: int | Omit = omit,
        delta_y: int | Omit = omit,
        hold_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Scroll the mouse wheel at a position on the host computer

        Args:
          x: X coordinate at which to perform the scroll

          y: Y coordinate at which to perform the scroll

          delta_x: Horizontal scroll amount. Positive scrolls right, negative scrolls left.

          delta_y: Vertical scroll amount. Positive scrolls down, negative scrolls up.

          hold_keys: Modifier keys to hold during the scroll

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/browsers/{id}/computer/scroll",
            body=await async_maybe_transform(
                {
                    "x": x,
                    "y": y,
                    "delta_x": delta_x,
                    "delta_y": delta_y,
                    "hold_keys": hold_keys,
                },
                computer_scroll_params.ComputerScrollParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set_cursor_visibility(
        self,
        id: str,
        *,
        hidden: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComputerSetCursorVisibilityResponse:
        """
        Set cursor visibility

        Args:
          hidden: Whether the cursor should be hidden or visible

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/browsers/{id}/computer/cursor",
            body=await async_maybe_transform(
                {"hidden": hidden}, computer_set_cursor_visibility_params.ComputerSetCursorVisibilityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComputerSetCursorVisibilityResponse,
        )

    async def type_text(
        self,
        id: str,
        *,
        text: str,
        delay: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Type text on the browser instance

        Args:
          text: Text to type on the browser instance

          delay: Delay in milliseconds between keystrokes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/browsers/{id}/computer/type",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "delay": delay,
                },
                computer_type_text_params.ComputerTypeTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ComputerResourceWithRawResponse:
    def __init__(self, computer: ComputerResource) -> None:
        self._computer = computer

        self.capture_screenshot = to_custom_raw_response_wrapper(
            computer.capture_screenshot,
            BinaryAPIResponse,
        )
        self.click_mouse = to_raw_response_wrapper(
            computer.click_mouse,
        )
        self.drag_mouse = to_raw_response_wrapper(
            computer.drag_mouse,
        )
        self.move_mouse = to_raw_response_wrapper(
            computer.move_mouse,
        )
        self.press_key = to_raw_response_wrapper(
            computer.press_key,
        )
        self.scroll = to_raw_response_wrapper(
            computer.scroll,
        )
        self.set_cursor_visibility = to_raw_response_wrapper(
            computer.set_cursor_visibility,
        )
        self.type_text = to_raw_response_wrapper(
            computer.type_text,
        )


class AsyncComputerResourceWithRawResponse:
    def __init__(self, computer: AsyncComputerResource) -> None:
        self._computer = computer

        self.capture_screenshot = async_to_custom_raw_response_wrapper(
            computer.capture_screenshot,
            AsyncBinaryAPIResponse,
        )
        self.click_mouse = async_to_raw_response_wrapper(
            computer.click_mouse,
        )
        self.drag_mouse = async_to_raw_response_wrapper(
            computer.drag_mouse,
        )
        self.move_mouse = async_to_raw_response_wrapper(
            computer.move_mouse,
        )
        self.press_key = async_to_raw_response_wrapper(
            computer.press_key,
        )
        self.scroll = async_to_raw_response_wrapper(
            computer.scroll,
        )
        self.set_cursor_visibility = async_to_raw_response_wrapper(
            computer.set_cursor_visibility,
        )
        self.type_text = async_to_raw_response_wrapper(
            computer.type_text,
        )


class ComputerResourceWithStreamingResponse:
    def __init__(self, computer: ComputerResource) -> None:
        self._computer = computer

        self.capture_screenshot = to_custom_streamed_response_wrapper(
            computer.capture_screenshot,
            StreamedBinaryAPIResponse,
        )
        self.click_mouse = to_streamed_response_wrapper(
            computer.click_mouse,
        )
        self.drag_mouse = to_streamed_response_wrapper(
            computer.drag_mouse,
        )
        self.move_mouse = to_streamed_response_wrapper(
            computer.move_mouse,
        )
        self.press_key = to_streamed_response_wrapper(
            computer.press_key,
        )
        self.scroll = to_streamed_response_wrapper(
            computer.scroll,
        )
        self.set_cursor_visibility = to_streamed_response_wrapper(
            computer.set_cursor_visibility,
        )
        self.type_text = to_streamed_response_wrapper(
            computer.type_text,
        )


class AsyncComputerResourceWithStreamingResponse:
    def __init__(self, computer: AsyncComputerResource) -> None:
        self._computer = computer

        self.capture_screenshot = async_to_custom_streamed_response_wrapper(
            computer.capture_screenshot,
            AsyncStreamedBinaryAPIResponse,
        )
        self.click_mouse = async_to_streamed_response_wrapper(
            computer.click_mouse,
        )
        self.drag_mouse = async_to_streamed_response_wrapper(
            computer.drag_mouse,
        )
        self.move_mouse = async_to_streamed_response_wrapper(
            computer.move_mouse,
        )
        self.press_key = async_to_streamed_response_wrapper(
            computer.press_key,
        )
        self.scroll = async_to_streamed_response_wrapper(
            computer.scroll,
        )
        self.set_cursor_visibility = async_to_streamed_response_wrapper(
            computer.set_cursor_visibility,
        )
        self.type_text = async_to_streamed_response_wrapper(
            computer.type_text,
        )
