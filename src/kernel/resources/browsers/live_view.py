# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.browsers import BrowserLiveViewScope, live_view_create_params
from ...types.browsers.browser_live_view import BrowserLiveView
from ...types.browsers.browser_live_view_scope import BrowserLiveViewScope

__all__ = ["LiveViewResource", "AsyncLiveViewResource"]


class LiveViewResource(SyncAPIResource):
    """Create and manage browser sessions."""

    @cached_property
    def with_raw_response(self) -> LiveViewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LiveViewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveViewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return LiveViewResourceWithStreamingResponse(self)

    def create(
        self,
        id_or_name: str,
        *,
        scope: BrowserLiveViewScope | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BrowserLiveView:
        """
        Creates a live view URL for a headful browser that grants either read-only or
        control access. The URL works only for the live view: it cannot connect to CDP,
        WebDriver, or any other browser endpoint. A read-only URL shows the browser but
        cannot send input, regardless of query parameters. The URL stays valid until the
        browser is deleted, or until `ttl_seconds` elapse when set. For a browser
        acquired from a pool, it stops working when the browser is released. Nothing is
        stored, so a URL cannot be revoked before then.

        Args:
          scope: `read` shows the browser without accepting input. `control` also lets the viewer
              drive the browser through the live view.

          ttl_seconds: Seconds until the URL expires. Omit to keep it valid until the browser is
              deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._post(
            path_template("/browsers/{id_or_name}/live_view", id_or_name=id_or_name),
            body=maybe_transform(
                {
                    "scope": scope,
                    "ttl_seconds": ttl_seconds,
                },
                live_view_create_params.LiveViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BrowserLiveView,
        )


class AsyncLiveViewResource(AsyncAPIResource):
    """Create and manage browser sessions."""

    @cached_property
    def with_raw_response(self) -> AsyncLiveViewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLiveViewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveViewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncLiveViewResourceWithStreamingResponse(self)

    async def create(
        self,
        id_or_name: str,
        *,
        scope: BrowserLiveViewScope | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BrowserLiveView:
        """
        Creates a live view URL for a headful browser that grants either read-only or
        control access. The URL works only for the live view: it cannot connect to CDP,
        WebDriver, or any other browser endpoint. A read-only URL shows the browser but
        cannot send input, regardless of query parameters. The URL stays valid until the
        browser is deleted, or until `ttl_seconds` elapse when set. For a browser
        acquired from a pool, it stops working when the browser is released. Nothing is
        stored, so a URL cannot be revoked before then.

        Args:
          scope: `read` shows the browser without accepting input. `control` also lets the viewer
              drive the browser through the live view.

          ttl_seconds: Seconds until the URL expires. Omit to keep it valid until the browser is
              deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._post(
            path_template("/browsers/{id_or_name}/live_view", id_or_name=id_or_name),
            body=await async_maybe_transform(
                {
                    "scope": scope,
                    "ttl_seconds": ttl_seconds,
                },
                live_view_create_params.LiveViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BrowserLiveView,
        )


class LiveViewResourceWithRawResponse:
    def __init__(self, live_view: LiveViewResource) -> None:
        self._live_view = live_view

        self.create = to_raw_response_wrapper(
            live_view.create,
        )


class AsyncLiveViewResourceWithRawResponse:
    def __init__(self, live_view: AsyncLiveViewResource) -> None:
        self._live_view = live_view

        self.create = async_to_raw_response_wrapper(
            live_view.create,
        )


class LiveViewResourceWithStreamingResponse:
    def __init__(self, live_view: LiveViewResource) -> None:
        self._live_view = live_view

        self.create = to_streamed_response_wrapper(
            live_view.create,
        )


class AsyncLiveViewResourceWithStreamingResponse:
    def __init__(self, live_view: AsyncLiveViewResource) -> None:
        self._live_view = live_view

        self.create = async_to_streamed_response_wrapper(
            live_view.create,
        )
