# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VgsCardInputParam"]


class VgsCardInputParam(TypedDict, total=False):
    """The card supplied to a purchase, as aliases in the customer's VGS vault.

    With card_mode full it is a whole card: a persistent alias of its number, a freshly collected volatile alias of its security code, its expiry and its last four digits. With card_mode cvc_only it is a CVC alias alone, because the merchant holds the rest on file. pan_alias, exp_month, exp_year and last4 are required with card_mode full and rejected with card_mode cvc_only. Write-only: stored encrypted and never returned in the item, its events or logs. A repeated PUT with the same key must send the same card.
    """

    cvc_alias: Required[str]
    """A volatile alias of a freshly collected security code in the customer's vault.

    It must still exist when authorize runs. Required in both modes.
    """

    exp_month: int
    """Required with card_mode full, rejected with card_mode cvc_only."""

    exp_year: int
    """Required with card_mode full, rejected with card_mode cvc_only."""

    last4: str
    """The card number's last four digits, checked against the revealed alias.

    Required with card_mode full, rejected with card_mode cvc_only.
    """

    pan_alias: str
    """A persistent alias of the card number in the customer's vault.

    Required with card_mode full, rejected with card_mode cvc_only.
    """
