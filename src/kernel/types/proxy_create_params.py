# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ProxyCreateParams",
    "Config",
    "ConfigDatacenterProxyConfig",
    "ConfigIspProxyConfig",
    "ConfigResidentialProxyConfig",
    "ConfigMobileProxyConfig",
    "ConfigCreateCustomProxyConfig",
]


class ProxyCreateParams(TypedDict, total=False):
    type: Required[Literal["datacenter", "isp", "residential", "mobile", "custom"]]
    """Proxy type to use.

    In terms of quality for avoiding bot-detection, from best to worst: `mobile` >
    `residential` > `isp` > `datacenter`.
    """

    bypass_hosts: SequenceNotStr[str]
    """Hostnames that should bypass the parent proxy and connect directly."""

    config: Config
    """Configuration specific to the selected proxy `type`."""

    name: str
    """Readable name of the proxy."""

    protocol: Literal["http", "https"]
    """Protocol to use for the proxy connection."""


class ConfigDatacenterProxyConfig(TypedDict, total=False):
    """Configuration for a datacenter proxy."""

    country: str
    """ISO 3166 country code. Defaults to US if not provided."""


class ConfigIspProxyConfig(TypedDict, total=False):
    """Configuration for an ISP proxy."""

    country: str
    """ISO 3166 country code. Defaults to US if not provided."""


class ConfigResidentialProxyConfig(TypedDict, total=False):
    """Configuration for residential proxies."""

    asn: str
    """Autonomous system number. See https://bgp.potaroo.net/cidr/autnums.html"""

    city: str
    """City name (no spaces, e.g.

    `sanfrancisco`). If provided, `country` must also be provided.
    """

    country: str
    """ISO 3166 country code."""

    os: Literal["windows", "macos", "android"]
    """Operating system of the residential device."""

    state: str
    """Two-letter state code."""

    zip: str
    """US ZIP code."""


class ConfigMobileProxyConfig(TypedDict, total=False):
    """Configuration for mobile proxies."""

    city: str
    """Provider city alias. Mobile carrier routing can make observed geo vary."""

    country: str
    """ISO 3166 country code"""

    state: str
    """US-only state code. Mobile carrier routing can make observed geo vary."""


class ConfigCreateCustomProxyConfig(TypedDict, total=False):
    """Configuration for a custom proxy (e.g., private proxy server)."""

    host: Required[str]
    """Proxy host address or IP."""

    port: Required[int]
    """Proxy port."""

    password: str
    """Password for proxy authentication."""

    username: str
    """Username for proxy authentication."""


Config: TypeAlias = Union[
    ConfigDatacenterProxyConfig,
    ConfigIspProxyConfig,
    ConfigResidentialProxyConfig,
    ConfigMobileProxyConfig,
    ConfigCreateCustomProxyConfig,
]
