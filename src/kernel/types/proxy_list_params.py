# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProxyListParams"]


class ProxyListParams(TypedDict, total=False):
    ip_address: str
    """Exact match on the primary exit IP of ISP proxies.

    Must be an IPv4 address. Only ISP proxies are matched: the ip_address shown on
    other proxy types is a one-time observation, not a stable identity.
    """

    limit: int
    """Limit the number of proxies to return."""

    name: str
    """Exact-match filter on proxy name using the database collation.

    In production, matching is case- and accent-insensitive. Names are not required
    to be unique, so multiple proxies may match.
    """

    offset: int
    """Offset the number of proxies to return."""

    query: str
    """Case-insensitive substring match against proxy name, host, or IP address.

    IDs match by exact value.
    """
