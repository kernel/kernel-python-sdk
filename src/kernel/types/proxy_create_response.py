# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ProxyCreateResponse",
    "Config",
    "ConfigIspProxyConfig",
    "ConfigResidentialProxyConfig",
    "ConfigMobileProxyConfig",
    "ConfigCustomProxyConfig",
]


class ConfigIspProxyConfig(BaseModel):
    """Configuration for an ISP proxy."""

    country: Optional[str] = None
    """ISO 3166 country code.

    Supported countries are US, GB, FR, DE, SG, and KR. Defaults to US if not
    provided, or to the country of ip_address when that is set.
    """

    ip_address: Optional[str] = None
    """Reserved exit IP to pin the proxy to.

    Available only to organizations with a reserved ISP allocation; the IP must be
    active in it (see GET /proxy_ips) and, when country is also set, in that
    country. Omit to let Kernel choose an IP. A proxy read includes it only when the
    proxy's primary exit IP is one of the organization's reserved IPs; every ISP
    proxy's exit IP is on the top-level ip_address. An IP outside the allocation is
    rejected with code ip_not_reserved; one that cannot currently be assigned, with
    409 ip_unavailable.
    """


class ConfigResidentialProxyConfig(BaseModel):
    """Configuration for residential proxies."""

    asn: Optional[str] = None
    """Autonomous system number. See https://bgp.potaroo.net/cidr/autnums.html"""

    city: Optional[str] = None
    """City name (no spaces, e.g.

    `sanfrancisco`). If provided, `country` must also be provided.
    """

    country: Optional[str] = None
    """ISO 3166 country code.

    If omitted, the proxy uses the global pool without country targeting.
    """

    os: Optional[Literal["windows", "macos", "android"]] = None
    """Operating system of the residential device."""

    state: Optional[str] = None
    """Two-letter state code."""

    zip: Optional[str] = None
    """US ZIP code."""


class ConfigMobileProxyConfig(BaseModel):
    """Configuration for mobile proxies."""

    city: Optional[str] = None
    """Provider city alias. Mobile carrier routing can make observed geo vary."""

    country: Optional[str] = None
    """ISO 3166 country code.

    If omitted, the proxy uses the global pool without country targeting.
    """

    state: Optional[str] = None
    """US-only state code. Mobile carrier routing can make observed geo vary."""


class ConfigCustomProxyConfig(BaseModel):
    """Configuration for a custom proxy (e.g., private proxy server)."""

    host: str
    """Proxy host address or IP."""

    port: int
    """Proxy port."""

    has_ca_bundle: Optional[bool] = None
    """Whether the proxy has a custom CA bundle configured."""

    has_password: Optional[bool] = None
    """Whether the proxy has a password."""

    username: Optional[str] = None
    """Username for proxy authentication."""


Config: TypeAlias = Union[
    ConfigIspProxyConfig, ConfigResidentialProxyConfig, ConfigMobileProxyConfig, ConfigCustomProxyConfig
]


class ProxyCreateResponse(BaseModel):
    """Configuration for routing traffic through a proxy."""

    type: Literal["isp", "residential", "mobile", "custom"]

    id: Optional[str] = None

    bypass_hosts: Optional[List[str]] = None
    """Hostnames that should bypass the parent proxy and connect directly."""

    config: Optional[Config] = None
    """Configuration for an ISP proxy."""

    ip_address: Optional[str] = None
    """IP address that the proxy uses when making requests."""

    last_checked: Optional[datetime] = None
    """Timestamp of the last health check performed on this proxy."""

    name: Optional[str] = None
    """Readable name of the proxy."""

    protocol: Optional[Literal["http", "https"]] = None
    """Protocol to use for the proxy connection."""

    status: Optional[Literal["available", "unavailable"]] = None
    """Current health status of the proxy."""
