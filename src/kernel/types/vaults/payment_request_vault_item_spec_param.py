# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .kernel_payment_request_vault_item_spec_param import KernelPaymentRequestVaultItemSpecParam

__all__ = [
    "PaymentRequestVaultItemSpecParam",
    "LinkCardVaultItemSpec",
    "LinkCardVaultItemSpecLineItem",
    "LinkCardVaultItemSpecLineItemTotal",
    "LinkCardVaultItemSpecRecurring",
    "LinkCardVaultItemSpecTotal",
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

    Test-mode card creation is not supported. The spec can be changed with PATCH until the card is authorized at a checkout. Authorize it with the browser at final checkout: Kernel inspects the checkout through WebMCP and internally chooses a merchant-bound Link Pay Token when supported or a virtual card otherwise. Callers never receive or choose how the credential is delivered.
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


PaymentRequestVaultItemSpecParam: TypeAlias = Union[LinkCardVaultItemSpec, KernelPaymentRequestVaultItemSpecParam]
