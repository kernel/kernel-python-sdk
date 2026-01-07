# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.auth import invocation_create_params, invocation_submit_params, invocation_exchange_params
from ....types.agents.agent_auth_submit_response import AgentAuthSubmitResponse
from ....types.agents.agent_auth_invocation_response import AgentAuthInvocationResponse
from ....types.agents.auth.invocation_exchange_response import InvocationExchangeResponse
from ....types.agents.auth_agent_invocation_create_response import AuthAgentInvocationCreateResponse

__all__ = ["InvocationsResource", "AsyncInvocationsResource"]


class InvocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return InvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return InvocationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        auth_agent_id: str,
        save_credential_as: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthAgentInvocationCreateResponse:
        """Creates a new authentication invocation for the specified auth agent.

        This
        starts the auth flow and returns a hosted URL for the user to complete
        authentication.

        Args:
          auth_agent_id: ID of the auth agent to create an invocation for

          save_credential_as: If provided, saves the submitted credentials under this name upon successful
              login. The credential will be linked to the auth agent for automatic
              re-authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents/auth/invocations",
            body=maybe_transform(
                {
                    "auth_agent_id": auth_agent_id,
                    "save_credential_as": save_credential_as,
                },
                invocation_create_params.InvocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthAgentInvocationCreateResponse,
        )

    def retrieve(
        self,
        invocation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthInvocationResponse:
        """Returns invocation details including status, app_name, and domain.

        Supports both
        API key and JWT (from exchange endpoint) authentication.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invocation_id:
            raise ValueError(f"Expected a non-empty value for `invocation_id` but received {invocation_id!r}")
        return self._get(
            f"/agents/auth/invocations/{invocation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentAuthInvocationResponse,
        )

    def exchange(
        self,
        invocation_id: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvocationExchangeResponse:
        """Validates the handoff code and returns a JWT token for subsequent requests.

        No
        authentication required (the handoff code serves as the credential).

        Args:
          code: Handoff code from start endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invocation_id:
            raise ValueError(f"Expected a non-empty value for `invocation_id` but received {invocation_id!r}")
        return self._post(
            f"/agents/auth/invocations/{invocation_id}/exchange",
            body=maybe_transform({"code": code}, invocation_exchange_params.InvocationExchangeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationExchangeResponse,
        )

    @overload
    def submit(
        self,
        invocation_id: str,
        *,
        field_values: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthSubmitResponse:
        """Submits field values for the discovered login form.

        Returns immediately after
        submission is accepted. Poll the invocation endpoint to track progress and get
        results.

        Args:
          field_values: Values for the discovered login fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def submit(
        self,
        invocation_id: str,
        *,
        sso_button: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthSubmitResponse:
        """Submits field values for the discovered login form.

        Returns immediately after
        submission is accepted. Poll the invocation endpoint to track progress and get
        results.

        Args:
          sso_button: Selector of SSO button to click

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["field_values"], ["sso_button"])
    def submit(
        self,
        invocation_id: str,
        *,
        field_values: Dict[str, str] | Omit = omit,
        sso_button: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthSubmitResponse:
        if not invocation_id:
            raise ValueError(f"Expected a non-empty value for `invocation_id` but received {invocation_id!r}")
        return self._post(
            f"/agents/auth/invocations/{invocation_id}/submit",
            body=maybe_transform(
                {
                    "field_values": field_values,
                    "sso_button": sso_button,
                },
                invocation_submit_params.InvocationSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentAuthSubmitResponse,
        )


class AsyncInvocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncInvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncInvocationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        auth_agent_id: str,
        save_credential_as: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthAgentInvocationCreateResponse:
        """Creates a new authentication invocation for the specified auth agent.

        This
        starts the auth flow and returns a hosted URL for the user to complete
        authentication.

        Args:
          auth_agent_id: ID of the auth agent to create an invocation for

          save_credential_as: If provided, saves the submitted credentials under this name upon successful
              login. The credential will be linked to the auth agent for automatic
              re-authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents/auth/invocations",
            body=await async_maybe_transform(
                {
                    "auth_agent_id": auth_agent_id,
                    "save_credential_as": save_credential_as,
                },
                invocation_create_params.InvocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthAgentInvocationCreateResponse,
        )

    async def retrieve(
        self,
        invocation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthInvocationResponse:
        """Returns invocation details including status, app_name, and domain.

        Supports both
        API key and JWT (from exchange endpoint) authentication.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invocation_id:
            raise ValueError(f"Expected a non-empty value for `invocation_id` but received {invocation_id!r}")
        return await self._get(
            f"/agents/auth/invocations/{invocation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentAuthInvocationResponse,
        )

    async def exchange(
        self,
        invocation_id: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvocationExchangeResponse:
        """Validates the handoff code and returns a JWT token for subsequent requests.

        No
        authentication required (the handoff code serves as the credential).

        Args:
          code: Handoff code from start endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invocation_id:
            raise ValueError(f"Expected a non-empty value for `invocation_id` but received {invocation_id!r}")
        return await self._post(
            f"/agents/auth/invocations/{invocation_id}/exchange",
            body=await async_maybe_transform({"code": code}, invocation_exchange_params.InvocationExchangeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationExchangeResponse,
        )

    @overload
    async def submit(
        self,
        invocation_id: str,
        *,
        field_values: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthSubmitResponse:
        """Submits field values for the discovered login form.

        Returns immediately after
        submission is accepted. Poll the invocation endpoint to track progress and get
        results.

        Args:
          field_values: Values for the discovered login fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def submit(
        self,
        invocation_id: str,
        *,
        sso_button: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthSubmitResponse:
        """Submits field values for the discovered login form.

        Returns immediately after
        submission is accepted. Poll the invocation endpoint to track progress and get
        results.

        Args:
          sso_button: Selector of SSO button to click

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["field_values"], ["sso_button"])
    async def submit(
        self,
        invocation_id: str,
        *,
        field_values: Dict[str, str] | Omit = omit,
        sso_button: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentAuthSubmitResponse:
        if not invocation_id:
            raise ValueError(f"Expected a non-empty value for `invocation_id` but received {invocation_id!r}")
        return await self._post(
            f"/agents/auth/invocations/{invocation_id}/submit",
            body=await async_maybe_transform(
                {
                    "field_values": field_values,
                    "sso_button": sso_button,
                },
                invocation_submit_params.InvocationSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentAuthSubmitResponse,
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
        self.exchange = to_raw_response_wrapper(
            invocations.exchange,
        )
        self.submit = to_raw_response_wrapper(
            invocations.submit,
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
        self.exchange = async_to_raw_response_wrapper(
            invocations.exchange,
        )
        self.submit = async_to_raw_response_wrapper(
            invocations.submit,
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
        self.exchange = to_streamed_response_wrapper(
            invocations.exchange,
        )
        self.submit = to_streamed_response_wrapper(
            invocations.submit,
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
        self.exchange = async_to_streamed_response_wrapper(
            invocations.exchange,
        )
        self.submit = async_to_streamed_response_wrapper(
            invocations.submit,
        )
