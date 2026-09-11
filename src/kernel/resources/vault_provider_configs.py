# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal, overload

import httpx

from ..types import (
    vault_provider_config_list_params,
    vault_provider_config_create_params,
    vault_provider_config_update_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
from ..types.vault_provider_config import VaultProviderConfig

__all__ = ["VaultProviderConfigsResource", "AsyncVaultProviderConfigsResource"]


class VaultProviderConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VaultProviderConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return VaultProviderConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VaultProviderConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return VaultProviderConfigsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        credentials: vault_provider_config_create_params.VaultLinkProviderConfigRequestCredentials,
        name: str,
        provider: Literal["link"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultProviderConfig:
        """Register a configuration shared across the organization's projects.

        Names are
        unique within the organization; duplicate names return 409 without replacing
        credentials. A configuration serves many wallets. Secret credentials are never
        returned. Requires an organization-scoped credential or dashboard
        authentication; project-scoped credentials receive 403.

        Args:
          name: Unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        credentials: vault_provider_config_create_params.VaultAgentCardProviderConfigRequestCredentials,
        name: str,
        provider: Literal["agentcard"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultProviderConfig:
        """Register a configuration shared across the organization's projects.

        Names are
        unique within the organization; duplicate names return 409 without replacing
        credentials. A configuration serves many wallets. Secret credentials are never
        returned. Requires an organization-scoped credential or dashboard
        authentication; project-scoped credentials receive 403.

        Args:
          name: Unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["credentials", "name", "provider"])
    def create(
        self,
        *,
        credentials: vault_provider_config_create_params.VaultLinkProviderConfigRequestCredentials
        | vault_provider_config_create_params.VaultAgentCardProviderConfigRequestCredentials,
        name: str,
        provider: Literal["link"] | Literal["agentcard"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultProviderConfig:
        return cast(
            VaultProviderConfig,
            self._post(
                "/vault-provider-configs",
                body=maybe_transform(
                    {
                        "credentials": credentials,
                        "name": name,
                        "provider": provider,
                    },
                    vault_provider_config_create_params.VaultProviderConfigCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VaultProviderConfig
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> VaultProviderConfig:
        """Look up a configuration by ID or name.

        Returns 404 when it does not exist in the
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return cast(
            VaultProviderConfig,
            self._get(
                path_template("/vault-provider-configs/{id_or_name}", id_or_name=id_or_name),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VaultProviderConfig
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        id_or_name: str,
        *,
        credentials: vault_provider_config_update_params.Credentials | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultProviderConfig:
        """Update the supplied fields; omitted fields remain unchanged.

        Names must remain
        unique within the organization. Requires an organization-scoped credential or
        dashboard authentication; project-scoped credentials receive 403.

        Args:
          credentials: Fields to update. Omitted credentials are left unchanged. A rejected update
              leaves existing credentials unchanged.

          name: Unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return cast(
            VaultProviderConfig,
            self._patch(
                path_template("/vault-provider-configs/{id_or_name}", id_or_name=id_or_name),
                body=maybe_transform(
                    {
                        "credentials": credentials,
                        "name": name,
                    },
                    vault_provider_config_update_params.VaultProviderConfigUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VaultProviderConfig
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[VaultProviderConfig]:
        """
        Secret credentials are never returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/vault-provider-configs",
            page=SyncOffsetPagination[VaultProviderConfig],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    vault_provider_config_list_params.VaultProviderConfigListParams,
                ),
            ),
            model=cast(Any, VaultProviderConfig),  # Union types cannot be passed in as arguments in the type system
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
        """Delete a configuration in the organization.

        Returns 409 while any non-deleted
        vault item references the configuration, regardless of connection status. Does
        not delete the external OAuth client or revoke unrelated grants. Requires an
        organization-scoped credential or dashboard authentication; project-scoped
        credentials receive 403.

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
            path_template("/vault-provider-configs/{id_or_name}", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncVaultProviderConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVaultProviderConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVaultProviderConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVaultProviderConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncVaultProviderConfigsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        credentials: vault_provider_config_create_params.VaultLinkProviderConfigRequestCredentials,
        name: str,
        provider: Literal["link"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultProviderConfig:
        """Register a configuration shared across the organization's projects.

        Names are
        unique within the organization; duplicate names return 409 without replacing
        credentials. A configuration serves many wallets. Secret credentials are never
        returned. Requires an organization-scoped credential or dashboard
        authentication; project-scoped credentials receive 403.

        Args:
          name: Unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        credentials: vault_provider_config_create_params.VaultAgentCardProviderConfigRequestCredentials,
        name: str,
        provider: Literal["agentcard"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultProviderConfig:
        """Register a configuration shared across the organization's projects.

        Names are
        unique within the organization; duplicate names return 409 without replacing
        credentials. A configuration serves many wallets. Secret credentials are never
        returned. Requires an organization-scoped credential or dashboard
        authentication; project-scoped credentials receive 403.

        Args:
          name: Unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["credentials", "name", "provider"])
    async def create(
        self,
        *,
        credentials: vault_provider_config_create_params.VaultLinkProviderConfigRequestCredentials
        | vault_provider_config_create_params.VaultAgentCardProviderConfigRequestCredentials,
        name: str,
        provider: Literal["link"] | Literal["agentcard"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultProviderConfig:
        return cast(
            VaultProviderConfig,
            await self._post(
                "/vault-provider-configs",
                body=await async_maybe_transform(
                    {
                        "credentials": credentials,
                        "name": name,
                        "provider": provider,
                    },
                    vault_provider_config_create_params.VaultProviderConfigCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VaultProviderConfig
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> VaultProviderConfig:
        """Look up a configuration by ID or name.

        Returns 404 when it does not exist in the
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return cast(
            VaultProviderConfig,
            await self._get(
                path_template("/vault-provider-configs/{id_or_name}", id_or_name=id_or_name),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VaultProviderConfig
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        id_or_name: str,
        *,
        credentials: vault_provider_config_update_params.Credentials | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultProviderConfig:
        """Update the supplied fields; omitted fields remain unchanged.

        Names must remain
        unique within the organization. Requires an organization-scoped credential or
        dashboard authentication; project-scoped credentials receive 403.

        Args:
          credentials: Fields to update. Omitted credentials are left unchanged. A rejected update
              leaves existing credentials unchanged.

          name: Unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return cast(
            VaultProviderConfig,
            await self._patch(
                path_template("/vault-provider-configs/{id_or_name}", id_or_name=id_or_name),
                body=await async_maybe_transform(
                    {
                        "credentials": credentials,
                        "name": name,
                    },
                    vault_provider_config_update_params.VaultProviderConfigUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VaultProviderConfig
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VaultProviderConfig, AsyncOffsetPagination[VaultProviderConfig]]:
        """
        Secret credentials are never returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/vault-provider-configs",
            page=AsyncOffsetPagination[VaultProviderConfig],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    vault_provider_config_list_params.VaultProviderConfigListParams,
                ),
            ),
            model=cast(Any, VaultProviderConfig),  # Union types cannot be passed in as arguments in the type system
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
        """Delete a configuration in the organization.

        Returns 409 while any non-deleted
        vault item references the configuration, regardless of connection status. Does
        not delete the external OAuth client or revoke unrelated grants. Requires an
        organization-scoped credential or dashboard authentication; project-scoped
        credentials receive 403.

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
            path_template("/vault-provider-configs/{id_or_name}", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class VaultProviderConfigsResourceWithRawResponse:
    def __init__(self, vault_provider_configs: VaultProviderConfigsResource) -> None:
        self._vault_provider_configs = vault_provider_configs

        self.create = to_raw_response_wrapper(
            vault_provider_configs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vault_provider_configs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vault_provider_configs.update,
        )
        self.list = to_raw_response_wrapper(
            vault_provider_configs.list,
        )
        self.delete = to_raw_response_wrapper(
            vault_provider_configs.delete,
        )


class AsyncVaultProviderConfigsResourceWithRawResponse:
    def __init__(self, vault_provider_configs: AsyncVaultProviderConfigsResource) -> None:
        self._vault_provider_configs = vault_provider_configs

        self.create = async_to_raw_response_wrapper(
            vault_provider_configs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vault_provider_configs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vault_provider_configs.update,
        )
        self.list = async_to_raw_response_wrapper(
            vault_provider_configs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vault_provider_configs.delete,
        )


class VaultProviderConfigsResourceWithStreamingResponse:
    def __init__(self, vault_provider_configs: VaultProviderConfigsResource) -> None:
        self._vault_provider_configs = vault_provider_configs

        self.create = to_streamed_response_wrapper(
            vault_provider_configs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vault_provider_configs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vault_provider_configs.update,
        )
        self.list = to_streamed_response_wrapper(
            vault_provider_configs.list,
        )
        self.delete = to_streamed_response_wrapper(
            vault_provider_configs.delete,
        )


class AsyncVaultProviderConfigsResourceWithStreamingResponse:
    def __init__(self, vault_provider_configs: AsyncVaultProviderConfigsResource) -> None:
        self._vault_provider_configs = vault_provider_configs

        self.create = async_to_streamed_response_wrapper(
            vault_provider_configs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vault_provider_configs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vault_provider_configs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vault_provider_configs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vault_provider_configs.delete,
        )
