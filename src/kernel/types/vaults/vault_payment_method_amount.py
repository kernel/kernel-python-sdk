# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["VaultPaymentMethodAmount"]


class VaultPaymentMethodAmount(BaseModel):
    amount: int
    """Amount in the currency's smallest unit, for example cents for USD."""

    currency: str
    """Lowercase ISO 4217 currency code."""
