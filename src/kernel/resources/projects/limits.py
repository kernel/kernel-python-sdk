# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.projects import limit_update_params
from ...types.projects.project_limits import ProjectLimits

__all__ = ["LimitsResource", "AsyncLimitsResource"]


class LimitsResource(SyncAPIResource):
    """Create and manage projects for resource isolation within an organization."""

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
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectLimits:
        """Get the resource limit overrides for a project.

        Null values mean no
        project-level cap (org limit applies).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/projects/{id}/limits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectLimits,
        )

    def update(
        self,
        id: str,
        *,
        max_concurrent_invocations: Optional[int] | Omit = omit,
        max_concurrent_sessions: Optional[int] | Omit = omit,
        max_persistent_sessions: Optional[int] | Omit = omit,
        max_pooled_sessions: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectLimits:
        """Update resource limit overrides for a project.

        Only fields present in the
        request are modified. Set a field to 0 to remove that limit cap; omit a field to
        leave it unchanged.

        Args:
          max_concurrent_invocations: Maximum concurrent app invocations for this project. Set to 0 to remove the cap;
              omit to leave unchanged.

          max_concurrent_sessions: Maximum concurrent browser sessions for this project. Set to 0 to remove the
              cap; omit to leave unchanged.

          max_persistent_sessions: Maximum persistent browser sessions for this project. Set to 0 to remove the
              cap; omit to leave unchanged.

          max_pooled_sessions: Maximum pooled sessions capacity for this project. Set to 0 to remove the cap;
              omit to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/projects/{id}/limits", id=id),
            body=maybe_transform(
                {
                    "max_concurrent_invocations": max_concurrent_invocations,
                    "max_concurrent_sessions": max_concurrent_sessions,
                    "max_persistent_sessions": max_persistent_sessions,
                    "max_pooled_sessions": max_pooled_sessions,
                },
                limit_update_params.LimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectLimits,
        )


class AsyncLimitsResource(AsyncAPIResource):
    """Create and manage projects for resource isolation within an organization."""

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
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectLimits:
        """Get the resource limit overrides for a project.

        Null values mean no
        project-level cap (org limit applies).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/projects/{id}/limits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectLimits,
        )

    async def update(
        self,
        id: str,
        *,
        max_concurrent_invocations: Optional[int] | Omit = omit,
        max_concurrent_sessions: Optional[int] | Omit = omit,
        max_persistent_sessions: Optional[int] | Omit = omit,
        max_pooled_sessions: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectLimits:
        """Update resource limit overrides for a project.

        Only fields present in the
        request are modified. Set a field to 0 to remove that limit cap; omit a field to
        leave it unchanged.

        Args:
          max_concurrent_invocations: Maximum concurrent app invocations for this project. Set to 0 to remove the cap;
              omit to leave unchanged.

          max_concurrent_sessions: Maximum concurrent browser sessions for this project. Set to 0 to remove the
              cap; omit to leave unchanged.

          max_persistent_sessions: Maximum persistent browser sessions for this project. Set to 0 to remove the
              cap; omit to leave unchanged.

          max_pooled_sessions: Maximum pooled sessions capacity for this project. Set to 0 to remove the cap;
              omit to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/projects/{id}/limits", id=id),
            body=await async_maybe_transform(
                {
                    "max_concurrent_invocations": max_concurrent_invocations,
                    "max_concurrent_sessions": max_concurrent_sessions,
                    "max_persistent_sessions": max_persistent_sessions,
                    "max_pooled_sessions": max_pooled_sessions,
                },
                limit_update_params.LimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectLimits,
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
