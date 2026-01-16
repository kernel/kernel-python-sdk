# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import invocation_list_params, invocation_create_params, invocation_follow_params, invocation_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.invocation_list_response import InvocationListResponse
from ..types.invocation_create_response import InvocationCreateResponse
from ..types.invocation_follow_response import InvocationFollowResponse
from ..types.invocation_update_response import InvocationUpdateResponse
from ..types.invocation_retrieve_response import InvocationRetrieveResponse

__all__ = ["InvocationsResource", "AsyncInvocationsResource"]


class InvocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return InvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return InvocationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action_name: str,
        app_name: str,
        version: str,
        async_: bool | Omit = omit,
        async_timeout_seconds: int | Omit = omit,
        payload: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvocationCreateResponse:
        """
        Invoke an action.

        Args:
          action_name: Name of the action to invoke

          app_name: Name of the application

          version: Version of the application

          async_: If true, invoke asynchronously. When set, the API responds 202 Accepted with
              status "queued".

          async_timeout_seconds: Timeout in seconds for async invocations (min 10, max 3600). Only applies when
              async is true.

          payload: Input data for the action, sent as a JSON string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/invocations",
            body=maybe_transform(
                {
                    "action_name": action_name,
                    "app_name": app_name,
                    "version": version,
                    "async_": async_,
                    "async_timeout_seconds": async_timeout_seconds,
                    "payload": payload,
                },
                invocation_create_params.InvocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationCreateResponse,
        )

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
    ) -> InvocationRetrieveResponse:
        """
        Get details about an invocation's status and output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/invocations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["succeeded", "failed"],
        output: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvocationUpdateResponse:
        """Update an invocation's status or output.

        This can be used to cancel an
        invocation by setting the status to "failed".

        Args:
          status: New status for the invocation.

          output: Updated output of the invocation rendered as JSON string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/invocations/{id}",
            body=maybe_transform(
                {
                    "status": status,
                    "output": output,
                },
                invocation_update_params.InvocationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationUpdateResponse,
        )

    def list(
        self,
        *,
        action_name: str | Omit = omit,
        app_name: str | Omit = omit,
        deployment_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        since: str | Omit = omit,
        status: Literal["queued", "running", "succeeded", "failed"] | Omit = omit,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[InvocationListResponse]:
        """List invocations.

        Optionally filter by application name, action name, status,
        deployment ID, or start time.

        Args:
          action_name: Filter results by action name.

          app_name: Filter results by application name.

          deployment_id: Filter results by deployment ID.

          limit: Limit the number of invocations to return.

          offset: Offset the number of invocations to return.

          since: Show invocations that have started since the given time (RFC timestamps or
              durations like 5m).

          status: Filter results by invocation status.

          version: Filter results by application version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/invocations",
            page=SyncOffsetPagination[InvocationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_name": action_name,
                        "app_name": app_name,
                        "deployment_id": deployment_id,
                        "limit": limit,
                        "offset": offset,
                        "since": since,
                        "status": status,
                        "version": version,
                    },
                    invocation_list_params.InvocationListParams,
                ),
            ),
            model=InvocationListResponse,
        )

    def delete_browsers(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete all browser sessions created within the specified invocation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/invocations/{id}/browsers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def follow(
        self,
        id: str,
        *,
        since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[InvocationFollowResponse]:
        """
        Establishes a Server-Sent Events (SSE) stream that delivers real-time logs and
        status updates for an invocation. The stream terminates automatically once the
        invocation reaches a terminal state.

        Args:
          since: Show logs since the given time (RFC timestamps or durations like 5m).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            f"/invocations/{id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"since": since}, invocation_follow_params.InvocationFollowParams),
            ),
            cast_to=cast(
                Any, InvocationFollowResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[InvocationFollowResponse],
        )


class AsyncInvocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncInvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncInvocationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action_name: str,
        app_name: str,
        version: str,
        async_: bool | Omit = omit,
        async_timeout_seconds: int | Omit = omit,
        payload: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvocationCreateResponse:
        """
        Invoke an action.

        Args:
          action_name: Name of the action to invoke

          app_name: Name of the application

          version: Version of the application

          async_: If true, invoke asynchronously. When set, the API responds 202 Accepted with
              status "queued".

          async_timeout_seconds: Timeout in seconds for async invocations (min 10, max 3600). Only applies when
              async is true.

          payload: Input data for the action, sent as a JSON string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/invocations",
            body=await async_maybe_transform(
                {
                    "action_name": action_name,
                    "app_name": app_name,
                    "version": version,
                    "async_": async_,
                    "async_timeout_seconds": async_timeout_seconds,
                    "payload": payload,
                },
                invocation_create_params.InvocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationCreateResponse,
        )

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
    ) -> InvocationRetrieveResponse:
        """
        Get details about an invocation's status and output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/invocations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["succeeded", "failed"],
        output: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvocationUpdateResponse:
        """Update an invocation's status or output.

        This can be used to cancel an
        invocation by setting the status to "failed".

        Args:
          status: New status for the invocation.

          output: Updated output of the invocation rendered as JSON string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/invocations/{id}",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "output": output,
                },
                invocation_update_params.InvocationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationUpdateResponse,
        )

    def list(
        self,
        *,
        action_name: str | Omit = omit,
        app_name: str | Omit = omit,
        deployment_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        since: str | Omit = omit,
        status: Literal["queued", "running", "succeeded", "failed"] | Omit = omit,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InvocationListResponse, AsyncOffsetPagination[InvocationListResponse]]:
        """List invocations.

        Optionally filter by application name, action name, status,
        deployment ID, or start time.

        Args:
          action_name: Filter results by action name.

          app_name: Filter results by application name.

          deployment_id: Filter results by deployment ID.

          limit: Limit the number of invocations to return.

          offset: Offset the number of invocations to return.

          since: Show invocations that have started since the given time (RFC timestamps or
              durations like 5m).

          status: Filter results by invocation status.

          version: Filter results by application version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/invocations",
            page=AsyncOffsetPagination[InvocationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_name": action_name,
                        "app_name": app_name,
                        "deployment_id": deployment_id,
                        "limit": limit,
                        "offset": offset,
                        "since": since,
                        "status": status,
                        "version": version,
                    },
                    invocation_list_params.InvocationListParams,
                ),
            ),
            model=InvocationListResponse,
        )

    async def delete_browsers(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete all browser sessions created within the specified invocation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/invocations/{id}/browsers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def follow(
        self,
        id: str,
        *,
        since: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[InvocationFollowResponse]:
        """
        Establishes a Server-Sent Events (SSE) stream that delivers real-time logs and
        status updates for an invocation. The stream terminates automatically once the
        invocation reaches a terminal state.

        Args:
          since: Show logs since the given time (RFC timestamps or durations like 5m).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            f"/invocations/{id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"since": since}, invocation_follow_params.InvocationFollowParams),
            ),
            cast_to=cast(
                Any, InvocationFollowResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[InvocationFollowResponse],
        )


class InvocationsResourceWithRawResponse:
    def __init__(self, invocations: InvocationsResource) -> None:
        self._invocations = invocations

        self.create = to_raw_response_wrapper(
            invocations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invocations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            invocations.update,
        )
        self.list = to_raw_response_wrapper(
            invocations.list,
        )
        self.delete_browsers = to_raw_response_wrapper(
            invocations.delete_browsers,
        )
        self.follow = to_raw_response_wrapper(
            invocations.follow,
        )


class AsyncInvocationsResourceWithRawResponse:
    def __init__(self, invocations: AsyncInvocationsResource) -> None:
        self._invocations = invocations

        self.create = async_to_raw_response_wrapper(
            invocations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invocations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            invocations.update,
        )
        self.list = async_to_raw_response_wrapper(
            invocations.list,
        )
        self.delete_browsers = async_to_raw_response_wrapper(
            invocations.delete_browsers,
        )
        self.follow = async_to_raw_response_wrapper(
            invocations.follow,
        )


class InvocationsResourceWithStreamingResponse:
    def __init__(self, invocations: InvocationsResource) -> None:
        self._invocations = invocations

        self.create = to_streamed_response_wrapper(
            invocations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invocations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            invocations.update,
        )
        self.list = to_streamed_response_wrapper(
            invocations.list,
        )
        self.delete_browsers = to_streamed_response_wrapper(
            invocations.delete_browsers,
        )
        self.follow = to_streamed_response_wrapper(
            invocations.follow,
        )


class AsyncInvocationsResourceWithStreamingResponse:
    def __init__(self, invocations: AsyncInvocationsResource) -> None:
        self._invocations = invocations

        self.create = async_to_streamed_response_wrapper(
            invocations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invocations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            invocations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            invocations.list,
        )
        self.delete_browsers = async_to_streamed_response_wrapper(
            invocations.delete_browsers,
        )
        self.follow = async_to_streamed_response_wrapper(
            invocations.follow,
        )
