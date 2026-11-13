# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentcardCheckoutAuthorization"]


class AgentcardCheckoutAuthorization(BaseModel):
    """The in-flight or most recent checkout authorization.

    Present while a checkout is pending approval and after it settles.
    """

    id: str

    amount_cents: int

    created_at: datetime

    currency: str

    merchant: str

    psp: str

    status: Literal["awaiting_approval", "approved", "declined", "expired"]

    actual_cents: Optional[int] = None

    amount: Optional[str] = None
    """Display amount shown on the approval screen."""

    amount_authority: Optional[Literal["processor", "agent", "page", "none", "display_only"]] = None
    """Source of the approved amount.

    `processor` is read from the processor request or payment; `agent` is the item's
    declared amount; `page` is the checkout page total; `none` means no amount was
    named. `display_only` appears only on authorizations recovered without a
    provider read. `agent` and `display_only` don't prove what the processor
    charged.
    """

    amount_verified: Optional[bool] = None
    """Whether the processor charged the approved amount.

    Absent when there was no charge to compare, including tokenization checkouts.
    """

    approval_url: Optional[str] = None

    browser_id: Optional[str] = None
    """Browser session that submitted the checkout."""

    charged_amount_cents: Optional[int] = None
    """Amount the processor reported collecting.

    Absent when the provider didn't observe a charge.
    """

    charged_currency: Optional[str] = None
    """Currency of `charged_amount_cents`.

    Absent when the provider didn't observe a charge.
    """

    charged_kind: Optional[Literal["captured", "authorized", "none"]] = None
    """What the processor collected.

    `none` means the checkout produced a token or payment method that the merchant
    charges later. Absent when the provider reported nothing, which is common for
    tokenization checkouts; use item events and the merchant's order record instead.
    """

    expected_cents: Optional[int] = None

    expires_at: Optional[datetime] = None

    psp_error_code: Optional[str] = None

    reason: Optional[str] = None

    replay_attempted: Optional[bool] = None

    replay_delivered: Optional[bool] = None
    """Whether the processor response was delivered to the browser."""

    replay_status: Optional[int] = None
    """HTTP status of the replayed processor response."""
