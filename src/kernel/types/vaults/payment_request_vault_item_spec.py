# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .kernel_payment_request_vault_item_spec import KernelPaymentRequestVaultItemSpec

__all__ = [
    "PaymentRequestVaultItemSpec",
    "LinkCardVaultItemSpec",
    "LinkCardVaultItemSpecLineItem",
    "LinkCardVaultItemSpecLineItemTotal",
    "LinkCardVaultItemSpecRecurring",
    "LinkCardVaultItemSpecTotal",
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


PaymentRequestVaultItemSpec: TypeAlias = Annotated[
    Union[LinkCardVaultItemSpec, KernelPaymentRequestVaultItemSpec], PropertyInfo(discriminator="provider")
]
