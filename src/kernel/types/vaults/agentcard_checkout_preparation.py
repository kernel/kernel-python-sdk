# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .agentcard_prepared_processor import AgentcardPreparedProcessor

__all__ = ["AgentcardCheckoutPreparation"]


class AgentcardCheckoutPreparation(BaseModel):
    """One-use processor-bound checkout preparation.

    Keep the approval page open through token handoff. The amount is display-only and does not constrain the merchant's eventual charge.
    """

    browser_id: str

    created_at: datetime

    environment: Literal["production", "sandbox", "shared"]

    merchant_origin: str

    psp: AgentcardPreparedProcessor

    status: Literal["creating", "awaiting_approval", "ready", "consumed", "cancelled", "expired", "unknown"]
    """
    Preparation consumed means egress claimed the preparation and it cannot be
    reused. It does not mean the attempt settled. Use the enclosing item's status as
    the lifecycle indicator; item consumed means the attempt settled, not that an
    order or charge succeeded.
    """

    id: Optional[str] = None

    approval_url: Optional[str] = None

    expires_at: Optional[datetime] = None
    """
    When ready, the absolute deadline to submit the first native request; no later
    than provider readiness expiry or 30 seconds after Kernel first observes
    readiness. Polling never extends this deadline.
    """
