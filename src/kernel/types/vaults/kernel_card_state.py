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
    """
    A ready Kernel card retains its encrypted network token and one-time code for the fill operation until the item's expires_at. Fill and submit checkout before then. Visa cards can be enrolled, but Visa purchases are not yet supported and authorize returns 400; supported Mastercard purchases need no cardholder approval. masks.last4 is the enrolled card's last four digits; masks.token_last4 is the network token's last four digits shown to the merchant. Kernel cards do not expose aliases or support egress substitution. Kernel does not observe whether the merchant charged the card.
    """

    provider: Literal["kernel"]

    status: Literal[
        "requested", "pending_authorization", "ready", "consumed", "expired", "declined", "recovery_required"
    ]
    """recovery_required means issuing the one-time code has an unresolved outcome.

    Kernel never issues another code for the item automatically, and the item cannot
    be deleted or replaced until the original attempt is reconciled with support.
    When status_reason says the provider refused retrieval before acceptance, no
    code was issued and a later read retries.
    """

    domains: Optional[List[str]] = None
    """Informational registrable domain.

    Fill is locked to merchant_url's exact origin.
    """

    masks: Optional[Masks] = None

    status_reason: Optional[str] = None
