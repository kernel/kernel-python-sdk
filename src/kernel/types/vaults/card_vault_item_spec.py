# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .kernel_card_vault_item_spec import KernelCardVaultItemSpec
from .shop_pay_card_vault_item_spec import ShopPayCardVaultItemSpec

__all__ = [
    "CardVaultItemSpec",
    "LinkCardVaultItemSpec",
    "LinkCardVaultItemSpecLineItem",
    "LinkCardVaultItemSpecLineItemTotal",
    "LinkCardVaultItemSpecRecurring",
    "LinkCardVaultItemSpecTotal",
    "AgentCardCardVaultItemSpec",
]


class LinkCardVaultItemSpecLineItemTotal(BaseModel):
    amount: int
    """Total amount in minor currency units."""

    display_text: str

    type: str


class LinkCardVaultItemSpecLineItem(BaseModel):
    name: str

    description: Optional[str] = None

    image_url: Optional[str] = None

    product_url: Optional[str] = None

    quantity: Optional[int] = None

    sku: Optional[str] = None

    totals: Optional[List[LinkCardVaultItemSpecLineItemTotal]] = None

    unit_amount: Optional[int] = None
    """Unit amount in minor currency units."""

    url: Optional[str] = None


class LinkCardVaultItemSpecRecurring(BaseModel):
    """Recurring terms for a subscription or other repeated purchase.

    The amount becomes the spending limit for each period of interval_count intervals, for example every 2 weeks. The merchant schedules charges. The card stays ready after each charge until it expires or is deleted; do not create a new card each period. Deleting the card, its wallet or its vault first cancels the credential with Link, so later charges decline; if Link cannot be reached, deletion returns 409 provider_revocation_pending and should be retried. Deletion does not cancel the subscription with the merchant. Recurring terms cannot be changed once the card is authorized.
    """

    interval: Literal["day", "week", "month", "year"]

    interval_count: Optional[int] = None
    """Number of intervals per period. Link defaults it to 1."""


class LinkCardVaultItemSpecTotal(BaseModel):
    amount: int
    """Total amount in minor currency units."""

    display_text: str

    type: str


class LinkCardVaultItemSpec(BaseModel):
    """Live Link card request.

    Test-mode card creation is not supported. The spec can be changed with PATCH until the card is authorized at a checkout. Authorize it with the browser at final checkout: Kernel inspects the checkout through WebMCP and internally chooses a merchant-bound Link Pay Token when supported or a virtual card otherwise. Callers never receive or choose how the credential is delivered.
    """

    amount: int
    """Integer amount in minor currency units, at most 50000.

    With recurring, the spending limit per period, not a lifetime total.
    """

    context: str

    currency: str

    merchant_name: str

    merchant_url: str

    payment_method_id: str
    """Payment-method ID returned by the referenced wallet's payment-method listing.

    The provider decides whether the selected funding method can satisfy the card
    request.
    """

    provider: Literal["link"]

    wallet: str
    """Connected Link wallet item key."""

    line_items: Optional[List[LinkCardVaultItemSpecLineItem]] = None

    metadata: Optional[Dict[str, str]] = None

    recurring: Optional[LinkCardVaultItemSpecRecurring] = None
    """Recurring terms for a subscription or other repeated purchase.

    The amount becomes the spending limit for each period of interval_count
    intervals, for example every 2 weeks. The merchant schedules charges. The card
    stays ready after each charge until it expires or is deleted; do not create a
    new card each period. Deleting the card, its wallet or its vault first cancels
    the credential with Link, so later charges decline; if Link cannot be reached,
    deletion returns 409 provider_revocation_pending and should be retried. Deletion
    does not cancel the subscription with the merchant. Recurring terms cannot be
    changed once the card is authorized.
    """

    totals: Optional[List[LinkCardVaultItemSpecTotal]] = None


class AgentCardCardVaultItemSpec(BaseModel):
    """AgentCard reusable live payment card.

    Test-mode card creation is not supported. Each checkout creates an authorization for spec.merchant / spec.amount that the cardholder approves, unless AgentCard runs it under one of the cardholder's autopilot rules. The card stays ready after each authorization.
    """

    amount: int
    """Integer amount in minor currency units."""

    currency: str

    merchant: str
    """Merchant name shown on the cardholder's approval screen."""

    provider: Literal["agentcard"]

    wallet: str
    """Wallet item key used to authorize checkouts."""

    card_id: Optional[str] = None
    """Opaque card ID returned by AgentCard for a card in the connected wallet.

    Pass it through unchanged without assuming a prefix or format. Omitted, the
    cardholder picks on the approval screen.
    """

    checkout_origin: Optional[str] = None
    """
    Origin of the top-level checkout page, such as https://shop.example.com: https,
    a lowercase host, a port only when it is not 443, and no path. http is accepted
    only for localhost test pages. Checkouts without a preparation send it to
    AgentCard, which uses it to match the cardholder's autopilot rules; prepared
    checkouts send the preparation's merchant_origin instead. Kernel sends the
    declared value and does not compare it with the page the browser has open.
    Omitted, those checkouts ask the cardholder to approve. Card updates replace the
    whole spec, so an update that omits it removes it.
    """


CardVaultItemSpec: TypeAlias = Annotated[
    Union[LinkCardVaultItemSpec, AgentCardCardVaultItemSpec, KernelCardVaultItemSpec, ShopPayCardVaultItemSpec],
    PropertyInfo(discriminator="provider"),
]
