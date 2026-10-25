# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = [
    "LinkUserInfo",
    "Address",
    "AgentWalletSpendLimits",
    "AgentWalletSpendLimitsDaily",
    "AgentWalletSpendLimitsPerTransaction",
    "AgentWalletSpendLimitsThirtyDay",
    "AgentWalletStepUp",
]


class Address(BaseModel):
    """The Link user's postal address. Omitted when Link reports none."""

    city: Optional[str] = None

    country: Optional[str] = None

    line1: Optional[str] = None

    line2: Optional[str] = None

    postal_code: Optional[str] = None

    state: Optional[str] = None


class AgentWalletSpendLimitsDaily(BaseModel):
    limit: Optional[int] = None
    """Null means unlimited."""

    remaining: Optional[int] = None
    """Amount still available in the rolling period; null means unlimited."""

    used: int
    """Amount already spent in the rolling period."""


class AgentWalletSpendLimitsPerTransaction(BaseModel):
    limit: Optional[int] = None
    """Null means unlimited."""


class AgentWalletSpendLimitsThirtyDay(BaseModel):
    limit: Optional[int] = None
    """Null means unlimited."""

    remaining: Optional[int] = None
    """Amount still available in the rolling period; null means unlimited."""

    used: int
    """Amount already spent in the rolling period."""


class AgentWalletSpendLimits(BaseModel):
    """Link's agent wallet spend limits, per transaction and over rolling periods."""

    daily: AgentWalletSpendLimitsDaily

    per_transaction: AgentWalletSpendLimitsPerTransaction

    thirty_day: AgentWalletSpendLimitsThirtyDay


class AgentWalletStepUp(BaseModel):
    """Verification Link requires from the user before the agent wallet can spend."""

    action_url: Optional[str] = None
    """URL where the user completes verification; null when no action is available."""

    status: str
    """
    Link status such as not_required, ssn_verification, identity_verification,
    contact_support or complete.
    """


class LinkUserInfo(BaseModel):
    """
    Link's `GET /userinfo` response for the connected wallet, passed through as Link reports it when the `link_user_info` expansion is requested. Kernel never stores it. Null fields are null at Link; omitted fields were not reported. Amounts are in the minor unit of `default_spend_request_currency`.
    """

    id: Optional[str] = None
    """Stable Link user ID."""

    email: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    address: Optional[Address] = None
    """The Link user's postal address. Omitted when Link reports none."""

    agent_wallet_spend_limits: Optional[AgentWalletSpendLimits] = None
    """Link's agent wallet spend limits, per transaction and over rolling periods."""

    agent_wallet_step_up: Optional[AgentWalletStepUp] = None
    """Verification Link requires from the user before the agent wallet can spend."""

    default_spend_request_currency: Optional[str] = None
    """Lowercase ISO currency Link applies to a spend request created without one."""

    eligible_for_balance: Optional[bool] = None
    """Whether the user can fund purchases from a Link balance."""
