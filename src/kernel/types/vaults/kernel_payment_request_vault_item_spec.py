# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KernelPaymentRequestVaultItemSpec"]


class KernelPaymentRequestVaultItemSpec(BaseModel):
    """
    One live purchase funded by the Kernel wallet payment method named by payment_method_id. The method must be active and eligible when the request is created. The purchase is bound to that method; later operations cannot switch funding, and removing the method makes the purchase unusable rather than moving it to another card. Approval, issuance, fill and the alias fallback behave as described for KernelCardVaultItemSpec.
    """

    amount: int
    """
    Integer amount in minor currency units (at most 1000000), bound to the one-time
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

    payment_method_id: str
    """Payment method ID from the wallet's payment_methods expansion."""

    provider: Literal["kernel"]

    wallet: str
    """Key of the Kernel wallet item that owns the payment method."""

    merchant_category: Optional[str] = None
    """Actual merchant category when known. Omit rather than invent a category."""

    merchant_category_code: Optional[str] = None
    """Actual merchant MCC when known.

    Omit rather than invent a code. 0000 is not accepted.
    """

    merchant_country: Optional[str] = None
    """The merchant's ISO 3166-1 alpha-2 country code.

    Required for Visa cards, whose one-time code is issued for the merchant's
    country.
    """
