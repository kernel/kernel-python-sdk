# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIKeyCreateParams", "Policy", "PolicyStatement"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """Label for the API key (1-255 characters). API keys are not addressable by name."""

    days_to_expire: Optional[int]
    """Number of days until expiry, up to 3650.

    Use null for never. Cannot be combined with expires_at.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Exact expiry time.

    Must be in the future and no later than the issuing credential's own expiry.
    Cannot be combined with days_to_expire.
    """

    policy: Policy
    """
    Issue a scoped key that may only perform the listed actions on the listed
    resources.
    """

    project_id: Optional[str]
    """Unique project identifier"""


class PolicyStatement(TypedDict, total=False):
    action: Required[str]
    """Permitted action, such as browsers:use or vaults:read."""

    resource: Required[str]
    """Resource the action applies to, in the format projects/{project_id}/{kind}/{id}.

    Wildcards are supported.
    """


class Policy(TypedDict, total=False):
    """
    Issue a scoped key that may only perform the listed actions on the listed resources.
    """

    statements: Required[Iterable[PolicyStatement]]
    """Allow statements. Every action and resource not listed is denied."""
