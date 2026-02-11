# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.auth import (
    connection_list_params,
    connection_login_params,
    connection_create_params,
    connection_submit_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.auth.managed_auth import ManagedAuth
from ...types.auth.login_response import LoginResponse
from ...types.auth.submit_fields_response import SubmitFieldsResponse
from ...types.auth.connection_follow_response import ConnectionFollowResponse

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        domain: str,
        profile_name: str,
        allowed_domains: SequenceNotStr[str] | Omit = omit,
        credential: connection_create_params.Credential | Omit = omit,
        health_check_interval: int | Omit = omit,
        login_url: str | Omit = omit,
        proxy: connection_create_params.Proxy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAuth:
        """Creates an auth connection for a profile and domain combination.

        Returns 409
        Conflict if an auth connection already exists for the given profile and domain.

        Args:
          domain: Domain for authentication

          profile_name: Name of the profile to manage authentication for

          allowed_domains: Additional domains valid for this auth flow (besides the primary domain). Useful
              when login pages redirect to different domains.

              The following SSO/OAuth provider domains are automatically allowed by default
              and do not need to be specified:

              - Google: accounts.google.com
              - Microsoft/Azure AD: login.microsoftonline.com, login.live.com
              - Okta: _.okta.com, _.oktapreview.com
              - Auth0: _.auth0.com, _.us.auth0.com, _.eu.auth0.com, _.au.auth0.com
              - Apple: appleid.apple.com
              - GitHub: github.com
              - Facebook/Meta: www.facebook.com
              - LinkedIn: www.linkedin.com
              - Amazon Cognito: \\**.amazoncognito.com
              - OneLogin: \\**.onelogin.com
              - Ping Identity: _.pingone.com, _.pingidentity.com

          credential:
              Reference to credentials for the auth connection. Use one of:

              - { name } for Kernel credentials
              - { provider, path } for external provider item
              - { provider, auto: true } for external provider domain lookup

          health_check_interval: Interval in seconds between automatic health checks. When set, the system
              periodically verifies the authentication status and triggers re-authentication
              if needed. Maximum is 86400 (24 hours). Default is 3600 (1 hour). The minimum
              depends on your plan: Enterprise: 300 (5 minutes), Startup: 1200 (20 minutes),
              Hobbyist: 3600 (1 hour).

          login_url: Optional login page URL to skip discovery

          proxy: Proxy selection. Provide either id or name. The proxy must belong to the
              caller's org.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/connections",
            body=maybe_transform(
                {
                    "domain": domain,
                    "profile_name": profile_name,
                    "allowed_domains": allowed_domains,
                    "credential": credential,
                    "health_check_interval": health_check_interval,
                    "login_url": login_url,
                    "proxy": proxy,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAuth,
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
    ) -> ManagedAuth:
        """Retrieve an auth connection by its ID.

        Includes current flow state if a login is
        in progress.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/auth/connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAuth,
        )

    def list(
        self,
        *,
        domain: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        profile_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ManagedAuth]:
        """
        List auth connections with optional filters for profile_name and domain.

        Args:
          domain: Filter by domain

          limit: Maximum number of results to return

          offset: Number of results to skip

          profile_name: Filter by profile name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/auth/connections",
            page=SyncOffsetPagination[ManagedAuth],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "limit": limit,
                        "offset": offset,
                        "profile_name": profile_name,
                    },
                    connection_list_params.ConnectionListParams,
                ),
            ),
            model=ManagedAuth,
        )

    def delete(
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
        """Deletes an auth connection and terminates its workflow.

        This will:

        - Delete the auth connection record
        - Terminate the Temporal workflow
        - Cancel any in-progress login flows

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
            f"/auth/connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def follow(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ConnectionFollowResponse]:
        """
        Establishes a Server-Sent Events (SSE) stream that delivers real-time login flow
        state updates. The stream terminates automatically once the flow reaches a
        terminal state (SUCCESS, FAILED, EXPIRED, CANCELED).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            f"/auth/connections/{id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ConnectionFollowResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ConnectionFollowResponse],
        )

    def login(
        self,
        id: str,
        *,
        proxy: connection_login_params.Proxy | Omit = omit,
        save_credential_as: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginResponse:
        """Starts a login flow for the auth connection.

        Returns immediately with a hosted
        URL for the user to complete authentication, or triggers automatic re-auth if
        credentials are stored.

        Args:
          proxy: Proxy selection. Provide either id or name. The proxy must belong to the
              caller's org.

          save_credential_as: If provided, saves credentials under this name upon successful login

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/auth/connections/{id}/login",
            body=maybe_transform(
                {
                    "proxy": proxy,
                    "save_credential_as": save_credential_as,
                },
                connection_login_params.ConnectionLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginResponse,
        )

    def submit(
        self,
        id: str,
        *,
        fields: Dict[str, str],
        mfa_option_id: str | Omit = omit,
        sso_button_selector: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmitFieldsResponse:
        """Submits field values for the login form.

        Poll the auth connection to track
        progress and get results.

        Args:
          fields: Map of field name to value

          mfa_option_id: Optional MFA option ID if user selected an MFA method

          sso_button_selector: Optional XPath selector if user chose to click an SSO button instead

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/auth/connections/{id}/submit",
            body=maybe_transform(
                {
                    "fields": fields,
                    "mfa_option_id": mfa_option_id,
                    "sso_button_selector": sso_button_selector,
                },
                connection_submit_params.ConnectionSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmitFieldsResponse,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        domain: str,
        profile_name: str,
        allowed_domains: SequenceNotStr[str] | Omit = omit,
        credential: connection_create_params.Credential | Omit = omit,
        health_check_interval: int | Omit = omit,
        login_url: str | Omit = omit,
        proxy: connection_create_params.Proxy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAuth:
        """Creates an auth connection for a profile and domain combination.

        Returns 409
        Conflict if an auth connection already exists for the given profile and domain.

        Args:
          domain: Domain for authentication

          profile_name: Name of the profile to manage authentication for

          allowed_domains: Additional domains valid for this auth flow (besides the primary domain). Useful
              when login pages redirect to different domains.

              The following SSO/OAuth provider domains are automatically allowed by default
              and do not need to be specified:

              - Google: accounts.google.com
              - Microsoft/Azure AD: login.microsoftonline.com, login.live.com
              - Okta: _.okta.com, _.oktapreview.com
              - Auth0: _.auth0.com, _.us.auth0.com, _.eu.auth0.com, _.au.auth0.com
              - Apple: appleid.apple.com
              - GitHub: github.com
              - Facebook/Meta: www.facebook.com
              - LinkedIn: www.linkedin.com
              - Amazon Cognito: \\**.amazoncognito.com
              - OneLogin: \\**.onelogin.com
              - Ping Identity: _.pingone.com, _.pingidentity.com

          credential:
              Reference to credentials for the auth connection. Use one of:

              - { name } for Kernel credentials
              - { provider, path } for external provider item
              - { provider, auto: true } for external provider domain lookup

          health_check_interval: Interval in seconds between automatic health checks. When set, the system
              periodically verifies the authentication status and triggers re-authentication
              if needed. Maximum is 86400 (24 hours). Default is 3600 (1 hour). The minimum
              depends on your plan: Enterprise: 300 (5 minutes), Startup: 1200 (20 minutes),
              Hobbyist: 3600 (1 hour).

          login_url: Optional login page URL to skip discovery

          proxy: Proxy selection. Provide either id or name. The proxy must belong to the
              caller's org.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/connections",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "profile_name": profile_name,
                    "allowed_domains": allowed_domains,
                    "credential": credential,
                    "health_check_interval": health_check_interval,
                    "login_url": login_url,
                    "proxy": proxy,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAuth,
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
    ) -> ManagedAuth:
        """Retrieve an auth connection by its ID.

        Includes current flow state if a login is
        in progress.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/auth/connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAuth,
        )

    def list(
        self,
        *,
        domain: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        profile_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ManagedAuth, AsyncOffsetPagination[ManagedAuth]]:
        """
        List auth connections with optional filters for profile_name and domain.

        Args:
          domain: Filter by domain

          limit: Maximum number of results to return

          offset: Number of results to skip

          profile_name: Filter by profile name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/auth/connections",
            page=AsyncOffsetPagination[ManagedAuth],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "limit": limit,
                        "offset": offset,
                        "profile_name": profile_name,
                    },
                    connection_list_params.ConnectionListParams,
                ),
            ),
            model=ManagedAuth,
        )

    async def delete(
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
        """Deletes an auth connection and terminates its workflow.

        This will:

        - Delete the auth connection record
        - Terminate the Temporal workflow
        - Cancel any in-progress login flows

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
            f"/auth/connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def follow(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ConnectionFollowResponse]:
        """
        Establishes a Server-Sent Events (SSE) stream that delivers real-time login flow
        state updates. The stream terminates automatically once the flow reaches a
        terminal state (SUCCESS, FAILED, EXPIRED, CANCELED).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            f"/auth/connections/{id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ConnectionFollowResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ConnectionFollowResponse],
        )

    async def login(
        self,
        id: str,
        *,
        proxy: connection_login_params.Proxy | Omit = omit,
        save_credential_as: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginResponse:
        """Starts a login flow for the auth connection.

        Returns immediately with a hosted
        URL for the user to complete authentication, or triggers automatic re-auth if
        credentials are stored.

        Args:
          proxy: Proxy selection. Provide either id or name. The proxy must belong to the
              caller's org.

          save_credential_as: If provided, saves credentials under this name upon successful login

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/auth/connections/{id}/login",
            body=await async_maybe_transform(
                {
                    "proxy": proxy,
                    "save_credential_as": save_credential_as,
                },
                connection_login_params.ConnectionLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginResponse,
        )

    async def submit(
        self,
        id: str,
        *,
        fields: Dict[str, str],
        mfa_option_id: str | Omit = omit,
        sso_button_selector: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmitFieldsResponse:
        """Submits field values for the login form.

        Poll the auth connection to track
        progress and get results.

        Args:
          fields: Map of field name to value

          mfa_option_id: Optional MFA option ID if user selected an MFA method

          sso_button_selector: Optional XPath selector if user chose to click an SSO button instead

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/auth/connections/{id}/submit",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "mfa_option_id": mfa_option_id,
                    "sso_button_selector": sso_button_selector,
                },
                connection_submit_params.ConnectionSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmitFieldsResponse,
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.create = to_raw_response_wrapper(
            connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connections.retrieve,
        )
        self.list = to_raw_response_wrapper(
            connections.list,
        )
        self.delete = to_raw_response_wrapper(
            connections.delete,
        )
        self.follow = to_raw_response_wrapper(
            connections.follow,
        )
        self.login = to_raw_response_wrapper(
            connections.login,
        )
        self.submit = to_raw_response_wrapper(
            connections.submit,
        )


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.create = async_to_raw_response_wrapper(
            connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connections.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connections.delete,
        )
        self.follow = async_to_raw_response_wrapper(
            connections.follow,
        )
        self.login = async_to_raw_response_wrapper(
            connections.login,
        )
        self.submit = async_to_raw_response_wrapper(
            connections.submit,
        )


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.create = to_streamed_response_wrapper(
            connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            connections.delete,
        )
        self.follow = to_streamed_response_wrapper(
            connections.follow,
        )
        self.login = to_streamed_response_wrapper(
            connections.login,
        )
        self.submit = to_streamed_response_wrapper(
            connections.submit,
        )


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.create = async_to_streamed_response_wrapper(
            connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connections.delete,
        )
        self.follow = async_to_streamed_response_wrapper(
            connections.follow,
        )
        self.login = async_to_streamed_response_wrapper(
            connections.login,
        )
        self.submit = async_to_streamed_response_wrapper(
            connections.submit,
        )
