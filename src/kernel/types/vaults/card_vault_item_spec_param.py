# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .vgs_card_vault_item_spec_param import VgsCardVaultItemSpecParam
from .kernel_card_vault_item_spec_param import KernelCardVaultItemSpecParam
from .shop_pay_card_vault_item_spec_param import ShopPayCardVaultItemSpecParam

__all__ = [
    "CardVaultItemSpecParam",
    "LinkCardVaultItemSpec",
    "LinkCardVaultItemSpecLineItem",
    "LinkCardVaultItemSpecLineItemTotal",
    "LinkCardVaultItemSpecRecurring",
    "LinkCardVaultItemSpecTotal",
    "AgentCardCardVaultItemSpec",
    "AgentCardCardVaultItemSpecLineItem",
]


class LinkCardVaultItemSpecLineItemTotal(TypedDict, total=False):
    amount: Required[int]
    """Total amount in minor currency units."""

    display_text: Required[str]

    type: Required[str]


class LinkCardVaultItemSpecLineItem(TypedDict, total=False):
    name: Required[str]

    description: str

    image_url: str

    product_url: str

    quantity: int

    sku: str

    totals: Iterable[LinkCardVaultItemSpecLineItemTotal]

    unit_amount: int
    """Unit amount in minor currency units."""

    url: str


class LinkCardVaultItemSpecRecurring(TypedDict, total=False):
    """Recurring terms for a subscription or other repeated purchase.

    The amount becomes the spending limit for each period of interval_count intervals, for example every 2 weeks. The merchant schedules charges. The card stays ready after each charge until it expires or is deleted; do not create a new card each period. Deleting the card, its wallet or its vault first cancels the credential with Link, so later charges decline; if Link cannot be reached, deletion returns 409 provider_revocation_pending and should be retried. Deletion does not cancel the subscription with the merchant. Recurring terms cannot be changed once the card is authorized.
    """

    interval: Required[Literal["day", "week", "month", "year"]]

    interval_count: int
    """Number of intervals per period. Link defaults it to 1."""


class LinkCardVaultItemSpecTotal(TypedDict, total=False):
    amount: Required[int]
    """Total amount in minor currency units."""

    display_text: Required[str]

    type: Required[str]


class LinkCardVaultItemSpec(TypedDict, total=False):
    """Live Link card request.

    Test-mode card creation is not supported. The spec can be changed with PATCH until the card is authorized at a checkout. Authorize it with the browser at final checkout: Kernel inspects the checkout through WebMCP and internally chooses a merchant-bound Link Pay Token when supported or a virtual card otherwise. Callers do not choose how the credential is delivered; after authorize, state.credential_type reports it.
    """

    amount: Required[int]
    """Integer amount in minor currency units, at most 50000.

    With recurring, the spending limit per period, not a lifetime total.
    """

    context: Required[str]

    currency: Required[str]

    merchant_name: Required[str]

    merchant_url: Required[str]

    payment_method_id: Required[str]
    """Payment-method ID returned by the referenced wallet's payment-method listing.

    The provider decides whether the selected funding method can satisfy the card
    request.
    """

    provider: Required[Literal["link"]]

    wallet: Required[str]
    """Connected Link wallet item key."""

    line_items: Iterable[LinkCardVaultItemSpecLineItem]

    metadata: Dict[str, str]

    recurring: LinkCardVaultItemSpecRecurring
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

    totals: Iterable[LinkCardVaultItemSpecTotal]


class AgentCardCardVaultItemSpecLineItem(TypedDict, total=False):
    """One product on the AgentCard approval screen."""

    quantity: Required[int]

    title: Required[str]
    """The product's name as the store shows it."""

    amount: int
    """The line's total in minor currency units.

    Shown instead of unit_amount times quantity when both are set; a line with
    neither shows without a price.
    """

    brand: str
    """Shown beside the title."""

    image_url: str
    """https URL of the product's picture.

    AgentCard shows pictures only from the image hosts it allows and shows the line
    without one otherwise.
    """

    options: str
    """The options the shopper chose, such as "Size S · Pink"."""

    unit_amount: int
    """Price of one, in minor currency units.

    The line shows unit_amount times quantity.
    """


class AgentCardCardVaultItemSpec(TypedDict, total=False):
    """AgentCard reusable live payment card.

    Test-mode card creation is not supported. Each checkout creates an authorization for spec.merchant / spec.amount that the cardholder approves, unless AgentCard runs it under one of the cardholder's autopilot rules. The card stays ready after each authorization.
    """

    amount: Required[int]
    """Integer amount in minor currency units."""

    currency: Required[str]

    merchant: Required[str]
    """Merchant name shown on the cardholder's approval screen."""

    provider: Required[Literal["agentcard"]]

    wallet: Required[str]
    """Wallet item key used to authorize checkouts."""

    card_id: str
    """Opaque card ID returned by AgentCard for a card in the connected wallet.

    Pass it through unchanged without assuming a prefix or format. Omitted, the
    cardholder picks on the approval screen.
    """

    checkout_origin: str
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

    discount: int
    """Discount as a positive number of minor currency units; 500 takes 5.00 off.

    Requires line_items.
    """

    line_items: Iterable[AgentCardCardVaultItemSpecLineItem]
    """
    What the next checkout buys, listed on the cardholder's approval screen above
    the total. Display only: the cardholder approves amount, or the amount the
    processor charges, and a line total that disagrees with it changes nothing they
    pay. Amounts are in minor units of currency. Sent only for checkouts without a
    preparation; omitted, the approval screen shows the merchant and amount alone.
    Card updates replace the whole spec, so set the cart again for each checkout.
    """

    shipping: int
    """Shipping charge in minor currency units. Requires line_items."""

    subtotal: int
    """Cart subtotal in minor currency units. Requires line_items."""

    tax: int
    """Tax in minor currency units. Requires line_items."""


CardVaultItemSpecParam: TypeAlias = Union[
    LinkCardVaultItemSpec,
    AgentCardCardVaultItemSpec,
    KernelCardVaultItemSpecParam,
    ShopPayCardVaultItemSpecParam,
    VgsCardVaultItemSpecParam,
]
