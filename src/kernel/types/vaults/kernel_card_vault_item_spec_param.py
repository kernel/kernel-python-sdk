# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["KernelCardVaultItemSpecParam"]


class KernelCardVaultItemSpecParam(TypedDict, total=False):
    """One live purchase with a Kernel-enrolled card.

    Authorization obtains an agentic network token number, expiry and one-time 3-digit code. They are stored encrypted for the fill operation, which types them only on merchant_url's origin; the merchant's own checkout submits the payment. The one-time code is valid until the item's expires_at; fill and submit checkout before then. Mastercard purchases need no cardholder approval. A Visa purchase returns a spend_approval action: the cardholder approves it with a Visa passkey, and Kernel registers a Visa intent for one transaction up to the amount before issuing the code. Card updates are not supported; delete and create a new item instead.
    """

    amount: Required[int]
    """
    Integer amount in minor currency units (at most 50000), bound to the one-time
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
