# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrowserCost"]


class BrowserCost(BaseModel):
    status: Literal["provisional", "pending", "unavailable"]
    """
    Pending means the billing checkpoint or rate calculation is not ready;
    unavailable means the session cannot currently be priced safely.
    """

    as_of: Optional[datetime] = None
    """Time of the live uptime read or durable billing checkpoint.

    A running or recently deleted session may accrue additional usage.
    """

    estimated_usage_spend_usd: Optional[str] = None
    """
    Gross provisional USD browser-meter cost before credits, subscriptions, tax, and
    adjustments. Present only with provisional status, including zero for a
    completed zero-uptime session. Not an invoice total.
    """
