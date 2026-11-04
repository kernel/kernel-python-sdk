# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .kernel_single_use_card_param import KernelSingleUseCardParam

__all__ = ["KernelCardVaultItemSpecParam"]


class KernelCardVaultItemSpecParam(TypedDict, total=False):
    """One live purchase with a Kernel-enrolled card.

    Authorization obtains an agentic network token number, expiry and one-time 3-digit code. They are stored encrypted for the fill operation, which types them only on merchant_url's origin; the merchant's own checkout submits the payment. The one-time code is valid until the item's expires_at; fill and submit checkout before then. Mastercard purchases need no cardholder approval. A Visa purchase returns a spend_approval action: the cardholder approves it with a Visa passkey, and Kernel registers a Visa intent for one transaction up to the amount before issuing the code. For supported cards whose network cannot be enrolled for agentic tokens, authorize returns pending_authorization with a spend_approval action to collect a fresh security code in a hosted field. Once collected, the card is ready and can be filled before its expires_at, by default five minutes after collection. An expired card requires a new purchase. Fill types those details on merchant_url's origin. The amount, merchant_url and merchant_country are recorded but do not restrict payment requests sent by the browser. Card updates are not supported; delete and create a new item instead. With single_use_card the item is instead a single-use card whose details the caller supplies, such as a virtual card from its issuer. It is not funded by a payment method, is ready on creation, and supports only fill: Kernel stores the details encrypted, never returns them, and fills them on any https page whose registrable domain (state.domains) is merchant_url's, including its subdomains. Fill does not consume it. From expires_at it is expired and can no longer be filled; Kernel deletes its stored details shortly after expires_at. Deleting the card, its wallet or its vault deletes them immediately. amount, currency and the merchant fields are recorded but not enforced. Repeating the identical request returns the existing card; any other request with the same key returns 409, as does repeating it once the expired card's details have been deleted.
    """

    amount: Required[int]
    """
    Integer amount in minor currency units (at most 1000000), bound to the one-time
    code.
    """

    currency: Required[str]
    """ISO 4217 code.

    Supported: aud, brl, cad, chf, czk, dkk, eur, gbp, hkd, inr, jpy, krw, mxn, nok,
    nzd, pln, sek, sgd, usd, zar.
    """

    merchant_name: Required[str]

    merchant_url: Required[str]
    """Merchant checkout URL. Fill is allowed only on this URL's origin."""

    provider: Required[Literal["kernel"]]

    wallet: Required[str]
    """Key of the Kernel wallet item whose enrolled card pays."""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Single-use cards only.

    From this time the card is expired and can no longer be filled; Kernel deletes
    its stored details shortly after. Deleting the card, its wallet or its vault
    deletes them immediately. Defaults to 2 hours after creation, capped at the end
    of the card's expiry month; a requested time must be in the future, at most 24
    hours after creation, and not after the end of the card's expiry month. Returned
    in UTC.
    """

    merchant_category: str
    """Actual merchant category when known. Omit rather than invent a category."""

    merchant_category_code: str
    """Actual merchant MCC when known.

    Omit rather than invent a code. 0000 is not accepted.
    """

    merchant_country: str
    """The merchant's ISO 3166-1 alpha-2 country code.

    Required for Visa cards, whose one-time code is issued for the merchant's
    country.
    """

    payment_method_id: str
    """Wallet-scoped payment method ID from the wallet's payment_methods expansion.

    Omission selects the wallet's default card, ID card, for compatibility with
    existing requests; it never falls back to another method, and a wallet without a
    default card requires the ID. The purchase is bound to the method's enrolled
    card and network token, so later operations cannot switch funding. Not allowed
    with single_use_card.
    """

    single_use_card: KernelSingleUseCardParam
    """
    Details of a card the caller supplies, such as a single-use virtual card from
    its issuer. Mutually exclusive with payment_method_id. The card details are
    stored encrypted for fill and never returned; reads return only reference.
    Kernel deletes them shortly after the card's expires_at; deleting the card, its
    wallet or its vault deletes them immediately. A card whose expiry month has
    ended is rejected.
    """
