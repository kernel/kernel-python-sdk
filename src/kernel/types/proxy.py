# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "Proxy",
    "ConfigRegistryDirectProxy",
    "ConfigRegistryManagedProxy",
    "ConfigRegistryManagedProxyCreate",
    "ConfigRegistryManagedProxyCreateConfig",
    "ConfigRegistryManagedProxyCreateConfigDatacenterProxyConfig",
    "ConfigRegistryManagedProxyCreateConfigIspProxyConfig",
    "ConfigRegistryManagedProxyCreateConfigResidentialProxyConfig",
    "ConfigRegistryManagedProxyCreateConfigMobileProxyConfig",
    "ConfigRegistryManagedProxyCreateConfigCreateCustomProxyConfig",
]


class ConfigRegistryDirectProxy(BaseModel):
    """Direct egress recipe. Pass `{ "mode": "direct" }` as the browser's `proxy`."""

    mode: Literal["direct"]


class ConfigRegistryManagedProxyCreateConfigDatacenterProxyConfig(BaseModel):
    """Configuration for a datacenter proxy."""

    country: Optional[str] = None
    """ISO 3166 country code. Defaults to US if not provided."""


class ConfigRegistryManagedProxyCreateConfigIspProxyConfig(BaseModel):
    """Configuration for an ISP proxy."""

    country: Optional[str] = None
    """ISO 3166 country code.

    Supported countries are US, GB, FR, DE, and SG. Defaults to US if not provided.
    """


class ConfigRegistryManagedProxyCreateConfigResidentialProxyConfig(BaseModel):
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


class ConfigRegistryManagedProxyCreateConfigMobileProxyConfig(BaseModel):
    """Configuration for mobile proxies."""

    city: Optional[str] = None
    """Provider city alias. Mobile carrier routing can make observed geo vary."""

    country: Optional[str] = None
    """ISO 3166 country code.

    If omitted, the proxy uses the global pool without country targeting.
    """

    state: Optional[str] = None
    """US-only state code. Mobile carrier routing can make observed geo vary."""


class ConfigRegistryManagedProxyCreateConfigCreateCustomProxyConfig(BaseModel):
    """Configuration for a custom proxy (e.g., private proxy server)."""

    host: str
    """Proxy host address or IP."""

    port: int
    """Proxy port."""

    ca_bundle: Optional[str] = None
    """PEM-encoded CA certificate bundle the proxy re-signs upstream TLS with.

    Provide when the proxy terminates TLS (MITM) so the browser trusts its
    certificates. May contain multiple concatenated certificates.
    """

    password: Optional[str] = None
    """Password for proxy authentication."""

    username: Optional[str] = None
    """Username for proxy authentication."""


ConfigRegistryManagedProxyCreateConfig: TypeAlias = Union[
    ConfigRegistryManagedProxyCreateConfigDatacenterProxyConfig,
    ConfigRegistryManagedProxyCreateConfigIspProxyConfig,
    ConfigRegistryManagedProxyCreateConfigResidentialProxyConfig,
    ConfigRegistryManagedProxyCreateConfigMobileProxyConfig,
    ConfigRegistryManagedProxyCreateConfigCreateCustomProxyConfig,
]


class ConfigRegistryManagedProxyCreate(BaseModel):
    """Configuration for routing traffic through a proxy."""

    type: Literal["datacenter", "isp", "residential", "mobile", "custom"]
    """Proxy type to use.

    In terms of quality for avoiding bot-detection, from best to worst: `mobile` >
    `residential` > `isp` > `datacenter`.
    """

    bypass_hosts: Optional[List[str]] = None
    """Hostnames that should bypass the parent proxy and connect directly."""

    config: Optional[ConfigRegistryManagedProxyCreateConfig] = None
    """Configuration specific to the selected proxy `type`."""

    name: Optional[str] = None
    """Readable name of the proxy."""

    protocol: Optional[Literal["http", "https"]] = None
    """Protocol to use for the proxy connection."""


class ConfigRegistryManagedProxy(BaseModel):
    """Managed proxy recipe.

    `create` is a non-idempotent `POST /proxies` payload:
    create the resource once, retain its ID, and reuse that ID as the browser's
    `proxy.id`. Do not submit this recipe before every browser session.
    """

    create: ConfigRegistryManagedProxyCreate
    """Configuration for routing traffic through a proxy."""

    mode: Literal["managed"]


Proxy: TypeAlias = Annotated[
    Union[ConfigRegistryDirectProxy, ConfigRegistryManagedProxy], PropertyInfo(discriminator="mode")
]
