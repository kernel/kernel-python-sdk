# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SingleUseCardBillingAddressParam"]


class SingleUseCardBillingAddressParam(TypedDict, total=False):
    """Billing address filled with the billing_* fill fields. Never returned."""

    city: str

    country: str
    """ISO 3166-1 alpha-2 code."""

    line1: str

    line2: str

    postal_code: str

    state: str
