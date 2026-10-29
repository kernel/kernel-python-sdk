# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ShopPayCardVaultItemSpec", "Total", "LineItem"]


class Total(BaseModel):
    amount: int
    """Amount in minor currency units; discounts are negative."""

    type: str
    """For example subtotal, fulfillment, tax, discount or total."""


class LineItem(BaseModel):
    name: str

    quantity: int

    unit_amount: int
    """Unit price in minor currency units."""


class ShopPayCardVaultItemSpec(BaseModel):
    """Shop Pay purchase.

    amount is the limit the shopper approves; totals must include exactly one positive total no higher than it. context is shown to the shopper when they approve. Authorize it with the browser at final checkout: Kernel sends that page to Shop as the merchant and the card fills only on its origin. Without browser_id and page_url it authorizes for merchant_url. authorize returns an approval action for the shopper, who approves the purchase in Shop; share its URL unchanged when present. Report the merchant outcome with confirm_transaction, which ends the card.
    """

    amount: int
    """Approval limit in minor currency units, at most 1000000."""

    context: str
    """What is being bought and why, written for the shopper."""

    currency: str
    """Shop accepts USD spend requests only."""

    merchant_name: str

    merchant_url: str
    """The merchant's https URL."""

    provider: Literal["shop_pay"]

    totals: List[Total]

    wallet: str
    """Connected Shop Pay wallet item key."""

    line_items: Optional[List[LineItem]] = None

    merchant_country: Optional[str] = None
    """ISO 3166-1 alpha-2 country of the merchant."""

    payment_method_id: Optional[str] = None
    """Card ID from the wallet's payment_methods expansion.

    Omit it to use the shopper's preferred card.
    """
