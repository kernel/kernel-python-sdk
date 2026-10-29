# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ShopPayCardState", "Masks"]


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


class ShopPayCardState(BaseModel):
    """Issued Shop Pay cards retain encrypted card material for the fill operation."""

    provider: Literal["shop_pay"]

    status: Literal[
        "requested", "pending_authorization", "ready", "consumed", "expired", "declined", "recovery_required"
    ]
    """declined covers a request the shopper declined or that was cancelled.

    consumed means the transaction outcome was reported with confirm_transaction;
    the card is no longer stored and cannot be filled again, whatever the outcome.
    recovery_required means a provider operation has an unresolved outcome and the
    card cannot be used. When status_reason says the provider refused retrieval
    before acceptance, no card was issued and a later read retries. Otherwise follow
    status_reason: recovery for issuance can be abandoned by deleting the card and
    creating a new one, and the shopper approves the new purchase separately.
    Recovery while reporting a merchant transaction cannot be deleted and must be
    reconciled with support.
    """

    domains: Optional[List[str]] = None

    masks: Optional[Masks] = None

    status_reason: Optional[str] = None
