# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["APIKeyCreateParams", "Policy", "PolicyStatement", "PolicyStatementCondition"]


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
    resources. A statement may carry a condition; a `source_ip` condition restricts
    the statement to requests from inside its CIDR networks.
    """

    project_id: Optional[str]
    """Unique project identifier"""

    service_account_id: str
    """Link to an active same-organization service account.

    Requires an organization administrator, explicit project and nonempty policy.
    Omit for a personal key.
    """


class PolicyStatementCondition(TypedDict, total=False):
    """
    A condition narrows a policy statement to requests matching its constraint: the request attribute, a comparison operator, and that operator's values.
    """

    key: Required[Literal["source_ip"]]
    """Request attribute the condition constrains.

    `source_ip` restricts the statement to requests whose client address falls
    inside one of `values`.
    """

    operator: Required[Literal["in"]]
    """Comparison the condition applies between the request attribute and values."""

    values: Required[SequenceNotStr[str]]
    """Values the request attribute must match.

    For `source_ip`, CIDR networks: a bare address without a mask is rejected, and
    so are an entry with host bits set and an IPv4 network written in IPv6 notation.
    """


class PolicyStatement(TypedDict, total=False):
    action: Required[str]
    """Permitted action, such as browsers:use or vaults:read.

    When creating an API key or replacing its policy, `*` may replace whole
    components as shorthand: browsers:_ names every browsers action, _:delete every
    delete action the resource can carry, and _:_ every action the resource can
    carry. The stored policy lists the concrete actions, so actions added later are
    not granted, and api_keys:issue_beyond_expiry must always be listed explicitly.
    Partial components such as brow*:use and a bare * are rejected. Other policies,
    such as workload identity rules and deployment runtime policies, accept only
    exact actions.
    """

    resource: Required[str]
    """Resource the action applies to, in the format projects/{project_id}/{kind}/{id}.

    Wildcards are supported.
    """

    condition: PolicyStatementCondition
    """
    A condition narrows a policy statement to requests matching its constraint: the
    request attribute, a comparison operator, and that operator's values.
    """


class Policy(TypedDict, total=False):
    """
    Issue a scoped key that may only perform the listed actions on the listed resources. A statement may carry a condition; a `source_ip` condition restricts the statement to requests from inside its CIDR networks.
    """

    statements: Required[Iterable[PolicyStatement]]
    """Allow statements. Every action and resource not listed is denied."""
