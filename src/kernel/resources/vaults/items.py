# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.vaults import (
    item_events_params,
    item_update_params,
    item_upsert_params,
    item_retrieve_params,
    item_perform_operation_params,
)
from ...types.vaults.vault_item import VaultItem
from ...types.vaults.item_list_response import ItemListResponse
from ...types.vaults.item_events_response import ItemEventsResponse
from ...types.vaults.card_vault_item_spec_param import CardVaultItemSpecParam

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        key: str,
        *,
        id_or_name: str,
        expand: List[Literal["payment_methods"]] | Omit = omit,
        wait: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """
        The response advertises operations that are valid in the item's current state
        and live data that can be requested through `expand`. Read each operation's
        description before using it. Expanded data is fetched from the provider and is
        not persisted in the vault item. Requesting an unavailable expansion returns 409
        instead of a partial item.

        Args:
          expand: Live fields advertised by `available_expansions` to include in `expanded`.

          wait: Hold for up to this many seconds while the item is pending authorization or
              approval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            self._get(
                path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "expand": expand,
                            "wait": wait,
                        },
                        item_retrieve_params.ItemRetrieveParams,
                    ),
                ),
                cast_to=cast(Any, VaultItem),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CardVaultItemSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """Requested cards accept a replacement specification.

        Pending issuance requests
        may update provider-supported fields on their existing request, subject to
        atomic provider approval checks; omitted optional fields remain unchanged and
        explicit empty lists clear them. Wallet/provider binding and unsupported fields
        cannot change after authorization starts. An uncertain update enters
        recovery_required and must not be retried. Checkout cards may be edited between
        authorizations.

        Args:
          spec: Live payment card. Test-mode card creation is not supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            self._patch(
                path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
                body=maybe_transform({"spec": spec}, item_update_params.ItemUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, VaultItem),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemListResponse:
        """
        List vault items without secret values

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._get(
            path_template("/vaults/{id_or_name}/items", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemListResponse,
        )

    def delete(
        self,
        key: str,
        *,
        id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unresolved payment operations block deletion, including operations on child
        cards of a wallet. Reconcile the original attempt with the provider or support
        first; deleting or recreating an item is not proof that a payment did not occur.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def events(
        self,
        key: str,
        *,
        id_or_name: str,
        after: str | Omit = omit,
        wait: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemEventsResponse:
        """
        List immutable audit events for a vault item

        Args:
          after: Return events after this event ID.

          wait: Long-poll for new events for up to this many seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            path_template("/vaults/{id_or_name}/items/{key}/events", id_or_name=id_or_name, key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "wait": wait,
                    },
                    item_events_params.ItemEventsParams,
                ),
            ),
            cast_to=ItemEventsResponse,
        )

    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["authorize"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Operations
        may call an external provider and return updated state. Link cards advertise
        authorize. AgentCard cards are created with PUT and request approval when their
        aliases are used at checkout; they do not expose this operation. If
        spend-request creation is rate limited, returns HTTP 429 with code
        `spend_request_rate_limited`; stop and back off before retrying.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            self._post(
                path_template("/vaults/{id_or_name}/items/{key}/operations", id_or_name=id_or_name, key=key),
                body=maybe_transform({"type": type}, item_perform_operation_params.ItemPerformOperationParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, VaultItem),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: item_upsert_params.WalletVaultItemRequestSpec,
        type: Literal["wallet"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema.

        Args:
          spec: AgentCard wallet. Omit provider_config to use Kernel-managed credentials, or
              select a customer-owned configuration. Mode (sandbox vs live) is determined by
              the selected credential; there is no per-item test flag. Without user_id,
              creation returns a hosted enrollment action and Kernel polls until the user
              connects. user_id may only reference a user already enrolled by a wallet in this
              organization under the same configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CardVaultItemSpecParam,
        type: Literal["card"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema.

        Args:
          spec: Live payment card. Test-mode card creation is not supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["id_or_name", "spec", "type"])
    def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: item_upsert_params.WalletVaultItemRequestSpec | CardVaultItemSpecParam,
        type: Literal["wallet"] | Literal["card"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            self._put(
                path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
                body=maybe_transform(
                    {
                        "spec": spec,
                        "type": type,
                    },
                    item_upsert_params.ItemUpsertParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, VaultItem),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        key: str,
        *,
        id_or_name: str,
        expand: List[Literal["payment_methods"]] | Omit = omit,
        wait: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """
        The response advertises operations that are valid in the item's current state
        and live data that can be requested through `expand`. Read each operation's
        description before using it. Expanded data is fetched from the provider and is
        not persisted in the vault item. Requesting an unavailable expansion returns 409
        instead of a partial item.

        Args:
          expand: Live fields advertised by `available_expansions` to include in `expanded`.

          wait: Hold for up to this many seconds while the item is pending authorization or
              approval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            await self._get(
                path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "expand": expand,
                            "wait": wait,
                        },
                        item_retrieve_params.ItemRetrieveParams,
                    ),
                ),
                cast_to=cast(Any, VaultItem),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CardVaultItemSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """Requested cards accept a replacement specification.

        Pending issuance requests
        may update provider-supported fields on their existing request, subject to
        atomic provider approval checks; omitted optional fields remain unchanged and
        explicit empty lists clear them. Wallet/provider binding and unsupported fields
        cannot change after authorization starts. An uncertain update enters
        recovery_required and must not be retried. Checkout cards may be edited between
        authorizations.

        Args:
          spec: Live payment card. Test-mode card creation is not supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            await self._patch(
                path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
                body=await async_maybe_transform({"spec": spec}, item_update_params.ItemUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, VaultItem),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemListResponse:
        """
        List vault items without secret values

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._get(
            path_template("/vaults/{id_or_name}/items", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemListResponse,
        )

    async def delete(
        self,
        key: str,
        *,
        id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unresolved payment operations block deletion, including operations on child
        cards of a wallet. Reconcile the original attempt with the provider or support
        first; deleting or recreating an item is not proof that a payment did not occur.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def events(
        self,
        key: str,
        *,
        id_or_name: str,
        after: str | Omit = omit,
        wait: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemEventsResponse:
        """
        List immutable audit events for a vault item

        Args:
          after: Return events after this event ID.

          wait: Long-poll for new events for up to this many seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            path_template("/vaults/{id_or_name}/items/{key}/events", id_or_name=id_or_name, key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "wait": wait,
                    },
                    item_events_params.ItemEventsParams,
                ),
            ),
            cast_to=ItemEventsResponse,
        )

    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["authorize"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Operations
        may call an external provider and return updated state. Link cards advertise
        authorize. AgentCard cards are created with PUT and request approval when their
        aliases are used at checkout; they do not expose this operation. If
        spend-request creation is rate limited, returns HTTP 429 with code
        `spend_request_rate_limited`; stop and back off before retrying.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            await self._post(
                path_template("/vaults/{id_or_name}/items/{key}/operations", id_or_name=id_or_name, key=key),
                body=await async_maybe_transform(
                    {"type": type}, item_perform_operation_params.ItemPerformOperationParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, VaultItem),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: item_upsert_params.WalletVaultItemRequestSpec,
        type: Literal["wallet"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema.

        Args:
          spec: AgentCard wallet. Omit provider_config to use Kernel-managed credentials, or
              select a customer-owned configuration. Mode (sandbox vs live) is determined by
              the selected credential; there is no per-item test flag. Without user_id,
              creation returns a hosted enrollment action and Kernel polls until the user
              connects. user_id may only reference a user already enrolled by a wallet in this
              organization under the same configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CardVaultItemSpecParam,
        type: Literal["card"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema.

        Args:
          spec: Live payment card. Test-mode card creation is not supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["id_or_name", "spec", "type"])
    async def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: item_upsert_params.WalletVaultItemRequestSpec | CardVaultItemSpecParam,
        type: Literal["wallet"] | Literal["card"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultItem:
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            await self._put(
                path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
                body=await async_maybe_transform(
                    {
                        "spec": spec,
                        "type": type,
                    },
                    item_upsert_params.ItemUpsertParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, VaultItem),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.retrieve = to_raw_response_wrapper(
            items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            items.update,
        )
        self.list = to_raw_response_wrapper(
            items.list,
        )
        self.delete = to_raw_response_wrapper(
            items.delete,
        )
        self.events = to_raw_response_wrapper(
            items.events,
        )
        self.perform_operation = to_raw_response_wrapper(
            items.perform_operation,
        )
        self.upsert = to_raw_response_wrapper(
            items.upsert,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.retrieve = async_to_raw_response_wrapper(
            items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            items.update,
        )
        self.list = async_to_raw_response_wrapper(
            items.list,
        )
        self.delete = async_to_raw_response_wrapper(
            items.delete,
        )
        self.events = async_to_raw_response_wrapper(
            items.events,
        )
        self.perform_operation = async_to_raw_response_wrapper(
            items.perform_operation,
        )
        self.upsert = async_to_raw_response_wrapper(
            items.upsert,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.retrieve = to_streamed_response_wrapper(
            items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            items.update,
        )
        self.list = to_streamed_response_wrapper(
            items.list,
        )
        self.delete = to_streamed_response_wrapper(
            items.delete,
        )
        self.events = to_streamed_response_wrapper(
            items.events,
        )
        self.perform_operation = to_streamed_response_wrapper(
            items.perform_operation,
        )
        self.upsert = to_streamed_response_wrapper(
            items.upsert,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.retrieve = async_to_streamed_response_wrapper(
            items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            items.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            items.delete,
        )
        self.events = async_to_streamed_response_wrapper(
            items.events,
        )
        self.perform_operation = async_to_streamed_response_wrapper(
            items.perform_operation,
        )
        self.upsert = async_to_streamed_response_wrapper(
            items.upsert,
        )
