# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ..._base_client import make_request_options
from ...types.organization import limit_update_params
from ...types.organization.org_limits import OrgLimits

__all__ = ["LimitsResource", "AsyncLimitsResource"]


class LimitsResource(SyncAPIResource):
    """Read and manage organization-level limits."""

    @cached_property
    def with_raw_response(self) -> LimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return LimitsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgLimits:
        """
        Get the organization's concurrent session ceiling and the default per-project
        concurrency cap applied to projects without an explicit override.
        """
        return self._get(
            "/org/limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgLimits,
        )

    def update(
        self,
        *,
        default_project_max_concurrent_sessions: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgLimits:
        """
        Set the default per-project concurrency cap applied to projects without an
        explicit override. Set the value to 0 to remove the default; omit to leave it
        unchanged. The default cannot exceed the organization's concurrent session
        ceiling.

        Args:
          default_project_max_concurrent_sessions: Default maximum concurrent browser sessions for projects without an explicit
              override. Set to 0 to remove the default; omit to leave unchanged. Cannot exceed
              the organization's concurrent session ceiling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/org/limits",
            body=maybe_transform(
                {"default_project_max_concurrent_sessions": default_project_max_concurrent_sessions},
                limit_update_params.LimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgLimits,
        )


class AsyncLimitsResource(AsyncAPIResource):
    """Read and manage organization-level limits."""

    @cached_property
    def with_raw_response(self) -> AsyncLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncLimitsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgLimits:
        """
        Get the organization's concurrent session ceiling and the default per-project
        concurrency cap applied to projects without an explicit override.
        """
        return await self._get(
            "/org/limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgLimits,
        )

    async def update(
        self,
        *,
        default_project_max_concurrent_sessions: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgLimits:
        """
        Set the default per-project concurrency cap applied to projects without an
        explicit override. Set the value to 0 to remove the default; omit to leave it
        unchanged. The default cannot exceed the organization's concurrent session
        ceiling.

        Args:
          default_project_max_concurrent_sessions: Default maximum concurrent browser sessions for projects without an explicit
              override. Set to 0 to remove the default; omit to leave unchanged. Cannot exceed
              the organization's concurrent session ceiling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/org/limits",
            body=await async_maybe_transform(
                {"default_project_max_concurrent_sessions": default_project_max_concurrent_sessions},
                limit_update_params.LimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgLimits,
        )


class LimitsResourceWithRawResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.retrieve = to_raw_response_wrapper(
            limits.retrieve,
        )
        self.update = to_raw_response_wrapper(
            limits.update,
        )


class AsyncLimitsResourceWithRawResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.retrieve = async_to_raw_response_wrapper(
            limits.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            limits.update,
        )


class LimitsResourceWithStreamingResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.retrieve = to_streamed_response_wrapper(
            limits.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            limits.update,
        )


class AsyncLimitsResourceWithStreamingResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.retrieve = async_to_streamed_response_wrapper(
            limits.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            limits.update,
        )
