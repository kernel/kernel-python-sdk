# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProxyIP"]


class ProxyIP(BaseModel):
    """One IP address reserved for the organization's ISP proxies."""

    country: str
    """ISO 3166 country code of the IP."""

    ip_address: str
    """Reserved exit IP address."""

    status: Literal["active", "excluded"]
    """Whether the IP can currently be assigned.

    An excluded IP is listed but cannot be pinned or moved to; proxies already on it
    keep working.
    """
