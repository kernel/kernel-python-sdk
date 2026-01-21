# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import credential_provider_create_params, credential_provider_update_params
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
from .._base_client import make_request_options
from ..types.credential_provider import CredentialProvider
from ..types.credential_provider_test_result import CredentialProviderTestResult
from ..types.credential_provider_list_response import CredentialProviderListResponse

__all__ = ["CredentialProvidersResource", "AsyncCredentialProvidersResource"]


class CredentialProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CredentialProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CredentialProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return CredentialProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        token: str,
        provider_type: Literal["onepassword"],
        cache_ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialProvider:
        """
        Configure an external credential provider (e.g., 1Password) for automatic
        credential lookup.

        Args:
          token: Service account token for the provider (e.g., 1Password service account token)

          provider_type: Type of credential provider

          cache_ttl_seconds: How long to cache credential lists (default 300 seconds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/org/credential-providers",
            body=maybe_transform(
                {
                    "token": token,
                    "provider_type": provider_type,
                    "cache_ttl_seconds": cache_ttl_seconds,
                },
                credential_provider_create_params.CredentialProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProvider,
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
    ) -> CredentialProvider:
        """
        Retrieve a credential provider by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/org/credential-providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProvider,
        )

    def update(
        self,
        id: str,
        *,
        token: str | Omit = omit,
        cache_ttl_seconds: int | Omit = omit,
        enabled: bool | Omit = omit,
        priority: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialProvider:
        """
        Update a credential provider's configuration.

        Args:
          token: New service account token (to rotate credentials)

          cache_ttl_seconds: How long to cache credential lists

          enabled: Whether the provider is enabled for credential lookups

          priority: Priority order for credential lookups (lower numbers are checked first)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/org/credential-providers/{id}",
            body=maybe_transform(
                {
                    "token": token,
                    "cache_ttl_seconds": cache_ttl_seconds,
                    "enabled": enabled,
                    "priority": priority,
                },
                credential_provider_update_params.CredentialProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProvider,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialProviderListResponse:
        """List external credential providers configured for the organization."""
        return self._get(
            "/org/credential-providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProviderListResponse,
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
        """
        Delete a credential provider by its ID.

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
            f"/org/credential-providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def test(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialProviderTestResult:
        """
        Validate the credential provider's token and list accessible vaults.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/org/credential-providers/{id}/test",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProviderTestResult,
        )


class AsyncCredentialProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCredentialProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncCredentialProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        token: str,
        provider_type: Literal["onepassword"],
        cache_ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialProvider:
        """
        Configure an external credential provider (e.g., 1Password) for automatic
        credential lookup.

        Args:
          token: Service account token for the provider (e.g., 1Password service account token)

          provider_type: Type of credential provider

          cache_ttl_seconds: How long to cache credential lists (default 300 seconds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/org/credential-providers",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "provider_type": provider_type,
                    "cache_ttl_seconds": cache_ttl_seconds,
                },
                credential_provider_create_params.CredentialProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProvider,
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
    ) -> CredentialProvider:
        """
        Retrieve a credential provider by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/org/credential-providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProvider,
        )

    async def update(
        self,
        id: str,
        *,
        token: str | Omit = omit,
        cache_ttl_seconds: int | Omit = omit,
        enabled: bool | Omit = omit,
        priority: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialProvider:
        """
        Update a credential provider's configuration.

        Args:
          token: New service account token (to rotate credentials)

          cache_ttl_seconds: How long to cache credential lists

          enabled: Whether the provider is enabled for credential lookups

          priority: Priority order for credential lookups (lower numbers are checked first)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/org/credential-providers/{id}",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "cache_ttl_seconds": cache_ttl_seconds,
                    "enabled": enabled,
                    "priority": priority,
                },
                credential_provider_update_params.CredentialProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProvider,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialProviderListResponse:
        """List external credential providers configured for the organization."""
        return await self._get(
            "/org/credential-providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProviderListResponse,
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
        """
        Delete a credential provider by its ID.

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
            f"/org/credential-providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def test(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialProviderTestResult:
        """
        Validate the credential provider's token and list accessible vaults.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/org/credential-providers/{id}/test",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialProviderTestResult,
        )


class CredentialProvidersResourceWithRawResponse:
    def __init__(self, credential_providers: CredentialProvidersResource) -> None:
        self._credential_providers = credential_providers

        self.create = to_raw_response_wrapper(
            credential_providers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credential_providers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credential_providers.update,
        )
        self.list = to_raw_response_wrapper(
            credential_providers.list,
        )
        self.delete = to_raw_response_wrapper(
            credential_providers.delete,
        )
        self.test = to_raw_response_wrapper(
            credential_providers.test,
        )


class AsyncCredentialProvidersResourceWithRawResponse:
    def __init__(self, credential_providers: AsyncCredentialProvidersResource) -> None:
        self._credential_providers = credential_providers

        self.create = async_to_raw_response_wrapper(
            credential_providers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credential_providers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credential_providers.update,
        )
        self.list = async_to_raw_response_wrapper(
            credential_providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credential_providers.delete,
        )
        self.test = async_to_raw_response_wrapper(
            credential_providers.test,
        )


class CredentialProvidersResourceWithStreamingResponse:
    def __init__(self, credential_providers: CredentialProvidersResource) -> None:
        self._credential_providers = credential_providers

        self.create = to_streamed_response_wrapper(
            credential_providers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credential_providers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credential_providers.update,
        )
        self.list = to_streamed_response_wrapper(
            credential_providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            credential_providers.delete,
        )
        self.test = to_streamed_response_wrapper(
            credential_providers.test,
        )


class AsyncCredentialProvidersResourceWithStreamingResponse:
    def __init__(self, credential_providers: AsyncCredentialProvidersResource) -> None:
        self._credential_providers = credential_providers

        self.create = async_to_streamed_response_wrapper(
            credential_providers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credential_providers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credential_providers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credential_providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credential_providers.delete,
        )
        self.test = async_to_streamed_response_wrapper(
            credential_providers.test,
        )
