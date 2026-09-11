# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .card_vault_item_spec_param import CardVaultItemSpecParam

__all__ = [
    "ItemUpsertParams",
    "WalletVaultItemRequest",
    "WalletVaultItemRequestSpec",
    "WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpec",
    "WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorization",
    "WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationKernelManagedLinkAuthorizationInput",
    "WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationKernelManagedLinkAuthorizationInputClient",
    "WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInput",
    "WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputClient",
    "WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputClientProviderConfig",
    "WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputTokens",
    "WalletVaultItemRequestSpecAgentCardWalletVaultItemSpec",
    "WalletVaultItemRequestSpecAgentCardWalletVaultItemSpecProviderConfig",
    "CardVaultItemRequest",
]


class WalletVaultItemRequest(TypedDict, total=False):
    id_or_name: Required[str]

    spec: Required[WalletVaultItemRequestSpec]
    """AgentCard wallet.

    Omit provider_config to use Kernel-managed credentials, or select a
    customer-owned configuration. Mode (sandbox vs live) is determined by the
    selected credential; there is no per-item test flag. Without user_id, creation
    returns a hosted enrollment action and Kernel polls until the user connects.
    user_id may only reference a user already enrolled by a wallet in this
    organization under the same configuration.
    """

    type: Required[Literal["wallet"]]


class WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationKernelManagedLinkAuthorizationInputClient(
    TypedDict, total=False
):
    type: Required[Literal["kernel_managed"]]


class WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationKernelManagedLinkAuthorizationInput(
    TypedDict, total=False
):
    """Kernel starts and completes the user's Link authorization flow."""

    client: Required[
        WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationKernelManagedLinkAuthorizationInputClient
    ]

    method: Required[Literal["oauth"]]


class WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputClientProviderConfig(
    TypedDict, total=False
):
    """Select a provider config by ID or name.

    Responses return the ID. Renaming a config does not change existing wallet bindings; a wallet cannot switch to a different config after creation.
    """

    id: str

    name: str


class WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputClient(
    TypedDict, total=False
):
    provider_config: Required[
        WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputClientProviderConfig
    ]
    """Select a provider config by ID or name.

    Responses return the ID. Renaming a config does not change existing wallet
    bindings; a wallet cannot switch to a different config after creation.
    """

    type: Required[Literal["customer_managed"]]


class WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputTokens(
    TypedDict, total=False
):
    """Send the token pair from your backend.

    Both tokens must be from the same Link grant under the referenced client. Supply a currently valid access token. Kernel refreshes when needed after import and uses the expiry returned by Link for subsequent tokens. Tokens are never returned in wallet responses, events, or logs.
    """

    access_token: Required[str]

    refresh_token: Required[str]


class WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInput(
    TypedDict, total=False
):
    """The customer's backend completes Link OAuth and supplies the resulting tokens.

    For a new wallet, Kernel verifies the access token can access Link payment methods without consuming or rotating the refresh token. Valid access creates a wallet with state.status=connected. An expired, invalid, revoked, or insufficiently scoped access token returns 400 and no wallet is created. Refresh expired tokens in your backend before importing them. A failed import does not modify existing wallets.
    After successful import, Kernel owns subsequent refresh-token rotation; the customer must stop refreshing this grant. Import does not verify the refresh token: if it or the configured client credentials are rejected during a later refresh, the imported wallet becomes degraded. An unknown refresh outcome also leaves it degraded; Kernel does not retry a refresh token that may already have been consumed. There is no in-place reauthorization operation for an imported wallet.
    If this imported wallet's credentials become unusable, obtain a fresh Link OAuth grant in your backend and create a wallet under a NEW wallet key. Use the new wallet for NEW cards and payments, not to retry an old payment whose outcome is uncertain. This does not replace the old grant, rebind existing cards, or resolve their payment outcomes. Retain the old wallet and its cards while reconciling any uncertain payments with the provider or support. Do not repeat an uncertain payment on the new wallet, and do not treat deletion as evidence that it did not execute. Deletion of the old wallet can remain blocked by unresolved child cards.
    Repeating a create for the same item key and non-secret spec returns the existing wallet without replacing tokens, even if they have rotated or the wallet needs reconnection. ID and name references resolving to the same config are equivalent. A different config or non-secret spec returns 409. This create operation does not replace an existing grant.
    """

    client: Required[
        WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputClient
    ]

    method: Required[Literal["oauth"]]

    tokens: Required[
        WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInputTokens
    ]
    """Send the token pair from your backend.

    Both tokens must be from the same Link grant under the referenced client. Supply
    a currently valid access token. Kernel refreshes when needed after import and
    uses the expiry returned by Link for subsequent tokens. Tokens are never
    returned in wallet responses, events, or logs.
    """


WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorization: TypeAlias = Union[
    WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationKernelManagedLinkAuthorizationInput,
    WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorizationImportedLinkAuthorizationInput,
]


class WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpec(TypedDict, total=False):
    authorization: Required[WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpecAuthorization]
    """Kernel starts and completes the user's Link authorization flow."""

    provider: Required[Literal["link"]]


class WalletVaultItemRequestSpecAgentCardWalletVaultItemSpecProviderConfig(TypedDict, total=False):
    """Select an AgentCard configuration.

    The wallet's configuration cannot be changed after creation.
    """

    id: str

    name: str


class WalletVaultItemRequestSpecAgentCardWalletVaultItemSpec(TypedDict, total=False):
    """AgentCard wallet.

    Omit provider_config to use Kernel-managed credentials, or select a customer-owned configuration. Mode (sandbox vs live) is determined by the selected credential; there is no per-item test flag. Without user_id, creation returns a hosted enrollment action and Kernel polls until the user connects. user_id may only reference a user already enrolled by a wallet in this organization under the same configuration.
    """

    provider: Required[Literal["agentcard"]]

    provider_config: WalletVaultItemRequestSpecAgentCardWalletVaultItemSpecProviderConfig
    """Select an AgentCard configuration.

    The wallet's configuration cannot be changed after creation.
    """

    user_id: str


WalletVaultItemRequestSpec: TypeAlias = Union[
    WalletVaultItemRequestSpecLinkWalletVaultItemRequestSpec, WalletVaultItemRequestSpecAgentCardWalletVaultItemSpec
]


class CardVaultItemRequest(TypedDict, total=False):
    id_or_name: Required[str]

    spec: Required[CardVaultItemSpecParam]
    """Live payment card. Test-mode card creation is not supported."""

    type: Required[Literal["card"]]


ItemUpsertParams: TypeAlias = Union[WalletVaultItemRequest, CardVaultItemRequest]
