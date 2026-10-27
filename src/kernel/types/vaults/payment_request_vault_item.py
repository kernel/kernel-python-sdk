# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .vault_item_action import VaultItemAction
from .payment_request_vault_item_spec import PaymentRequestVaultItemSpec
from .payment_request_vault_item_state import PaymentRequestVaultItemState

__all__ = ["PaymentRequestVaultItem", "AvailableExpansion", "AvailableOperation"]


class AvailableExpansion(BaseModel):
    """
    Live data that can currently be requested by passing its type to the item GET expand parameter.
    """

    description: str

    type: Literal["payment_methods", "link_user_info", "link_shipping_addresses"]


class AvailableOperation(BaseModel):
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
        "arm_passkey",
        "register_passkey",
        "disarm_passkey",
        "1pw_create_access_request",
        "1pw_access_request_status",
        "1pw_fill",
        "1pw_recover",
        "1pw_update_access_token",
        "webmcp_invoke",
        "add_payment_method",
        "remove_payment_method",
    ]


class PaymentRequestVaultItem(BaseModel):
    """One purchase from a Link or Kernel wallet, parented by that wallet.

    It has the same lifecycle, operations and fill behavior as a Link or Kernel card item. AgentCard reusable cards remain card items.
    """

    id: str

    available_expansions: List[AvailableExpansion]

    available_operations: List[AvailableOperation]

    created_at: datetime

    key: str
    """Immutable item key assigned when the item is created."""

    spec: PaymentRequestVaultItemSpec
    """Live Link card request.

    Test-mode card creation is not supported. The spec can be changed with PATCH
    until the card is authorized at a checkout. Authorize it with the browser at
    final checkout: Kernel inspects the checkout through WebMCP and internally
    chooses a merchant-bound Link Pay Token when supported or a virtual card
    otherwise. Callers never receive or choose how the credential is delivered.
    """

    state: PaymentRequestVaultItemState
    """Issued Link cards retain encrypted card material for the fill operation.

    Link cards do not expose aliases or support egress substitution.
    """

    type: Literal["payment_request"]

    updated_at: datetime

    action: Optional[VaultItemAction] = None

    expires_at: Optional[datetime] = None
