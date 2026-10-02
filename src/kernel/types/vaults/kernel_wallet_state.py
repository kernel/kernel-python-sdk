# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KernelWalletState"]


class KernelWalletState(BaseModel):
    provider: Literal["kernel"]

    status: Literal["pending_authorization", "connected", "reconnect_required", "degraded"]
    """pending_authorization asks the cardholder to use the card_enrollment action.

    connected is ready for supported purchases. reconnect_required asks the
    cardholder to use a new card_enrollment action after an uncertain enrollment was
    safely removed. degraded means the enrollment outcome is unknown and the wallet
    must be deleted before adding another card.
    """

    status_reason: Optional[str] = None
