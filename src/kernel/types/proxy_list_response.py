# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ProxyListResponse",
    "ProxyListResponseItem",
    "ProxyListResponseItemConfig",
    "ProxyListResponseItemConfigDatacenterProxyConfig",
    "ProxyListResponseItemConfigIspProxyConfig",
    "ProxyListResponseItemConfigResidentialProxyConfig",
    "ProxyListResponseItemConfigMobileProxyConfig",
    "ProxyListResponseItemConfigCustomProxyConfig",
]


class ProxyListResponseItemConfigDatacenterProxyConfig(BaseModel):
    """Configuration for a datacenter proxy."""

    country: Optional[str] = None
    """ISO 3166 country code. Defaults to US if not provided."""


class ProxyListResponseItemConfigIspProxyConfig(BaseModel):
    """Configuration for an ISP proxy."""

    country: Optional[str] = None
    """ISO 3166 country code. Defaults to US if not provided."""


class ProxyListResponseItemConfigResidentialProxyConfig(BaseModel):
    """Configuration for residential proxies."""

    asn: Optional[str] = None
    """Autonomous system number. See https://bgp.potaroo.net/cidr/autnums.html"""

    city: Optional[str] = None
    """City name (no spaces, e.g.

    `sanfrancisco`). If provided, `country` must also be provided.
    """

    country: Optional[str] = None
    """ISO 3166 country code."""

    os: Optional[Literal["windows", "macos", "android"]] = None
    """Operating system of the residential device."""

    state: Optional[str] = None
    """Two-letter state code."""

    zip: Optional[str] = None
    """US ZIP code."""


class ProxyListResponseItemConfigMobileProxyConfig(BaseModel):
    """Configuration for mobile proxies."""

    asn: Optional[str] = None
    """Autonomous system number. See https://bgp.potaroo.net/cidr/autnums.html"""

    carrier: Optional[
        Literal[
            "a1",
            "aircel",
            "airtel",
            "att",
            "celcom",
            "chinamobile",
            "claro",
            "comcast",
            "cox",
            "digi",
            "dt",
            "docomo",
            "dtac",
            "etisalat",
            "idea",
            "kyivstar",
            "meo",
            "megafon",
            "mtn",
            "mtnza",
            "mts",
            "optus",
            "orange",
            "qwest",
            "reliance_jio",
            "robi",
            "sprint",
            "telefonica",
            "telstra",
            "tmobile",
            "tigo",
            "tim",
            "verizon",
            "vimpelcom",
            "vodacomza",
            "vodafone",
            "vivo",
            "zain",
            "vivabo",
            "telenormyanmar",
            "kcelljsc",
            "swisscom",
            "singtel",
            "asiacell",
            "windit",
            "cellc",
            "ooredoo",
            "drei",
            "umobile",
            "cableone",
            "proximus",
            "tele2",
            "mobitel",
            "o2",
            "bouygues",
            "free",
            "sfr",
            "digicel",
        ]
    ] = None
    """Mobile carrier."""

    city: Optional[str] = None
    """City name (no spaces, e.g.

    `sanfrancisco`). If provided, `country` must also be provided.
    """

    country: Optional[str] = None
    """ISO 3166 country code"""

    state: Optional[str] = None
    """Two-letter state code."""

    zip: Optional[str] = None
    """US ZIP code."""


class ProxyListResponseItemConfigCustomProxyConfig(BaseModel):
    """Configuration for a custom proxy (e.g., private proxy server)."""

    host: str
    """Proxy host address or IP."""

    port: int
    """Proxy port."""

    has_password: Optional[bool] = None
    """Whether the proxy has a password."""

    username: Optional[str] = None
    """Username for proxy authentication."""


ProxyListResponseItemConfig: TypeAlias = Union[
    ProxyListResponseItemConfigDatacenterProxyConfig,
    ProxyListResponseItemConfigIspProxyConfig,
    ProxyListResponseItemConfigResidentialProxyConfig,
    ProxyListResponseItemConfigMobileProxyConfig,
    ProxyListResponseItemConfigCustomProxyConfig,
]


class ProxyListResponseItem(BaseModel):
    """Configuration for routing traffic through a proxy."""

    type: Literal["datacenter", "isp", "residential", "mobile", "custom"]
    """Proxy type to use.

    In terms of quality for avoiding bot-detection, from best to worst: `mobile` >
    `residential` > `isp` > `datacenter`.
    """

    id: Optional[str] = None

    config: Optional[ProxyListResponseItemConfig] = None
    """Configuration specific to the selected proxy `type`."""

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


ProxyListResponse: TypeAlias = List[ProxyListResponseItem]
