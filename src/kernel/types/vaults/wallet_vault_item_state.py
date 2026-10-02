# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .kernel_wallet_state import KernelWalletState

__all__ = ["WalletVaultItemState", "LinkWalletState", "AgentCardWalletState"]


class LinkWalletState(BaseModel):
    provider: Literal["link"]

    status: Literal["pending_authorization", "connected", "declined", "reconnect_required", "degraded"]

    status_reason: Optional[str] = None


class AgentCardWalletState(BaseModel):
    provider: Literal["agentcard"]

    status: Literal["pending_authorization", "connected", "degraded"]

    status_reason: Optional[str] = None

    user_id: Optional[str] = None
    """AgentCard user id linked to this wallet. Present once connected."""


WalletVaultItemState: TypeAlias = Annotated[
    Union[LinkWalletState, AgentCardWalletState, KernelWalletState], PropertyInfo(discriminator="provider")
]
