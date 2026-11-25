# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KernelWalletState"]


class KernelWalletState(BaseModel):
    provider: Literal["kernel"]

    status: Literal["pending_authorization", "connected", "reconnect_required", "degraded"]
    """connected means the wallet is usable.

    New wallets are created connected and empty. A wallet holds zero or more cards
    as payment methods, added with add_payment_method, removed with
    remove_payment_method and listed by the payment_methods expansion; each can pay
    once it reports capabilities.single_use_card.eligible. A wallet with no cards,
    before its first card or after its last is removed, is still connected. A wallet
    created before cards were added with add_payment_method holds a default card, ID
    card; while that card's enrollment is pending, its card_enrollment action is on
    the card in the payment_methods expansion, not on the wallet.
    pending_authorization, degraded and reconnect_required appear only on a wallet
    created before cards were payment methods and not yet upgraded. Reads preserve
    its stored state until the operator upgrade; payment and deletion requests are
    refused until then.
    """

    status_reason: Optional[str] = None
