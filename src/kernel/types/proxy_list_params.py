# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProxyListParams"]


class ProxyListParams(TypedDict, total=False):
    limit: int
    """Limit the number of proxies to return."""

    offset: int
    """Offset the number of proxies to return."""

    query: str
    """Case-insensitive substring match against proxy name, host, or IP address.

    IDs match by exact value.
    """
