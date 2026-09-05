# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "OrgEntitlements",
    "Features",
    "FeaturesBrowserExtensions",
    "FeaturesBrowserPools",
    "FeaturesBrowserReplays",
    "FeaturesCredentialProviders",
    "FeaturesCredentials",
    "FeaturesCustomProxies",
    "FeaturesFileIo",
    "FeaturesGPU",
    "FeaturesManagedAuth",
    "FeaturesManagedProxies",
    "FeaturesProfiles",
    "FeaturesProxyBypassHosts",
    "FeaturesVaults",
    "Limits",
    "Plan",
]


class FeaturesBrowserExtensions(BaseModel):
    enabled: bool
    """Whether browser extensions are available."""

    max_stored_per_org: Optional[int] = None
    """Maximum active custom extensions the organization may store.

    Null means unlimited. Loading stored extensions into a browser is not
    plan-limited.
    """


class FeaturesBrowserPools(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesBrowserReplays(BaseModel):
    enabled: bool
    """Whether browser replay recording is available."""

    retention_days: int
    """Number of days browser replays are retained, matching the replay reaper policy."""


class FeaturesCredentialProviders(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesCredentials(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesCustomProxies(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesFileIo(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesGPU(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesManagedAuth(BaseModel):
    enabled: bool
    """Whether managed auth is available."""

    health_check_interval_default_seconds: int
    """
    Effective interval in seconds used when a connection is created without an
    explicit health-check interval.
    """

    health_check_interval_max_seconds: int
    """Maximum accepted managed auth health-check interval in seconds."""

    health_check_interval_min_seconds: int
    """Minimum accepted managed auth health-check interval in seconds."""

    max_connections: Optional[int] = None
    """Maximum active managed auth connections in the organization.

    Null means unlimited.
    """


class FeaturesManagedProxies(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesProfiles(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesProxyBypassHosts(BaseModel):
    enabled: bool
    """Whether the organization is entitled to use this feature."""


class FeaturesVaults(BaseModel):
    """
    Whether the organization can access vaults, using the same access check as vault API routes.
    """

    enabled: bool
    """Whether the organization is entitled to use this feature."""


class Features(BaseModel):
    browser_extensions: FeaturesBrowserExtensions

    browser_pools: FeaturesBrowserPools

    browser_replays: FeaturesBrowserReplays

    credential_providers: FeaturesCredentialProviders

    credentials: FeaturesCredentials

    custom_proxies: FeaturesCustomProxies

    file_io: FeaturesFileIo

    gpu: FeaturesGPU

    managed_auth: FeaturesManagedAuth

    managed_proxies: FeaturesManagedProxies

    profiles: FeaturesProfiles

    proxy_bypass_hosts: FeaturesProxyBypassHosts

    vaults: FeaturesVaults
    """
    Whether the organization can access vaults, using the same access check as vault
    API routes.
    """


class Limits(BaseModel):
    default_max_concurrent_invocations_per_app: int
    """
    Effective org-level default concurrent invocation ceiling for apps without an
    app-specific override. App-specific overrides are not represented here.
    """

    max_concurrent_browsers: int
    """
    Effective organization-wide ceiling shared by on-demand browsers and browser
    pool reservations.
    """

    max_concurrent_invocations: int
    """Effective organization-wide concurrent app invocation ceiling."""


class Plan(BaseModel):
    id: Literal["FREE", "HOBBYIST", "START_UP", "ENTERPRISE"]
    """The organization's contractual plan identifier.

    Use the resolved feature and limit values, not this field, for access decisions.
    """

    effective_id: Literal["FREE", "HOBBYIST", "START_UP", "ENTERPRISE"]
    """The plan used to resolve plan-based access.

    Active trials resolve to START_UP regardless of the contractual plan.
    """

    is_trialing: bool
    """Whether the organization is currently within its trial period."""

    status: Optional[Literal["NEEDS_PAYMENT_METHOD", "ACTIVE", "CANCELED", "UNPAID"]] = None
    """
    Current billing status of the contractual plan, or null when no billing status
    is recorded. Status-sensitive feature values already account for it.
    """

    trial_ends_at: Optional[datetime] = None
    """Configured trial end timestamp, or null when the organization has no trial.

    A past timestamp may be returned when is_trialing is false.
    """


class OrgEntitlements(BaseModel):
    """Effective feature access and constraints for the authenticated organization.

    Values already include trial treatment, plan status, and organization-specific overrides; consumers should use these resolved values instead of comparing plan IDs.
    """

    features: Features

    limits: Limits

    plan: Plan
