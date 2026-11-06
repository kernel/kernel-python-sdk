# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ProxyCreateParams",
    "Config",
    "ConfigIspProxyConfig",
    "ConfigResidentialProxyConfig",
    "ConfigMobileProxyConfig",
    "ConfigCreateCustomProxyConfig",
]


class ProxyCreateParams(TypedDict, total=False):
    type: Required[Literal["isp", "residential", "mobile", "custom"]]

    bypass_hosts: SequenceNotStr[str]
    """Hostnames that should bypass the parent proxy and connect directly."""

    config: Config
    """Configuration for an ISP proxy."""

    name: str
    """Readable name of the proxy."""

    protocol: Literal["http", "https"]
    """Protocol to use for the proxy connection."""


class ConfigIspProxyConfig(TypedDict, total=False):
    """Configuration for an ISP proxy."""

    country: str
    """ISO 3166 country code.

    Supported countries are US, GB, FR, DE, SG, and KR. Defaults to US if not
    provided, or to the country of ip_address when that is set.
    """

    ip_address: str
    """Reserved exit IP to pin the proxy to.

    Available only to organizations with a reserved ISP allocation; the IP must be
    active in it (see GET /proxy_ips) and, when country is also set, in that
    country. Omit to let Kernel choose an IP. A proxy read includes it only when the
    proxy's primary exit IP is one of the organization's reserved IPs; every ISP
    proxy's exit IP is on the top-level ip_address. An IP outside the allocation is
    rejected with code ip_not_reserved; one that cannot currently be assigned, with
    409 ip_unavailable.
    """


class ConfigResidentialProxyConfig(TypedDict, total=False):
    """Configuration for residential proxies."""

    asn: str
    """Autonomous system number. See https://bgp.potaroo.net/cidr/autnums.html"""

    city: str
    """City name (no spaces, e.g.

    `sanfrancisco`). If provided, `country` must also be provided.
    """

    country: str
    """ISO 3166 country code.

    If omitted, the proxy uses the global pool without country targeting.
    """

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
    """ISO 3166 country code.

    If omitted, the proxy uses the global pool without country targeting.
    """

    state: str
    """US-only state code. Mobile carrier routing can make observed geo vary."""


class ConfigCreateCustomProxyConfig(TypedDict, total=False):
    """Configuration for a custom proxy (e.g., private proxy server)."""

    host: Required[str]
    """Proxy host address or IP."""

    port: Required[int]
    """Proxy port."""

    ca_bundle: str
    """PEM-encoded CA certificate bundle the proxy re-signs upstream TLS with.

    Provide when the proxy terminates TLS (MITM) so the browser trusts its
    certificates. May contain multiple concatenated certificates.
    """

    password: str
    """Password for proxy authentication."""

    username: str
    """Username for proxy authentication."""


Config: TypeAlias = Union[
    ConfigIspProxyConfig, ConfigResidentialProxyConfig, ConfigMobileProxyConfig, ConfigCreateCustomProxyConfig
]
