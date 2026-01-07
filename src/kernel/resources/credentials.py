# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import credential_list_params, credential_create_params, credential_update_params
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
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.credential import Credential
from ..types.credential_totp_code_response import CredentialTotpCodeResponse

__all__ = ["CredentialsResource", "AsyncCredentialsResource"]


class CredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return CredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        domain: str,
        name: str,
        values: Dict[str, str],
        sso_provider: str | Omit = omit,
        totp_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Create a new credential for storing login information.

        Args:
          domain: Target domain this credential is for

          name: Unique name for the credential within the organization

          values: Field name to value mapping (e.g., username, password)

          sso_provider: If set, indicates this credential should be used with the specified SSO provider
              (e.g., google, github, microsoft). When the target site has a matching SSO
              button, it will be clicked first before filling credential values on the
              identity provider's login page.

          totp_secret: Base32-encoded TOTP secret for generating one-time passwords. Used for automatic
              2FA during login.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/credentials",
            body=maybe_transform(
                {
                    "domain": domain,
                    "name": name,
                    "values": values,
                    "sso_provider": sso_provider,
                    "totp_secret": totp_secret,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )

    def retrieve(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """Retrieve a credential by its ID or name.

        Credential values are not returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._get(
            f"/credentials/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )

    def update(
        self,
        id_or_name: str,
        *,
        name: str | Omit = omit,
        sso_provider: Optional[str] | Omit = omit,
        totp_secret: str | Omit = omit,
        values: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """Update a credential's name or values.

        When values are provided, they are merged
        with existing values (new keys are added, existing keys are overwritten).

        Args:
          name: New name for the credential

          sso_provider: If set, indicates this credential should be used with the specified SSO
              provider. Set to empty string or null to remove.

          totp_secret: Base32-encoded TOTP secret for generating one-time passwords. Spaces and
              formatting are automatically normalized. Set to empty string to remove.

          values: Field name to value mapping. Values are merged with existing values (new keys
              added, existing keys overwritten).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._patch(
            f"/credentials/{id_or_name}",
            body=maybe_transform(
                {
                    "name": name,
                    "sso_provider": sso_provider,
                    "totp_secret": totp_secret,
                    "values": values,
                },
                credential_update_params.CredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )

    def list(
        self,
        *,
        domain: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[Credential]:
        """List credentials owned by the caller's organization.

        Credential values are not
        returned.

        Args:
          domain: Filter by domain

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/credentials",
            page=SyncOffsetPagination[Credential],
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
                    },
                    credential_list_params.CredentialListParams,
                ),
            ),
            model=Credential,
        )

    def delete(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a credential by its ID or name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/credentials/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def totp_code(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialTotpCodeResponse:
        """
        Returns the current 6-digit TOTP code for a credential with a configured
        totp_secret. Use this to complete 2FA setup on sites or when you need a fresh
        code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._get(
            f"/credentials/{id_or_name}/totp-code",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialTotpCodeResponse,
        )


class AsyncCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        domain: str,
        name: str,
        values: Dict[str, str],
        sso_provider: str | Omit = omit,
        totp_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """
        Create a new credential for storing login information.

        Args:
          domain: Target domain this credential is for

          name: Unique name for the credential within the organization

          values: Field name to value mapping (e.g., username, password)

          sso_provider: If set, indicates this credential should be used with the specified SSO provider
              (e.g., google, github, microsoft). When the target site has a matching SSO
              button, it will be clicked first before filling credential values on the
              identity provider's login page.

          totp_secret: Base32-encoded TOTP secret for generating one-time passwords. Used for automatic
              2FA during login.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/credentials",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "name": name,
                    "values": values,
                    "sso_provider": sso_provider,
                    "totp_secret": totp_secret,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )

    async def retrieve(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """Retrieve a credential by its ID or name.

        Credential values are not returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._get(
            f"/credentials/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )

    async def update(
        self,
        id_or_name: str,
        *,
        name: str | Omit = omit,
        sso_provider: Optional[str] | Omit = omit,
        totp_secret: str | Omit = omit,
        values: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Credential:
        """Update a credential's name or values.

        When values are provided, they are merged
        with existing values (new keys are added, existing keys are overwritten).

        Args:
          name: New name for the credential

          sso_provider: If set, indicates this credential should be used with the specified SSO
              provider. Set to empty string or null to remove.

          totp_secret: Base32-encoded TOTP secret for generating one-time passwords. Spaces and
              formatting are automatically normalized. Set to empty string to remove.

          values: Field name to value mapping. Values are merged with existing values (new keys
              added, existing keys overwritten).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._patch(
            f"/credentials/{id_or_name}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "sso_provider": sso_provider,
                    "totp_secret": totp_secret,
                    "values": values,
                },
                credential_update_params.CredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )

    def list(
        self,
        *,
        domain: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Credential, AsyncOffsetPagination[Credential]]:
        """List credentials owned by the caller's organization.

        Credential values are not
        returned.

        Args:
          domain: Filter by domain

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/credentials",
            page=AsyncOffsetPagination[Credential],
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
                    },
                    credential_list_params.CredentialListParams,
                ),
            ),
            model=Credential,
        )

    async def delete(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a credential by its ID or name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/credentials/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def totp_code(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialTotpCodeResponse:
        """
        Returns the current 6-digit TOTP code for a credential with a configured
        totp_secret. Use this to complete 2FA setup on sites or when you need a fresh
        code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._get(
            f"/credentials/{id_or_name}/totp-code",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialTotpCodeResponse,
        )


class CredentialsResourceWithRawResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.create = to_raw_response_wrapper(
            credentials.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credentials.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credentials.update,
        )
        self.list = to_raw_response_wrapper(
            credentials.list,
        )
        self.delete = to_raw_response_wrapper(
            credentials.delete,
        )
        self.totp_code = to_raw_response_wrapper(
            credentials.totp_code,
        )


class AsyncCredentialsResourceWithRawResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.create = async_to_raw_response_wrapper(
            credentials.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credentials.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credentials.update,
        )
        self.list = async_to_raw_response_wrapper(
            credentials.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credentials.delete,
        )
        self.totp_code = async_to_raw_response_wrapper(
            credentials.totp_code,
        )


class CredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.create = to_streamed_response_wrapper(
            credentials.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credentials.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credentials.update,
        )
        self.list = to_streamed_response_wrapper(
            credentials.list,
        )
        self.delete = to_streamed_response_wrapper(
            credentials.delete,
        )
        self.totp_code = to_streamed_response_wrapper(
            credentials.totp_code,
        )


class AsyncCredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.create = async_to_streamed_response_wrapper(
            credentials.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credentials.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credentials.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credentials.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credentials.delete,
        )
        self.totp_code = async_to_streamed_response_wrapper(
            credentials.totp_code,
        )
