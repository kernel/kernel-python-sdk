# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WorkloadIdentityAuthorizationParam", "Policy", "PolicyStatement", "PolicyStatementCondition"]


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
    Allow statements for resources in this rule's project, in the same format as a scoped API key policy. API key actions are not allowed.
    """

    statements: Required[Iterable[PolicyStatement]]
    """Allow statements. Every action and resource not listed is denied."""


class WorkloadIdentityAuthorizationParam(TypedDict, total=False):
    policy: Required[Policy]
    """
    Allow statements for resources in this rule's project, in the same format as a
    scoped API key policy. API key actions are not allowed.
    """

    project_id: Required[str]
    """The one project credentials from this rule are limited to."""

    token_audience: Required[str]

    max_token_ttl_seconds: int
