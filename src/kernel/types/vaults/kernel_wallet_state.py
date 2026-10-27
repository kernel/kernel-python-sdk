# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KernelWalletState"]


class KernelWalletState(BaseModel):
    provider: Literal["kernel"]

    status: Literal["pending_authorization", "connected", "reconnect_required", "degraded"]
    """connected means the wallet is usable.

    It holds zero or more cards as payment methods, listed by the payment_methods
    expansion, and each can pay once it reports
    capabilities.single_use_card.eligible. A wallet with no cards, before its first
    card or after its last is removed, is still connected. Where the wallet
    advertises add_payment_method and remove_payment_method, use them to manage
    cards. Otherwise the wallet enrolls one default card when created; until that
    card is enrolled the wallet reports pending_authorization with the card's
    card_enrollment action, or degraded when the card's enrollment outcome is
    unknown and the wallet must be deleted before adding another card.
    reconnect_required appears only on a wallet created before cards were payment
    methods and not yet upgraded. Reads preserve its stored state until the operator
    upgrade; payment and deletion requests are refused until then.
    """

    status_reason: Optional[str] = None
