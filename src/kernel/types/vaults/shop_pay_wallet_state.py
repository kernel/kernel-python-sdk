# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ShopPayWalletState"]


class ShopPayWalletState(BaseModel):
    provider: Literal["shop_pay"]

    status: Literal["pending_authorization", "connected", "declined", "reconnect_required", "degraded"]

    status_reason: Optional[str] = None
