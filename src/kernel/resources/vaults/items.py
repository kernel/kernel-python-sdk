# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, cast
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.vaults.vault_fill_field_param import VaultFillFieldParam
from ...types.vaults.card_vault_item_spec_param import CardVaultItemSpecParam
from ...types.vaults.vault_webmcp_binding_param import VaultWebmcpBindingParam
from ...types.vaults.vault_checkout_context_param import VaultCheckoutContextParam
from ...types.vaults.vault_item_operation_response import VaultItemOperationResponse
from ...types.vaults.payment_request_vault_item_spec_param import PaymentRequestVaultItemSpecParam
from ...types.vaults.credential_vault_item_spec_input_param import CredentialVaultItemSpecInputParam
from ...types.vaults.credential_vault_item_spec_update_param import CredentialVaultItemSpecUpdateParam
from ...types.vaults.one_password_credential_account_spec_param import OnePasswordCredentialAccountSpecParam

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
        expand: List[Literal["payment_methods", "link_user_info", "link_shipping_addresses"]] | Omit = omit,
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
        instead of a partial item. Pending credential items return a collection action.
        Kernel-hosted active collection links are renewed atomically on expiry for ready
        or pending items without changing the item version. Invoke collect to open a
        form for a ready item without clearing values. Sensitive credential values are
        never returned.

        Args:
          expand: Live fields advertised by `available_expansions` to include in `expanded`.

          wait: Hold for up to this many seconds while the item is pending authorization,
              approval, or credential collection. Return the current item when ready or when
              the wait elapses. This does not wait for edits to an already-ready credential;
              poll GET without wait and compare version to observe changes after collect.
              Managed auth credentials are created ready, so wait returns immediately.

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

    @overload
    def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CardVaultItemSpecParam,
        type: Literal["card"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Credential updates require type credential and the current version, and change
        only values or description; omitted values are preserved, nonempty strings
        replace, and null or empty strings clear supported fields. Clearing required
        text/email/password values returns pending_collection; browser forms still
        require nonempty required inputs. Card updates may omit type for compatibility
        with legacy requests. Requested cards accept a replacement specification.
        Pending issuance requests may update provider-supported fields on their existing
        request, subject to atomic provider approval checks; omitted optional fields
        remain unchanged and explicit empty lists clear them. Wallet/provider binding
        and unsupported fields cannot change after authorization starts. An uncertain
        update enters recovery_required; delete the card and create a new one rather
        than retrying the update. Checkout cards may be edited between authorizations. A
        Link card authorized with browser_id and page_url cannot be changed; delete it
        and create a new card with the updated details.

        Args:
          spec: Live Link card request. Test-mode card creation is not supported. The spec can
              be changed with PATCH until the card is authorized at a checkout. Authorize it
              with the browser at final checkout: Kernel inspects the checkout through WebMCP
              and internally chooses a merchant-bound Link Pay Token when supported or a
              virtual card otherwise. Callers never receive or choose how the credential is
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: PaymentRequestVaultItemSpecParam,
        type: Literal["payment_request"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Credential updates require type credential and the current version, and change
        only values or description; omitted values are preserved, nonempty strings
        replace, and null or empty strings clear supported fields. Clearing required
        text/email/password values returns pending_collection; browser forms still
        require nonempty required inputs. Card updates may omit type for compatibility
        with legacy requests. Requested cards accept a replacement specification.
        Pending issuance requests may update provider-supported fields on their existing
        request, subject to atomic provider approval checks; omitted optional fields
        remain unchanged and explicit empty lists clear them. Wallet/provider binding
        and unsupported fields cannot change after authorization starts. An uncertain
        update enters recovery_required; delete the card and create a new one rather
        than retrying the update. Checkout cards may be edited between authorizations. A
        Link card authorized with browser_id and page_url cannot be changed; delete it
        and create a new card with the updated details.

        Args:
          spec: Live Link card request. Test-mode card creation is not supported. The spec can
              be changed with PATCH until the card is authorized at a checkout. Authorize it
              with the browser at final checkout: Kernel inspects the checkout through WebMCP
              and internally chooses a merchant-bound Link Pay Token when supported or a
              virtual card otherwise. Callers never receive or choose how the credential is
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CredentialVaultItemSpecUpdateParam,
        type: Literal["credential"],
        version: int,
        expected_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Credential updates require type credential and the current version, and change
        only values or description; omitted values are preserved, nonempty strings
        replace, and null or empty strings clear supported fields. Clearing required
        text/email/password values returns pending_collection; browser forms still
        require nonempty required inputs. Card updates may omit type for compatibility
        with legacy requests. Requested cards accept a replacement specification.
        Pending issuance requests may update provider-supported fields on their existing
        request, subject to atomic provider approval checks; omitted optional fields
        remain unchanged and explicit empty lists clear them. Wallet/provider binding
        and unsupported fields cannot change after authorization starts. An uncertain
        update enters recovery_required; delete the card and create a new one rather
        than retrying the update. Checkout cards may be edited between authorizations. A
        Link card authorized with browser_id and page_url cannot be changed; delete it
        and create a new card with the updated details.

        Args:
          version: Expected current item version from the latest read.

          expected_item_id: Optional immutable item ID precondition. Returns 409 if the key now identifies a
              different item. Accepted writes target this immutable ID, preventing
              replacement-key races. Supply this when submitting a form bound to a previously
              read item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["id_or_name", "spec"], ["id_or_name", "spec", "type"], ["id_or_name", "spec", "type", "version"])
    def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CardVaultItemSpecParam | PaymentRequestVaultItemSpecParam | CredentialVaultItemSpecUpdateParam,
        type: Literal["card"] | Literal["payment_request"] | Literal["credential"] | Omit = omit,
        version: int | Omit = omit,
        expected_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            self._patch(
                path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
                body=maybe_transform(
                    {
                        "spec": spec,
                        "type": type,
                        "version": version,
                        "expected_item_id": expected_item_id,
                    },
                    item_update_params.ItemUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
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
        """Credential entries include safe field metadata and non-sensitive values.

        Listing
        never creates or renews collection sessions; only an existing unexpired active
        session is included. Use single-item GET or collect to obtain a fresh link.

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
        idempotency_key: str | None = None,
    ) -> None:
        """
        Unresolved payment operations normally block deletion, including operations on
        child cards of a wallet. Deleting a connected Kernel wallet first blocks new
        payments on it, then removes its enrolled card. If that fails, the wallet is
        kept and keeps refusing payments; retry the deletion. A Link or Kernel card in
        recovery_required for issuance, or an AgentCard card in recovery_required whose
        checkout create response returned no authorization ID, may be explicitly
        abandoned by deleting that card directly; deleting its wallet or vault remains
        blocked until the card is deleted. Deleting or recreating an item is not proof
        that a payment did not occur. Deleting a managed auth credential item leaves the
        connection and its saved credential unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["authorize"],
        browser_id: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name. The browser must have this
              vault attached.

          page_url: Exact current top-level URL of the final checkout page open in browser_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["restart_verification"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        amount: int,
        currency: str,
        occurred_at: Union[str, datetime],
        status: Literal["APPROVED", "DECLINED", "PENDING", "ERROR", "CANCELLED"],
        transaction_type: Literal[
            "PURCHASE", "AUTHORIZATION", "CAPTURE", "REFUND", "REVERSAL", "VERIFICATION", "CHARGEBACK", "FRAUD"
        ],
        type: Literal["confirm_transaction"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          amount: Actual transaction amount in minor units, no greater than the approved limit.

          currency: Must match the approved purchase currency.

          occurred_at: Time the merchant outcome was observed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["collect"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        checkout: VaultCheckoutContextParam,
        type: Literal["prepare_checkout"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          checkout: Required when preparing an unused AgentCard card for a supported checkout
              processor. Consent is bound to this browser and declared merchant origin, not a
              tab. Wait for the item's ready_to_submit status before native Pay and submit
              within its readiness deadline. Unused preparations expire automatically; every
              preparation is single-use, including after failure or expiry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        type: Literal["fill"],
        fields: Iterable[VaultFillFieldParam] | Omit = omit,
        page_url: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          fields: Field bindings, when the item's advertised fill operation requires them. Each
              selector is searched in the main frame and all descendant frames and must
              resolve to exactly one editable input or select, matched directly or through a
              containing element; zero or multiple candidates fail, and no two bindings may
              resolve to the same element. Select elements match an option by value, not
              label. All bindings are validated before any write, then filled in request
              order, stopping at the first failure. If the page navigates or a target
              disappears, fill stops rather than choosing another page or element.

          page_url: Exact current top-level page URL, including path, query, and fragment. Must
              match exactly one open page in the browser; zero or multiple matches fail. No
              prefix or glob matching. When an item allows omitting it, the browser must have
              exactly one open page.

          timeout_ms: Ignored. Fill sets no operation deadline; typing pace adapts to the length of
              the values instead. Accepted for compatibility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        type: Literal["arm_passkey"],
        field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          field: Passkey field to arm. Required when more than one passkey field holds a passkey.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        type: Literal["register_passkey"],
        field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          field: Empty passkey field to store the new passkey in. Required when more than one
              passkey field is empty.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        type: Literal["disarm_passkey"],
        field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          field: Limit disarming to one passkey field. Omit to disarm every passkey field of the
              item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["1pw_create_access_request"],
        goal: str | Omit = omit,
        keywords: SequenceNotStr[str] | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["1pw_access_request_status"],
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        page_url: str,
        type: Literal["1pw_fill"],
        entry_id: str | Omit = omit,
        target_id: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          page_url: Exact current top-level page URL. Must match exactly one open page in the
              browser unless target_id is supplied.

          entry_id: ID of an approved request entry. Required when several approved entries have the
              page's origin.

          target_id: CDP target ID of the page to fill, such as tab.target_id from
              playwright.execute. Use it when several open pages have page_url. The page's
              current URL must equal page_url. Kernel brings the page to the front of its
              window before filling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["1pw_recover"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        access_token: str,
        type: Literal["1pw_update_access_token"],
        access_token_expires_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          access_token_expires_at: Optional supplied expiry. Omit to clear the old expiry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        bindings: Iterable[VaultWebmcpBindingParam],
        browser_id: str,
        input: Dict[str, object],
        page_url: str,
        tool_ref: str,
        type: Literal["webmcp_invoke"],
        timeout_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          input: Public tool arguments with an existing null slot at each binding path. At most
              64 KiB after JSON serialization, including substituted values. Never include
              vault values here.

          page_url: Exact top-level URL from the discovered tool source (fragment omitted). This
              pins the target page; it does not authorize a destination.

          tool_ref: Opaque reference to the exact live WebMCP registration.

          timeout_sec: Tool invocation timeout in seconds; preflight and response handling have an
              additional bounded allowance. An indeterminate outcome is not retried.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["add_payment_method"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        payment_method_id: str,
        type: Literal["remove_payment_method"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          payment_method_id: ID from the wallet's payment_methods expansion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(
        ["id_or_name", "type"],
        ["id_or_name", "amount", "currency", "occurred_at", "status", "transaction_type", "type"],
        ["id_or_name", "checkout", "type"],
        ["id_or_name", "browser_id", "type"],
        ["id_or_name", "browser_id", "page_url", "type"],
        ["id_or_name", "access_token", "type"],
        ["id_or_name", "bindings", "browser_id", "input", "page_url", "tool_ref", "type"],
        ["id_or_name", "payment_method_id", "type"],
    )
    def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["authorize"]
        | Literal["restart_verification"]
        | Literal["confirm_transaction"]
        | Literal["collect"]
        | Literal["prepare_checkout"]
        | Literal["fill"]
        | Literal["arm_passkey"]
        | Literal["register_passkey"]
        | Literal["disarm_passkey"]
        | Literal["1pw_create_access_request"]
        | Literal["1pw_access_request_status"]
        | Literal["1pw_fill"]
        | Literal["1pw_recover"]
        | Literal["1pw_update_access_token"]
        | Literal["webmcp_invoke"]
        | Literal["add_payment_method"]
        | Literal["remove_payment_method"],
        browser_id: str | Omit = omit,
        page_url: str | Omit = omit,
        amount: int | Omit = omit,
        currency: str | Omit = omit,
        occurred_at: Union[str, datetime] | Omit = omit,
        status: Literal["APPROVED", "DECLINED", "PENDING", "ERROR", "CANCELLED"] | Omit = omit,
        transaction_type: Literal[
            "PURCHASE", "AUTHORIZATION", "CAPTURE", "REFUND", "REVERSAL", "VERIFICATION", "CHARGEBACK", "FRAUD"
        ]
        | Omit = omit,
        checkout: VaultCheckoutContextParam | Omit = omit,
        fields: Iterable[VaultFillFieldParam] | Omit = omit,
        timeout_ms: int | Omit = omit,
        field: str | Omit = omit,
        goal: str | Omit = omit,
        keywords: SequenceNotStr[str] | Omit = omit,
        reason: str | Omit = omit,
        timeout_seconds: int | Omit = omit,
        entry_id: str | Omit = omit,
        target_id: str | Omit = omit,
        access_token: str | Omit = omit,
        access_token_expires_at: Union[str, datetime] | Omit = omit,
        bindings: Iterable[VaultWebmcpBindingParam] | Omit = omit,
        input: Dict[str, object] | Omit = omit,
        tool_ref: str | Omit = omit,
        timeout_sec: int | Omit = omit,
        payment_method_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItemOperationResponse,
            self._client.with_options(max_retries=0).post(
                path_template("/vaults/{id_or_name}/items/{key}/operations", id_or_name=id_or_name, key=key),
                body=maybe_transform(
                    {
                        "type": type,
                        "browser_id": browser_id,
                        "page_url": page_url,
                        "amount": amount,
                        "currency": currency,
                        "occurred_at": occurred_at,
                        "status": status,
                        "transaction_type": transaction_type,
                        "checkout": checkout,
                        "fields": fields,
                        "timeout_ms": timeout_ms,
                        "field": field,
                        "goal": goal,
                        "keywords": keywords,
                        "reason": reason,
                        "timeout_seconds": timeout_seconds,
                        "entry_id": entry_id,
                        "target_id": target_id,
                        "access_token": access_token,
                        "access_token_expires_at": access_token_expires_at,
                        "bindings": bindings,
                        "input": input,
                        "tool_ref": tool_ref,
                        "timeout_sec": timeout_sec,
                        "payment_method_id": payment_method_id,
                    },
                    item_perform_operation_params.ItemPerformOperationParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, VaultItemOperationResponse
                ),  # Union types cannot be passed in as arguments in the type system
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
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          spec: AgentCard wallet. Omit provider_config to use Kernel-managed credentials, or
              select a customer-owned configuration. Mode (sandbox vs live) is determined by
              the selected credential; there is no per-item test flag. Without user_id,
              creation returns a hosted enrollment action and Kernel polls until the user
              connects. With a customer-owned provider_config, user_id imports an existing
              connection after verifying access with the selected credentials in their sandbox
              or live mode; no hosted enrollment is needed, even if the connected user has no
              stored cards. With Kernel-managed credentials, user_id may only reference a user
              already enrolled by a wallet in this organization under the same configuration.
              The user and configuration bindings cannot be changed after creation. Import
              validation is read-only and runs before creation: a failed validation leaves no
              wallet or reserved key, so the user_id can be corrected and retried. Concurrent
              imports of the same key may both validate, but create at most one wallet and
              connected event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          spec: Live Link card request. Test-mode card creation is not supported. The spec can
              be changed with PATCH until the card is authorized at a checkout. Authorize it
              with the browser at final checkout: Kernel inspects the checkout through WebMCP
              and internally chooses a merchant-bound Link Pay Token when supported or a
              virtual card otherwise. Callers never receive or choose how the credential is
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: PaymentRequestVaultItemSpecParam,
        type: Literal["payment_request"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          spec: Live Link card request. Test-mode card creation is not supported. The spec can
              be changed with PATCH until the card is authorized at a checkout. Authorize it
              with the browser at final checkout: Kernel inspects the checkout through WebMCP
              and internally chooses a merchant-bound Link Pay Token when supported or a
              virtual card otherwise. Callers never receive or choose how the credential is
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: OnePasswordCredentialAccountSpecParam,
        type: Literal["credential_account"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CredentialVaultItemSpecInputParam,
        type: Literal["credential"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          spec: Credential fields are for login and other non-payment credentials. Do not store,
              collect, or fill credit card data in credential items. Use wallet,
              payment_request and card item types for credit cards and payment checkout
              instead. Field order is preserved in the user-facing collection form, so list
              fields in the same top-to-bottom order as the website.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["id_or_name", "spec", "type"])
    def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: item_upsert_params.WalletVaultItemRequestSpec
        | CardVaultItemSpecParam
        | PaymentRequestVaultItemSpecParam
        | OnePasswordCredentialAccountSpecParam
        | CredentialVaultItemSpecInputParam,
        type: Literal["wallet"]
        | Literal["card"]
        | Literal["payment_request"]
        | Literal["credential_account"]
        | Literal["credential"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
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
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
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
        expand: List[Literal["payment_methods", "link_user_info", "link_shipping_addresses"]] | Omit = omit,
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
        instead of a partial item. Pending credential items return a collection action.
        Kernel-hosted active collection links are renewed atomically on expiry for ready
        or pending items without changing the item version. Invoke collect to open a
        form for a ready item without clearing values. Sensitive credential values are
        never returned.

        Args:
          expand: Live fields advertised by `available_expansions` to include in `expanded`.

          wait: Hold for up to this many seconds while the item is pending authorization,
              approval, or credential collection. Return the current item when ready or when
              the wait elapses. This does not wait for edits to an already-ready credential;
              poll GET without wait and compare version to observe changes after collect.
              Managed auth credentials are created ready, so wait returns immediately.

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

    @overload
    async def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CardVaultItemSpecParam,
        type: Literal["card"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Credential updates require type credential and the current version, and change
        only values or description; omitted values are preserved, nonempty strings
        replace, and null or empty strings clear supported fields. Clearing required
        text/email/password values returns pending_collection; browser forms still
        require nonempty required inputs. Card updates may omit type for compatibility
        with legacy requests. Requested cards accept a replacement specification.
        Pending issuance requests may update provider-supported fields on their existing
        request, subject to atomic provider approval checks; omitted optional fields
        remain unchanged and explicit empty lists clear them. Wallet/provider binding
        and unsupported fields cannot change after authorization starts. An uncertain
        update enters recovery_required; delete the card and create a new one rather
        than retrying the update. Checkout cards may be edited between authorizations. A
        Link card authorized with browser_id and page_url cannot be changed; delete it
        and create a new card with the updated details.

        Args:
          spec: Live Link card request. Test-mode card creation is not supported. The spec can
              be changed with PATCH until the card is authorized at a checkout. Authorize it
              with the browser at final checkout: Kernel inspects the checkout through WebMCP
              and internally chooses a merchant-bound Link Pay Token when supported or a
              virtual card otherwise. Callers never receive or choose how the credential is
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: PaymentRequestVaultItemSpecParam,
        type: Literal["payment_request"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Credential updates require type credential and the current version, and change
        only values or description; omitted values are preserved, nonempty strings
        replace, and null or empty strings clear supported fields. Clearing required
        text/email/password values returns pending_collection; browser forms still
        require nonempty required inputs. Card updates may omit type for compatibility
        with legacy requests. Requested cards accept a replacement specification.
        Pending issuance requests may update provider-supported fields on their existing
        request, subject to atomic provider approval checks; omitted optional fields
        remain unchanged and explicit empty lists clear them. Wallet/provider binding
        and unsupported fields cannot change after authorization starts. An uncertain
        update enters recovery_required; delete the card and create a new one rather
        than retrying the update. Checkout cards may be edited between authorizations. A
        Link card authorized with browser_id and page_url cannot be changed; delete it
        and create a new card with the updated details.

        Args:
          spec: Live Link card request. Test-mode card creation is not supported. The spec can
              be changed with PATCH until the card is authorized at a checkout. Authorize it
              with the browser at final checkout: Kernel inspects the checkout through WebMCP
              and internally chooses a merchant-bound Link Pay Token when supported or a
              virtual card otherwise. Callers never receive or choose how the credential is
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CredentialVaultItemSpecUpdateParam,
        type: Literal["credential"],
        version: int,
        expected_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Credential updates require type credential and the current version, and change
        only values or description; omitted values are preserved, nonempty strings
        replace, and null or empty strings clear supported fields. Clearing required
        text/email/password values returns pending_collection; browser forms still
        require nonempty required inputs. Card updates may omit type for compatibility
        with legacy requests. Requested cards accept a replacement specification.
        Pending issuance requests may update provider-supported fields on their existing
        request, subject to atomic provider approval checks; omitted optional fields
        remain unchanged and explicit empty lists clear them. Wallet/provider binding
        and unsupported fields cannot change after authorization starts. An uncertain
        update enters recovery_required; delete the card and create a new one rather
        than retrying the update. Checkout cards may be edited between authorizations. A
        Link card authorized with browser_id and page_url cannot be changed; delete it
        and create a new card with the updated details.

        Args:
          version: Expected current item version from the latest read.

          expected_item_id: Optional immutable item ID precondition. Returns 409 if the key now identifies a
              different item. Accepted writes target this immutable ID, preventing
              replacement-key races. Supply this when submitting a form bound to a previously
              read item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["id_or_name", "spec"], ["id_or_name", "spec", "type"], ["id_or_name", "spec", "type", "version"])
    async def update(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CardVaultItemSpecParam | PaymentRequestVaultItemSpecParam | CredentialVaultItemSpecUpdateParam,
        type: Literal["card"] | Literal["payment_request"] | Literal["credential"] | Omit = omit,
        version: int | Omit = omit,
        expected_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItem,
            await self._patch(
                path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
                body=await async_maybe_transform(
                    {
                        "spec": spec,
                        "type": type,
                        "version": version,
                        "expected_item_id": expected_item_id,
                    },
                    item_update_params.ItemUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
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
        """Credential entries include safe field metadata and non-sensitive values.

        Listing
        never creates or renews collection sessions; only an existing unexpired active
        session is included. Use single-item GET or collect to obtain a fresh link.

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
        idempotency_key: str | None = None,
    ) -> None:
        """
        Unresolved payment operations normally block deletion, including operations on
        child cards of a wallet. Deleting a connected Kernel wallet first blocks new
        payments on it, then removes its enrolled card. If that fails, the wallet is
        kept and keeps refusing payments; retry the deletion. A Link or Kernel card in
        recovery_required for issuance, or an AgentCard card in recovery_required whose
        checkout create response returned no authorization ID, may be explicitly
        abandoned by deleting that card directly; deleting its wallet or vault remains
        blocked until the card is deleted. Deleting or recreating an item is not proof
        that a payment did not occur. Deleting a managed auth credential item leaves the
        connection and its saved credential unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/vaults/{id_or_name}/items/{key}", id_or_name=id_or_name, key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["authorize"],
        browser_id: str | Omit = omit,
        page_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name. The browser must have this
              vault attached.

          page_url: Exact current top-level URL of the final checkout page open in browser_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["restart_verification"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        amount: int,
        currency: str,
        occurred_at: Union[str, datetime],
        status: Literal["APPROVED", "DECLINED", "PENDING", "ERROR", "CANCELLED"],
        transaction_type: Literal[
            "PURCHASE", "AUTHORIZATION", "CAPTURE", "REFUND", "REVERSAL", "VERIFICATION", "CHARGEBACK", "FRAUD"
        ],
        type: Literal["confirm_transaction"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          amount: Actual transaction amount in minor units, no greater than the approved limit.

          currency: Must match the approved purchase currency.

          occurred_at: Time the merchant outcome was observed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["collect"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        checkout: VaultCheckoutContextParam,
        type: Literal["prepare_checkout"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          checkout: Required when preparing an unused AgentCard card for a supported checkout
              processor. Consent is bound to this browser and declared merchant origin, not a
              tab. Wait for the item's ready_to_submit status before native Pay and submit
              within its readiness deadline. Unused preparations expire automatically; every
              preparation is single-use, including after failure or expiry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        type: Literal["fill"],
        fields: Iterable[VaultFillFieldParam] | Omit = omit,
        page_url: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          fields: Field bindings, when the item's advertised fill operation requires them. Each
              selector is searched in the main frame and all descendant frames and must
              resolve to exactly one editable input or select, matched directly or through a
              containing element; zero or multiple candidates fail, and no two bindings may
              resolve to the same element. Select elements match an option by value, not
              label. All bindings are validated before any write, then filled in request
              order, stopping at the first failure. If the page navigates or a target
              disappears, fill stops rather than choosing another page or element.

          page_url: Exact current top-level page URL, including path, query, and fragment. Must
              match exactly one open page in the browser; zero or multiple matches fail. No
              prefix or glob matching. When an item allows omitting it, the browser must have
              exactly one open page.

          timeout_ms: Ignored. Fill sets no operation deadline; typing pace adapts to the length of
              the values instead. Accepted for compatibility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        type: Literal["arm_passkey"],
        field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          field: Passkey field to arm. Required when more than one passkey field holds a passkey.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        type: Literal["register_passkey"],
        field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          field: Empty passkey field to store the new passkey in. Required when more than one
              passkey field is empty.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        type: Literal["disarm_passkey"],
        field: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          field: Limit disarming to one passkey field. Omit to disarm every passkey field of the
              item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["1pw_create_access_request"],
        goal: str | Omit = omit,
        keywords: SequenceNotStr[str] | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["1pw_access_request_status"],
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        browser_id: str,
        page_url: str,
        type: Literal["1pw_fill"],
        entry_id: str | Omit = omit,
        target_id: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          page_url: Exact current top-level page URL. Must match exactly one open page in the
              browser unless target_id is supplied.

          entry_id: ID of an approved request entry. Required when several approved entries have the
              page's origin.

          target_id: CDP target ID of the page to fill, such as tab.target_id from
              playwright.execute. Use it when several open pages have page_url. The page's
              current URL must equal page_url. Kernel brings the page to the front of its
              window before filling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["1pw_recover"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        access_token: str,
        type: Literal["1pw_update_access_token"],
        access_token_expires_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          access_token_expires_at: Optional supplied expiry. Omit to clear the old expiry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        bindings: Iterable[VaultWebmcpBindingParam],
        browser_id: str,
        input: Dict[str, object],
        page_url: str,
        tool_ref: str,
        type: Literal["webmcp_invoke"],
        timeout_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          browser_id: Browser session ID, not a reusable browser name.

          input: Public tool arguments with an existing null slot at each binding path. At most
              64 KiB after JSON serialization, including substituted values. Never include
              vault values here.

          page_url: Exact top-level URL from the discovered tool source (fragment omitted). This
              pins the target page; it does not authorize a destination.

          tool_ref: Opaque reference to the exact live WebMCP registration.

          timeout_sec: Tool invocation timeout in seconds; preflight and response handling have an
              additional bounded allowance. An indeterminate outcome is not retried.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["add_payment_method"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        payment_method_id: str,
        type: Literal["remove_payment_method"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        """
        Retrieve the item first and invoke only an operation listed in
        `available_operations`, following its natural-language description. Availability
        is rechecked at execution time; unavailable operations return 409. Authorization
        and preparation may call an external provider and return updated state. Link
        cards advertise authorize; pass browser_id and page_url from the final checkout
        page so Kernel can inspect the checkout. Eligible unused AgentCard cards
        advertise prepare_checkout, which requires checkout context and obtains device
        approval before native Square Pay. Keep the returned approval page open, poll
        until ready_to_submit, then submit before preparation.expires_at. Unused
        preparations expire automatically and cannot be reused. If spend-request
        creation is rejected with a non-retryable provider error, the card item is
        deleted and the provider's error code and message are returned. Rate limits
        return HTTP 429 and retain the card item; stop, back off, and retry the same
        authorize operation.

        Ready Kernel cards advertise fill. Fill delivers card details for a few minutes;
        submit checkout promptly after filling. A repeated fill is safe.

        Fill returns a value-free execution result. Validation failures before writing
        return 400 (invalid request or targets), 403 (access or destination denied), 404
        (resource not found), or 409 (item or browser not ready). Once writing starts,
        known partial failures and indeterminate field outcomes return 200 with status
        `failed` or `unknown`. Fill never submits the page, so it is safe to retry after
        a failure, an `unknown` outcome, or a transport error.

        Connected Kernel wallets may advertise add_payment_method, which returns a
        single-use hosted card_enrollment link for a card, and remove_payment_method,
        which removes one card without affecting the others. Both operations require
        vaults:write in addition to vaults:use on the vault for scoped API keys, and
        return 403 without both permissions.

        Args:
          payment_method_id: ID from the wallet's payment_methods expansion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(
        ["id_or_name", "type"],
        ["id_or_name", "amount", "currency", "occurred_at", "status", "transaction_type", "type"],
        ["id_or_name", "checkout", "type"],
        ["id_or_name", "browser_id", "type"],
        ["id_or_name", "browser_id", "page_url", "type"],
        ["id_or_name", "access_token", "type"],
        ["id_or_name", "bindings", "browser_id", "input", "page_url", "tool_ref", "type"],
        ["id_or_name", "payment_method_id", "type"],
    )
    async def perform_operation(
        self,
        key: str,
        *,
        id_or_name: str,
        type: Literal["authorize"]
        | Literal["restart_verification"]
        | Literal["confirm_transaction"]
        | Literal["collect"]
        | Literal["prepare_checkout"]
        | Literal["fill"]
        | Literal["arm_passkey"]
        | Literal["register_passkey"]
        | Literal["disarm_passkey"]
        | Literal["1pw_create_access_request"]
        | Literal["1pw_access_request_status"]
        | Literal["1pw_fill"]
        | Literal["1pw_recover"]
        | Literal["1pw_update_access_token"]
        | Literal["webmcp_invoke"]
        | Literal["add_payment_method"]
        | Literal["remove_payment_method"],
        browser_id: str | Omit = omit,
        page_url: str | Omit = omit,
        amount: int | Omit = omit,
        currency: str | Omit = omit,
        occurred_at: Union[str, datetime] | Omit = omit,
        status: Literal["APPROVED", "DECLINED", "PENDING", "ERROR", "CANCELLED"] | Omit = omit,
        transaction_type: Literal[
            "PURCHASE", "AUTHORIZATION", "CAPTURE", "REFUND", "REVERSAL", "VERIFICATION", "CHARGEBACK", "FRAUD"
        ]
        | Omit = omit,
        checkout: VaultCheckoutContextParam | Omit = omit,
        fields: Iterable[VaultFillFieldParam] | Omit = omit,
        timeout_ms: int | Omit = omit,
        field: str | Omit = omit,
        goal: str | Omit = omit,
        keywords: SequenceNotStr[str] | Omit = omit,
        reason: str | Omit = omit,
        timeout_seconds: int | Omit = omit,
        entry_id: str | Omit = omit,
        target_id: str | Omit = omit,
        access_token: str | Omit = omit,
        access_token_expires_at: Union[str, datetime] | Omit = omit,
        bindings: Iterable[VaultWebmcpBindingParam] | Omit = omit,
        input: Dict[str, object] | Omit = omit,
        tool_ref: str | Omit = omit,
        timeout_sec: int | Omit = omit,
        payment_method_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItemOperationResponse:
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return cast(
            VaultItemOperationResponse,
            await self._client.with_options(max_retries=0).post(
                path_template("/vaults/{id_or_name}/items/{key}/operations", id_or_name=id_or_name, key=key),
                body=await async_maybe_transform(
                    {
                        "type": type,
                        "browser_id": browser_id,
                        "page_url": page_url,
                        "amount": amount,
                        "currency": currency,
                        "occurred_at": occurred_at,
                        "status": status,
                        "transaction_type": transaction_type,
                        "checkout": checkout,
                        "fields": fields,
                        "timeout_ms": timeout_ms,
                        "field": field,
                        "goal": goal,
                        "keywords": keywords,
                        "reason": reason,
                        "timeout_seconds": timeout_seconds,
                        "entry_id": entry_id,
                        "target_id": target_id,
                        "access_token": access_token,
                        "access_token_expires_at": access_token_expires_at,
                        "bindings": bindings,
                        "input": input,
                        "tool_ref": tool_ref,
                        "timeout_sec": timeout_sec,
                        "payment_method_id": payment_method_id,
                    },
                    item_perform_operation_params.ItemPerformOperationParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, VaultItemOperationResponse
                ),  # Union types cannot be passed in as arguments in the type system
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
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          spec: AgentCard wallet. Omit provider_config to use Kernel-managed credentials, or
              select a customer-owned configuration. Mode (sandbox vs live) is determined by
              the selected credential; there is no per-item test flag. Without user_id,
              creation returns a hosted enrollment action and Kernel polls until the user
              connects. With a customer-owned provider_config, user_id imports an existing
              connection after verifying access with the selected credentials in their sandbox
              or live mode; no hosted enrollment is needed, even if the connected user has no
              stored cards. With Kernel-managed credentials, user_id may only reference a user
              already enrolled by a wallet in this organization under the same configuration.
              The user and configuration bindings cannot be changed after creation. Import
              validation is read-only and runs before creation: a failed validation leaves no
              wallet or reserved key, so the user_id can be corrected and retried. Concurrent
              imports of the same key may both validate, but create at most one wallet and
              connected event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          spec: Live Link card request. Test-mode card creation is not supported. The spec can
              be changed with PATCH until the card is authorized at a checkout. Authorize it
              with the browser at final checkout: Kernel inspects the checkout through WebMCP
              and internally chooses a merchant-bound Link Pay Token when supported or a
              virtual card otherwise. Callers never receive or choose how the credential is
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: PaymentRequestVaultItemSpecParam,
        type: Literal["payment_request"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          spec: Live Link card request. Test-mode card creation is not supported. The spec can
              be changed with PATCH until the card is authorized at a checkout. Authorize it
              with the browser at final checkout: Kernel inspects the checkout through WebMCP
              and internally chooses a merchant-bound Link Pay Token when supported or a
              virtual card otherwise. Callers never receive or choose how the credential is
              delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: OnePasswordCredentialAccountSpecParam,
        type: Literal["credential_account"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: CredentialVaultItemSpecInputParam,
        type: Literal["credential"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VaultItem:
        """
        Create an item under a key unique within its vault, or retrieve the existing
        item when its specification matches. An identical card PUT returns the existing
        card in any lifecycle state without polling the provider, reauthorizing,
        replacing aliases, or resetting recovery. Conflicting specifications return 409.
        Provider-specific authorization requirements and retry behavior are described in
        the item's request schema. Do not use credential items to store, collect, or
        fill credit card data, including card numbers (PANs), security codes (CVV/CVC),
        or expiration dates. Use wallet, payment_request and card item types for credit
        cards and payment checkout instead. Where enabled, Link and Kernel purchases can
        be payment_request items parented by their wallet; card items remain supported
        for them and for AgentCard reusable cards.

        Args:
          spec: Credential fields are for login and other non-payment credentials. Do not store,
              collect, or fill credit card data in credential items. Use wallet,
              payment_request and card item types for credit cards and payment checkout
              instead. Field order is preserved in the user-facing collection form, so list
              fields in the same top-to-bottom order as the website.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["id_or_name", "spec", "type"])
    async def upsert(
        self,
        key: str,
        *,
        id_or_name: str,
        spec: item_upsert_params.WalletVaultItemRequestSpec
        | CardVaultItemSpecParam
        | PaymentRequestVaultItemSpecParam
        | OnePasswordCredentialAccountSpecParam
        | CredentialVaultItemSpecInputParam,
        type: Literal["wallet"]
        | Literal["card"]
        | Literal["payment_request"]
        | Literal["credential_account"]
        | Literal["credential"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
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
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
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
