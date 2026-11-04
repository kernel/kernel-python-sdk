# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SingleUseCardBillingAddress"]


class SingleUseCardBillingAddress(BaseModel):
    """Billing address filled with the billing_* fill fields. Never returned."""

    city: Optional[str] = None

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 code."""

    line1: Optional[str] = None

    line2: Optional[str] = None

    postal_code: Optional[str] = None

    state: Optional[str] = None
