# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LinkShippingAddress", "Address"]


class Address(BaseModel):
    """Link's nullable postal address fields.

    Omitted from the shipping address when Link reports null.
    """

    administrative_area: Optional[str] = None
    """State, province or region."""

    country_code: Optional[str] = None

    dependent_locality: Optional[str] = None

    line_1: Optional[str] = None

    line_2: Optional[str] = None

    locality: Optional[str] = None
    """City or town."""

    name: Optional[str] = None

    postal_code: Optional[str] = None

    sorting_code: Optional[str] = None


class LinkShippingAddress(BaseModel):
    """
    One entry of Link's `GET /shipping_addresses` response, passed through as Link reports it. Kernel never stores it.
    """

    id: str
    """Link shipping address ID."""

    is_default: bool

    nickname: Optional[str] = None

    address: Optional[Address] = None
    """Link's nullable postal address fields.

    Omitted from the shipping address when Link reports null.
    """
