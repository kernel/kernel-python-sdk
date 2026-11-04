# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["KernelSingleUseCard"]


class KernelSingleUseCard(BaseModel):
    """
    Details of a card the caller supplies, such as a single-use virtual card from its issuer. Mutually exclusive with payment_method_id. The card details are stored encrypted for fill and never returned; reads return only reference. Kernel deletes them shortly after the card's expires_at; deleting the card, its wallet or its vault deletes them immediately. A card whose expiry month has ended is rejected.
    """

    reference: Optional[str] = None
    """The caller's identifier for the card, such as the issuer's card ID.

    Returned unchanged on reads.
    """
