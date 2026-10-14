# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .vault_item_action import VaultItemAction
from .card_vault_item_spec import CardVaultItemSpec
from .vault_payment_method import VaultPaymentMethod
from .card_vault_item_state import CardVaultItemState
from .credential_vault_item import CredentialVaultItem
from .wallet_vault_item_spec import WalletVaultItemSpec
from .wallet_vault_item_state import WalletVaultItemState
from .credential_account_vault_item import CredentialAccountVaultItem

__all__ = [
    "VaultItem",
    "WalletVaultItem",
    "WalletVaultItemAvailableExpansion",
    "WalletVaultItemAvailableOperation",
    "WalletVaultItemExpanded",
    "CardVaultItem",
    "CardVaultItemAvailableExpansion",
    "CardVaultItemAvailableOperation",
]


class WalletVaultItemAvailableExpansion(BaseModel):
    """
    Live data that can currently be requested by passing its type to the item GET expand parameter.
    """

    description: str

    type: Literal["payment_methods"]


class WalletVaultItemAvailableOperation(BaseModel):
    """An operation that is currently valid for this item.

    Read the description before invoking it through the item operations endpoint.
    """

    description: str

    type: Literal[
        "authorize",
        "restart_verification",
        "confirm_transaction",
        "collect",
        "prepare_checkout",
        "fill",
        "1pw_create_access_request",
        "1pw_access_request_status",
        "1pw_fill",
        "1pw_recover",
        "1pw_update_access_token",
        "webmcp_invoke",
    ]


class WalletVaultItemExpanded(BaseModel):
    """Live, non-persisted data requested through the item GET expand parameter."""

    payment_methods: Optional[List[VaultPaymentMethod]] = None


class WalletVaultItem(BaseModel):
    id: str

    available_expansions: List[WalletVaultItemAvailableExpansion]

    available_operations: List[WalletVaultItemAvailableOperation]

    created_at: datetime

    key: str
    """Immutable item key assigned when the item is created."""

    spec: WalletVaultItemSpec
    """AgentCard wallet.

    Omit provider_config to use Kernel-managed credentials, or select a
    customer-owned configuration. Mode (sandbox vs live) is determined by the
    selected credential; there is no per-item test flag. Without user_id, creation
    returns a hosted enrollment action and Kernel polls until the user connects.
    user_id may only reference a user already enrolled by a wallet in this
    organization under the same configuration.
    """

    state: WalletVaultItemState

    type: Literal["wallet"]

    updated_at: datetime

    action: Optional[VaultItemAction] = None

    description: Optional[str] = None
    """Server-generated provider and lifecycle guidance for agents."""

    expanded: Optional[WalletVaultItemExpanded] = None
    """Live, non-persisted data requested through the item GET expand parameter."""

    expires_at: Optional[datetime] = None


class CardVaultItemAvailableExpansion(BaseModel):
    """
    Live data that can currently be requested by passing its type to the item GET expand parameter.
    """

    description: str

    type: Literal["payment_methods"]


class CardVaultItemAvailableOperation(BaseModel):
    """An operation that is currently valid for this item.

    Read the description before invoking it through the item operations endpoint.
    """

    description: str

    type: Literal[
        "authorize",
        "restart_verification",
        "confirm_transaction",
        "collect",
        "prepare_checkout",
        "fill",
        "1pw_create_access_request",
        "1pw_access_request_status",
        "1pw_fill",
        "1pw_recover",
        "1pw_update_access_token",
        "webmcp_invoke",
    ]


class CardVaultItem(BaseModel):
    id: str

    available_expansions: List[CardVaultItemAvailableExpansion]

    available_operations: List[CardVaultItemAvailableOperation]

    created_at: datetime

    key: str
    """Immutable item key assigned when the item is created."""

    spec: CardVaultItemSpec
    """Live Link card request.

    Test-mode card creation is not supported. The spec can be changed with PATCH
    until the card is authorized at a checkout. Authorize it with the browser at
    final checkout: Kernel inspects the checkout through WebMCP and internally
    chooses a merchant-bound Link Pay Token when supported or a virtual card
    otherwise. Callers never receive or choose how the credential is delivered.
    """

    state: CardVaultItemState
    """Issued Link cards retain encrypted card material for the fill operation.

    Link cards do not expose aliases or support egress substitution.
    """

    type: Literal["card"]

    updated_at: datetime

    action: Optional[VaultItemAction] = None

    expires_at: Optional[datetime] = None


VaultItem: TypeAlias = Annotated[
    Union[WalletVaultItem, CardVaultItem, CredentialAccountVaultItem, CredentialVaultItem],
    PropertyInfo(discriminator="type"),
]
