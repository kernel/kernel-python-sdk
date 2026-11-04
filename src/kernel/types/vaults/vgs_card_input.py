# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["VgsCardInput"]


class VgsCardInput(BaseModel):
    """The card's aliases in the customer's VGS vault, its expiry and last four digits.

    Write-only: stored encrypted and never returned in the item, its events or logs. A repeated PUT with the same key must send the same card.
    """

    pass
