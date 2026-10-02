# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .kernel_card_vault_item_spec import KernelCardVaultItemSpec

__all__ = [
    "CardVaultItemSpec",
    "LinkCardVaultItemSpec",
    "LinkCardVaultItemSpecLineItem",
    "LinkCardVaultItemSpecLineItemTotal",
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


class LinkCardVaultItemSpecTotal(BaseModel):
    amount: int
    """Total amount in minor currency units."""

    display_text: str

    type: str


class LinkCardVaultItemSpec(BaseModel):
    """Live payment card. Test-mode card creation is not supported."""

    amount: int
    """Integer amount in minor currency units.

    Link permits at most 50000 per spend request.
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
    """Wallet item key used to mint this card."""

    expires_at: Optional[int] = None

    line_items: Optional[List[LinkCardVaultItemSpecLineItem]] = None

    metadata: Optional[Dict[str, str]] = None

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
    Union[LinkCardVaultItemSpec, AgentCardCardVaultItemSpec, KernelCardVaultItemSpec],
    PropertyInfo(discriminator="provider"),
]
