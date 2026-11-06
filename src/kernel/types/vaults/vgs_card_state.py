# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VgsCardState", "Masks"]


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


class VgsCardState(BaseModel):
    """A ready VGS card supports fill, then submit checkout, until expires_at.

    Kernel does not observe whether the merchant charged the card. masks.last4 is the card's last four digits.
    """

    provider: Literal["vgs"]

    status: Literal["requested", "pending_authorization", "ready", "expired", "declined", "recovery_required"]
    """
    requested until authorize reveals the aliases; if the reveal fails before
    anything is stored, authorize returns 503 provider_unavailable and the card
    stays requested. declined means authorize was refused: invalid_card for aliases
    that do not match the card or a card that has expired (fix the input and create
    a new card), alias_not_found when the customer's vault has no such alias,
    usually an expired CVC alias (collect the CVC again and create a new card), or
    provider_credentials_rejected when VGS refused the configuration's service
    account (update the provider configuration and create a new card). ready lasts
    until the CVC alias expires, then expired.
    """

    domains: Optional[List[str]] = None
    """Informational registrable domain.

    Fill is locked to merchant_url's exact origin.
    """

    masks: Optional[Masks] = None

    status_reason: Optional[str] = None
