# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProxyIPListParams"]


class ProxyIPListParams(TypedDict, total=False):
    country: str
    """ISO 3166 country code to filter by. Must be a country ISP proxies support."""

    limit: int
    """Limit the number of IPs to return."""

    offset: int
    """Offset the number of IPs to return."""

    status: Literal["active", "excluded"]
    """Filter by whether the IP can currently be assigned."""
