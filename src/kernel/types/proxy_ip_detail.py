# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProxyIPDetail", "Proxy"]


class Proxy(BaseModel):
    """An ISP proxy whose primary exit is the reserved IP."""

    id: str

    name: Optional[str] = None


class ProxyIPDetail(BaseModel):
    """A reserved IP with the ISP proxies using it as their primary exit.

    Reservations are organization-wide, so proxy_count covers every project while proxies lists only those in the current project.
    """

    country: str
    """ISO 3166 country code of the IP."""

    ip_address: str
    """Reserved exit IP address."""

    proxies: List[Proxy]
    """ISP proxies in the current project whose primary exit IP is this address."""

    proxy_count: int
    """
    Number of ISP proxies across the organization whose primary exit IP is this
    address.
    """

    status: Literal["active", "excluded"]
    """Whether the IP can currently be assigned.

    An excluded IP is listed but cannot be pinned or moved to; proxies already on it
    keep working.
    """
