# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["KernelCardState", "Masks"]


class Masks(BaseModel):
    brand: Optional[str] = None

    last4: Optional[str] = None

    token_last4: Optional[str] = None
    """Last four digits of the network token presented to the merchant."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...
    else:
        __pydantic_extra__: Dict[str, str]


class KernelCardState(BaseModel):
    """A ready Kernel card supports authorize, fill, then submit checkout.

    Card details are delivered for a few minutes after fill; submit promptly. Repeated fill is safe and never submits checkout. Visa purchases require a spend_approval action before details are issued; Mastercard purchases need no hosted approval. masks.last4 is the enrolled card's last four digits; masks.token_last4, when present, is the token's last four digits shown to the merchant. Kernel does not observe whether the merchant charged the card.
    """

    provider: Literal["kernel"]

    status: Literal[
        "requested", "pending_authorization", "ready", "consumed", "expired", "declined", "recovery_required"
    ]
    """
    pending_authorization waits for cardholder approval on Visa purchases or fresh
    security-code collection on alias-mode purchases through the spend_approval
    action; an unused link expires after 30 minutes. Alias-mode cards become ready
    after collection and expire at the temporary security-code alias deadline, by
    default five minutes later. An expired alias purchase requires a new card.
    recovery_required means verification, approving the purchase or issuing the
    one-time code has an unresolved outcome. A server-classified initial attestation
    failure before intent dispatch may advertise restart_verification to prepare a
    fresh local verification link; this does not approve spending or replay any
    provider request. Unclassified legacy recovery and uncertain intent creation
    cannot restart. Kernel never approves again or issues another code for the item
    automatically. To continue, delete this card and create a new purchase; the
    cardholder approves the new purchase separately. Recovery while reporting a
    merchant transaction cannot be deleted and must be reconciled with support. When
    status_reason says the provider refused retrieval before acceptance, no code was
    issued and a later read retries. declined means the card network refused to
    issue a code.
    """

    domains: Optional[List[str]] = None
    """Informational registrable domain.

    Fill is locked to merchant_url's exact origin.
    """

    funding_status: Optional[Literal["available", "unavailable", "removed"]] = None
    """Whether payment_method_id can still fund this purchase.

    unavailable means the method is being removed or awaits recovery, so
    authorization, fill and confirmation are refused until it recovers. removed
    means the method was removed from its wallet, so this purchase can no longer be
    paid; create a new purchase with another method. Neither changes status, which
    still reports what already happened to this purchase.
    """

    masks: Optional[Masks] = None

    payment_method_id: Optional[str] = None
    """Wallet-scoped ID of the payment method funding this purchase.

    It is bound when the purchase is created and never changes; purchases created
    before payment methods could be selected report the wallet's default card, card.
    """

    status_reason: Optional[str] = None
