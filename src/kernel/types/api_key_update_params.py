# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["APIKeyUpdateParams", "Policy", "PolicyStatement", "PolicyStatementCondition"]


class APIKeyUpdateParams(TypedDict, total=False):
    name: str
    """New API key name"""

    policy: Policy
    """Permissions that fully replace the key's policy.

    Attaching a policy to a key without one makes the key scoped: every action and
    resource the policy does not list is denied. The key's credential, name,
    project, and expiry are unchanged, so consumers never need the key
    redistributed. A `source_ip` condition adds or changes IP allowlisting without
    rotating the credential. Requires api_keys:set_policy on the key.
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
    """Permitted action, such as browsers:use or vaults:read."""

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
    """Permissions that fully replace the key's policy.

    Attaching a policy to a key without one makes the key scoped: every action and resource the policy does not list is denied. The key's credential, name, project, and expiry are unchanged, so consumers never need the key redistributed. A `source_ip` condition adds or changes IP allowlisting without rotating the credential. Requires api_keys:set_policy on the key.
    """

    statements: Required[Iterable[PolicyStatement]]
    """Allow statements. Every action and resource not listed is denied."""
