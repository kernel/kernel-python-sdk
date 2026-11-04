# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VgsWalletState"]


class VgsWalletState(BaseModel):
    provider: Literal["vgs"]

    status: Literal["pending_authorization", "connected", "degraded"]
    """A VGS wallet is connected on creation.

    pending_authorization or degraded means its creation did not finish; reading the
    wallet retries it, and a wallet that stays degraded can be deleted and created
    again. Whether its configuration's credentials still work is checked when a card
    is authorized.
    """

    status_reason: Optional[str] = None
