# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["VgsCardInput"]


class VgsCardInput(BaseModel):
    """The card's aliases in the customer's VGS vault, its expiry and last four digits.

    Write-only: stored encrypted and never returned in the item, its events or logs. A repeated PUT with the same key must send the same card.
    """

    cvc_alias: str
    """A volatile alias of a freshly collected security code in the customer's vault.

    It must still exist when authorize runs.
    """

    exp_month: int

    exp_year: int

    last4: str
    """The card number's last four digits, checked against the revealed alias."""

    pan_alias: str
    """A persistent alias of the card number in the customer's vault."""
