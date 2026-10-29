# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShopPayCardVaultItemSpecParam", "Total", "LineItem"]


class Total(TypedDict, total=False):
    amount: Required[int]
    """Amount in minor currency units; discounts are negative."""

    type: Required[str]
    """For example subtotal, fulfillment, tax, discount or total."""


class LineItem(TypedDict, total=False):
    name: Required[str]

    quantity: Required[int]

    unit_amount: Required[int]
    """Unit price in minor currency units."""


class ShopPayCardVaultItemSpecParam(TypedDict, total=False):
    """Shop Pay purchase.

    amount is the limit the shopper approves; totals must include exactly one positive total no higher than it. context is shown to the shopper when they approve. Authorize it with the browser at final checkout: Kernel sends that page to Shop as the merchant and the card fills only on its origin. Without browser_id and page_url it authorizes for merchant_url. authorize returns an approval action for the shopper, who approves the purchase in Shop; share its URL unchanged when present. Report the merchant outcome with confirm_transaction, which ends the card.
    """

    amount: Required[int]
    """Approval limit in minor currency units, at most 1000000."""

    context: Required[str]
    """What is being bought and why, written for the shopper."""

    currency: Required[str]
    """Shop accepts USD spend requests only."""

    merchant_name: Required[str]

    merchant_url: Required[str]
    """The merchant's https URL."""

    provider: Required[Literal["shop_pay"]]

    totals: Required[Iterable[Total]]

    wallet: Required[str]
    """Connected Shop Pay wallet item key."""

    line_items: Iterable[LineItem]

    merchant_country: str
    """ISO 3166-1 alpha-2 country of the merchant."""

    payment_method_id: str
    """Card ID from the wallet's payment_methods expansion.

    Omit it to use the shopper's preferred card.
    """
