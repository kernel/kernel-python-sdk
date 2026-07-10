# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
    connection_update_params,
    connection_timeline_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.auth.managed_auth import ManagedAuth
from ...types.auth.login_response import LoginResponse
from ...types.auth.submit_fields_response import SubmitFieldsResponse
from ...types.auth.connection_follow_response import ConnectionFollowResponse
from ...types.auth.managed_auth_timeline_event import ManagedAuthTimelineEvent

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    """Create and manage auth connections for automated credential capture and login."""

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
        auto_reauth: bool | Omit = omit,
        credential: connection_create_params.Credential | Omit = omit,
        health_check_interval: int | Omit = omit,
        health_checks: bool | Omit = omit,
        login_url: str | Omit = omit,
        proxy: connection_create_params.Proxy | Omit = omit,
        record_session: bool | Omit = omit,
        save_credentials: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAuth:
        """Creates an auth connection for a profile and domain combination.

        If the provided
        profile_name does not exist, it is created automatically. Returns 409 Conflict
        if an auth connection already exists for the given profile and domain.

        Args:
          domain: Domain for authentication

          profile_name: Name of the profile to manage authentication for. If the profile does not exist,
              it is created automatically.

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

          auto_reauth: Whether to permit automatic re-authentication when a scheduled health check
              detects an expired session. This is an opt-in flag only — it does not check
              whether re-auth is actually feasible. Even when true, re-auth only runs when the
              system has what it needs to perform it (for example, saved credentials for the
              required login fields), and only after a scheduled health check detects an
              expired session — so this flag has no effect when `health_checks` is false. When
              false, expired sessions are marked as `NEEDS_AUTH` instead of attempting
              re-auth. Defaults to true.

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

          health_checks: Whether to enable periodic health checks. When false, the system will not
              automatically verify authentication status, and `auto_reauth` has no effect on
              the automatic flow (since re-auth is only triggered by a failed scheduled health
              check). Defaults to true.

          login_url: Optional login page URL to skip discovery

          proxy: Proxy selection. Provide either id or name. The proxy must be in the same
              project as the resource referencing it. When selecting by name, the name must
              match exactly one active proxy in the project. Ambiguous names return a 400; use
              id for stable references.

          record_session: Whether to record browser sessions for this connection by default. Useful for
              debugging. Can be overridden per-login. Defaults to false.

          save_credentials: Whether to save credentials after every successful login. Defaults to true.
              One-time codes (TOTP, SMS, etc.) are not saved.

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
                    "auto_reauth": auto_reauth,
                    "credential": credential,
                    "health_check_interval": health_check_interval,
                    "health_checks": health_checks,
                    "login_url": login_url,
                    "proxy": proxy,
                    "record_session": record_session,
                    "save_credentials": save_credentials,
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
            path_template("/auth/connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAuth,
        )

    def update(
        self,
        id: str,
        *,
        allowed_domains: SequenceNotStr[str] | Omit = omit,
        auto_reauth: bool | Omit = omit,
        credential: connection_update_params.Credential | Omit = omit,
        health_check_interval: int | Omit = omit,
        health_checks: bool | Omit = omit,
        login_url: str | Omit = omit,
        proxy: connection_update_params.Proxy | Omit = omit,
        record_session: bool | Omit = omit,
        save_credentials: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAuth:
        """Update an auth connection's configuration.

        Only the fields provided will be
        updated.

        Args:
          allowed_domains: Additional domains valid for this auth flow (replaces existing list)

          auto_reauth: Whether automatic re-authentication is permitted for this connection. This is an
              opt-in flag only — it does not check whether re-auth is actually feasible. Even
              when true, re-auth only runs when the system has what it needs to perform it
              (for example, saved credentials for the required login fields), and only after a
              scheduled health check detects an expired session — so this flag has no effect
              when `health_checks` is false. When false, expired sessions detected by a health
              check are marked as `NEEDS_AUTH` instead of attempting re-auth.

          credential:
              Reference to credentials for the auth connection. Use one of:

              - { name } for Kernel credentials
              - { provider, path } for external provider item
              - { provider, auto: true } for external provider domain lookup

          health_check_interval: Interval in seconds between automatic health checks

          health_checks: Whether periodic health checks are enabled. When set to false, the system will
              not automatically verify authentication status, and `auto_reauth` has no effect
              on the automatic flow (since re-auth is only triggered by a failed scheduled
              health check).

          login_url: Login page URL. Set to empty string to clear.

          proxy: Proxy selection. Provide either id or name. The proxy must be in the same
              project as the resource referencing it. When selecting by name, the name must
              match exactly one active proxy in the project. Ambiguous names return a 400; use
              id for stable references.

          record_session: Whether to record browser sessions for this connection by default

          save_credentials: Whether to save credentials after every successful login

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/auth/connections/{id}", id=id),
            body=maybe_transform(
                {
                    "allowed_domains": allowed_domains,
                    "auto_reauth": auto_reauth,
                    "credential": credential,
                    "health_check_interval": health_check_interval,
                    "health_checks": health_checks,
                    "login_url": login_url,
                    "proxy": proxy,
                    "record_session": record_session,
                    "save_credentials": save_credentials,
                },
                connection_update_params.ConnectionUpdateParams,
            ),
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
        query: str | Omit = omit,
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

          query: Search auth connections by ID, domain, or profile name.

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
                        "query": query,
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
            path_template("/auth/connections/{id}", id=id),
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
            path_template("/auth/connections/{id}/events", id=id),
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
        record_session: bool | Omit = omit,
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
          proxy: Proxy selection. Provide either id or name. The proxy must be in the same
              project as the resource referencing it. When selecting by name, the name must
              match exactly one active proxy in the project. Ambiguous names return a 400; use
              id for stable references.

          record_session: Override the connection's default for recording this login's browser session.
              When omitted, the connection's record_session default is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/auth/connections/{id}/login", id=id),
            body=maybe_transform(
                {
                    "proxy": proxy,
                    "record_session": record_session,
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
        fields: Dict[str, str] | Omit = omit,
        mfa_option_id: str | Omit = omit,
        sign_in_option_id: str | Omit = omit,
        sso_button_selector: str | Omit = omit,
        sso_provider: str | Omit = omit,
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

          mfa_option_id: The MFA method type to select (when mfa_options were returned)

          sign_in_option_id: The sign-in option ID to select (when sign_in_options were returned)

          sso_button_selector: XPath selector for the SSO button to click (ODA). Use sso_provider instead for
              CUA.

          sso_provider: SSO provider to click, matching the provider field from pending_sso_buttons
              (e.g., "google", "github"). Cannot be used with sso_button_selector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/auth/connections/{id}/submit", id=id),
            body=maybe_transform(
                {
                    "fields": fields,
                    "mfa_option_id": mfa_option_id,
                    "sign_in_option_id": sign_in_option_id,
                    "sso_button_selector": sso_button_selector,
                    "sso_provider": sso_provider,
                },
                connection_submit_params.ConnectionSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmitFieldsResponse,
        )

    def timeline(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        type: Literal["login", "reauth", "health_check"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[ManagedAuthTimelineEvent]:
        """
        Returns a chronological timeline of events for an auth connection — login
        attempts, automatic re-auth attempts, and health checks. Events are returned
        newest-first.

        Args:
          limit: Maximum number of events to return

          offset: Number of events to skip

          type: Filter the timeline to a single event type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/auth/connections/{id}/timeline", id=id),
            page=SyncOffsetPagination[ManagedAuthTimelineEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "type": type,
                    },
                    connection_timeline_params.ConnectionTimelineParams,
                ),
            ),
            model=ManagedAuthTimelineEvent,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    """Create and manage auth connections for automated credential capture and login."""

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
        auto_reauth: bool | Omit = omit,
        credential: connection_create_params.Credential | Omit = omit,
        health_check_interval: int | Omit = omit,
        health_checks: bool | Omit = omit,
        login_url: str | Omit = omit,
        proxy: connection_create_params.Proxy | Omit = omit,
        record_session: bool | Omit = omit,
        save_credentials: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAuth:
        """Creates an auth connection for a profile and domain combination.

        If the provided
        profile_name does not exist, it is created automatically. Returns 409 Conflict
        if an auth connection already exists for the given profile and domain.

        Args:
          domain: Domain for authentication

          profile_name: Name of the profile to manage authentication for. If the profile does not exist,
              it is created automatically.

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

          auto_reauth: Whether to permit automatic re-authentication when a scheduled health check
              detects an expired session. This is an opt-in flag only — it does not check
              whether re-auth is actually feasible. Even when true, re-auth only runs when the
              system has what it needs to perform it (for example, saved credentials for the
              required login fields), and only after a scheduled health check detects an
              expired session — so this flag has no effect when `health_checks` is false. When
              false, expired sessions are marked as `NEEDS_AUTH` instead of attempting
              re-auth. Defaults to true.

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

          health_checks: Whether to enable periodic health checks. When false, the system will not
              automatically verify authentication status, and `auto_reauth` has no effect on
              the automatic flow (since re-auth is only triggered by a failed scheduled health
              check). Defaults to true.

          login_url: Optional login page URL to skip discovery

          proxy: Proxy selection. Provide either id or name. The proxy must be in the same
              project as the resource referencing it. When selecting by name, the name must
              match exactly one active proxy in the project. Ambiguous names return a 400; use
              id for stable references.

          record_session: Whether to record browser sessions for this connection by default. Useful for
              debugging. Can be overridden per-login. Defaults to false.

          save_credentials: Whether to save credentials after every successful login. Defaults to true.
              One-time codes (TOTP, SMS, etc.) are not saved.

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
                    "auto_reauth": auto_reauth,
                    "credential": credential,
                    "health_check_interval": health_check_interval,
                    "health_checks": health_checks,
                    "login_url": login_url,
                    "proxy": proxy,
                    "record_session": record_session,
                    "save_credentials": save_credentials,
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
            path_template("/auth/connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAuth,
        )

    async def update(
        self,
        id: str,
        *,
        allowed_domains: SequenceNotStr[str] | Omit = omit,
        auto_reauth: bool | Omit = omit,
        credential: connection_update_params.Credential | Omit = omit,
        health_check_interval: int | Omit = omit,
        health_checks: bool | Omit = omit,
        login_url: str | Omit = omit,
        proxy: connection_update_params.Proxy | Omit = omit,
        record_session: bool | Omit = omit,
        save_credentials: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAuth:
        """Update an auth connection's configuration.

        Only the fields provided will be
        updated.

        Args:
          allowed_domains: Additional domains valid for this auth flow (replaces existing list)

          auto_reauth: Whether automatic re-authentication is permitted for this connection. This is an
              opt-in flag only — it does not check whether re-auth is actually feasible. Even
              when true, re-auth only runs when the system has what it needs to perform it
              (for example, saved credentials for the required login fields), and only after a
              scheduled health check detects an expired session — so this flag has no effect
              when `health_checks` is false. When false, expired sessions detected by a health
              check are marked as `NEEDS_AUTH` instead of attempting re-auth.

          credential:
              Reference to credentials for the auth connection. Use one of:

              - { name } for Kernel credentials
              - { provider, path } for external provider item
              - { provider, auto: true } for external provider domain lookup

          health_check_interval: Interval in seconds between automatic health checks

          health_checks: Whether periodic health checks are enabled. When set to false, the system will
              not automatically verify authentication status, and `auto_reauth` has no effect
              on the automatic flow (since re-auth is only triggered by a failed scheduled
              health check).

          login_url: Login page URL. Set to empty string to clear.

          proxy: Proxy selection. Provide either id or name. The proxy must be in the same
              project as the resource referencing it. When selecting by name, the name must
              match exactly one active proxy in the project. Ambiguous names return a 400; use
              id for stable references.

          record_session: Whether to record browser sessions for this connection by default

          save_credentials: Whether to save credentials after every successful login

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/auth/connections/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "allowed_domains": allowed_domains,
                    "auto_reauth": auto_reauth,
                    "credential": credential,
                    "health_check_interval": health_check_interval,
                    "health_checks": health_checks,
                    "login_url": login_url,
                    "proxy": proxy,
                    "record_session": record_session,
                    "save_credentials": save_credentials,
                },
                connection_update_params.ConnectionUpdateParams,
            ),
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
        query: str | Omit = omit,
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

          query: Search auth connections by ID, domain, or profile name.

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
                        "query": query,
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
            path_template("/auth/connections/{id}", id=id),
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
            path_template("/auth/connections/{id}/events", id=id),
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
        record_session: bool | Omit = omit,
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
          proxy: Proxy selection. Provide either id or name. The proxy must be in the same
              project as the resource referencing it. When selecting by name, the name must
              match exactly one active proxy in the project. Ambiguous names return a 400; use
              id for stable references.

          record_session: Override the connection's default for recording this login's browser session.
              When omitted, the connection's record_session default is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/auth/connections/{id}/login", id=id),
            body=await async_maybe_transform(
                {
                    "proxy": proxy,
                    "record_session": record_session,
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
        fields: Dict[str, str] | Omit = omit,
        mfa_option_id: str | Omit = omit,
        sign_in_option_id: str | Omit = omit,
        sso_button_selector: str | Omit = omit,
        sso_provider: str | Omit = omit,
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

          mfa_option_id: The MFA method type to select (when mfa_options were returned)

          sign_in_option_id: The sign-in option ID to select (when sign_in_options were returned)

          sso_button_selector: XPath selector for the SSO button to click (ODA). Use sso_provider instead for
              CUA.

          sso_provider: SSO provider to click, matching the provider field from pending_sso_buttons
              (e.g., "google", "github"). Cannot be used with sso_button_selector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/auth/connections/{id}/submit", id=id),
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "mfa_option_id": mfa_option_id,
                    "sign_in_option_id": sign_in_option_id,
                    "sso_button_selector": sso_button_selector,
                    "sso_provider": sso_provider,
                },
                connection_submit_params.ConnectionSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmitFieldsResponse,
        )

    def timeline(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        type: Literal["login", "reauth", "health_check"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ManagedAuthTimelineEvent, AsyncOffsetPagination[ManagedAuthTimelineEvent]]:
        """
        Returns a chronological timeline of events for an auth connection — login
        attempts, automatic re-auth attempts, and health checks. Events are returned
        newest-first.

        Args:
          limit: Maximum number of events to return

          offset: Number of events to skip

          type: Filter the timeline to a single event type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/auth/connections/{id}/timeline", id=id),
            page=AsyncOffsetPagination[ManagedAuthTimelineEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "type": type,
                    },
                    connection_timeline_params.ConnectionTimelineParams,
                ),
            ),
            model=ManagedAuthTimelineEvent,
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
        self.update = to_raw_response_wrapper(
            connections.update,
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
        self.timeline = to_raw_response_wrapper(
            connections.timeline,
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
        self.update = async_to_raw_response_wrapper(
            connections.update,
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
        self.timeline = async_to_raw_response_wrapper(
            connections.timeline,
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
        self.update = to_streamed_response_wrapper(
            connections.update,
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
        self.timeline = to_streamed_response_wrapper(
            connections.timeline,
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
        self.update = async_to_streamed_response_wrapper(
            connections.update,
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
        self.timeline = async_to_streamed_response_wrapper(
            connections.timeline,
        )
