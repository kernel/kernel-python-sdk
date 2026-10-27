# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VaultPaymentMethod", "Capabilities", "CapabilitiesSingleUseCard", "Display", "Action"]


class CapabilitiesSingleUseCard(BaseModel):
    eligible: bool

    reasons: List[str]


class Capabilities(BaseModel):
    """Provider-reported advisory capabilities.

    A missing capability is unknown, not ineligible; only eligible=false is an explicit negative signal.
    """

    single_use_card: Optional[CapabilitiesSingleUseCard] = None


class Display(BaseModel):
    brand: Optional[str] = None

    label: Optional[str] = None

    last4: Optional[str] = None


class Action(BaseModel):
    name: Literal["card_enrollment"]

    url: str

    capture_token: Optional[str] = None
    """Secret bearer capability for embedded card capture with @onkernel/vault-react.

    Present only for Kernel wallets; never for AgentCard. Treat it like the
    enrollment URL and do not log or persist it in browser storage.
    """


class VaultPaymentMethod(BaseModel):
    id: str

    capabilities: Capabilities
    """Provider-reported advisory capabilities.

    A missing capability is unknown, not ineligible; only eligible=false is an
    explicit negative signal.
    """

    display: Display

    is_default: bool
    """
    For Kernel wallets, true for the default card, ID card, which a Kernel card item
    that omits payment_method_id selects. Wallets created with payment methods
    enabled have no default card.
    """

    provider: str
    """Provider that issued this payment-method ID."""

    type: str
    """Provider-neutral payment-method type normalized to lowercase."""

    action: Optional[Action] = None

    expires_at: Optional[datetime] = None
    """Expiry of a pending enrollment link."""

    status: Optional[Literal["pending_enrollment", "active", "removal_pending", "recovery_required"]] = None
    """Kernel wallets only.

    pending_enrollment means a card_enrollment link is open; active means the card
    is stored and can pay when capabilities.single_use_card.eligible is true;
    removal_pending means removal started but the provider outcome is unknown, so
    retry remove_payment_method; recovery_required means either an enrollment
    outcome is unknown (remove the method), or the stored card cannot be read
    (contact support; removal is refused with 409). Consult status_reason to
    distinguish these cases. Absent for other providers.
    """

    status_reason: Optional[str] = None
