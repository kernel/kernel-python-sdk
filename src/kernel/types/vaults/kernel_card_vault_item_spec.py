# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KernelCardVaultItemSpec"]


class KernelCardVaultItemSpec(BaseModel):
    """One live purchase with a Kernel-enrolled card.

    Authorization obtains an agentic network token number, expiry and one-time 3-digit code. They are stored encrypted for the fill operation, which types them only on merchant_url's origin; the merchant's own checkout submits the payment. The one-time code is valid until the item's expires_at; fill and submit checkout before then. Visa cards can be enrolled, but Visa purchases are not yet supported: authorize returns 400. Supported Mastercard purchases need no cardholder approval. Card updates are not supported; delete and create a new item instead.
    """

    amount: int
    """
    Integer amount in minor currency units (at most 50000), bound to the one-time
    code.
    """

    currency: str
    """ISO 4217 code.

    Supported: aud, brl, cad, chf, czk, dkk, eur, gbp, hkd, inr, jpy, krw, mxn, nok,
    nzd, pln, sek, sgd, usd, zar.
    """

    merchant_name: str

    merchant_url: str
    """Merchant checkout URL. Fill is allowed only on this URL's origin."""

    provider: Literal["kernel"]

    wallet: str
    """Key of the Kernel wallet item whose enrolled card pays."""
