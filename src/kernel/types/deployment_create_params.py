# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = [
    "DeploymentCreateParams",
    "RuntimePolicy",
    "RuntimePolicyStatement",
    "RuntimePolicyStatementCondition",
    "Source",
    "SourceAuth",
]


class DeploymentCreateParams(TypedDict, total=False):
    entrypoint_rel_path: str
    """Relative path to the entrypoint of the application"""

    env_vars: Dict[str, str]
    """Map of environment variables to set for the deployed application.

    Each key-value pair represents an environment variable.
    """

    file: FileTypes
    """ZIP file containing the application source directory"""

    force: bool
    """Allow overwriting an existing app version"""

    region: Literal["aws.us-east-1a"]
    """Region for deployment. Currently we only support "aws.us-east-1a" """

    runtime_policy: RuntimePolicy
    """Permissions for each invocation's injected API key.

    Send this multipart field as JSON. Requires scoped deployment enablement. The
    policy must stay within the deployment's project, be a subset of the caller's
    permissions when the caller has a policy, and grant container-wide
    invocations:write for runtime callbacks. It cannot include
    api_keys:issue_beyond_expiry. Exact resource IDs must exist. The policy outlives
    the deploying credential; each invocation gets a fresh key valid for 65 minutes
    from issuance. When the caller has a policy, omission grants only project-wide
    invocations:write for runtime callbacks. A supplied policy must explicitly
    include that permission; it is never added automatically. Callers without a
    policy keep an unrestricted runtime key when this field is omitted. Scoped
    invokers must cover the runtime policy.
    """

    source: Source
    """Source from which to fetch application code."""

    version: str
    """Version of the application. Can be any string."""


class RuntimePolicyStatementCondition(TypedDict, total=False):
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


class RuntimePolicyStatement(TypedDict, total=False):
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

    condition: RuntimePolicyStatementCondition
    """
    A condition narrows a policy statement to requests matching its constraint: the
    request attribute, a comparison operator, and that operator's values.
    """


class RuntimePolicy(TypedDict, total=False):
    """Permissions for each invocation's injected API key.

    Send this multipart field as JSON. Requires scoped deployment enablement. The policy must stay within the deployment's project, be a subset of the caller's permissions when the caller has a policy, and grant container-wide invocations:write for runtime callbacks. It cannot include api_keys:issue_beyond_expiry. Exact resource IDs must exist. The policy outlives the deploying credential; each invocation gets a fresh key valid for 65 minutes from issuance. When the caller has a policy, omission grants only project-wide invocations:write for runtime callbacks. A supplied policy must explicitly include that permission; it is never added automatically. Callers without a policy keep an unrestricted runtime key when this field is omitted. Scoped invokers must cover the runtime policy.
    """

    statements: Required[Iterable[RuntimePolicyStatement]]
    """Allow statements. Every action and resource not listed is denied."""


class SourceAuth(TypedDict, total=False):
    """Authentication for private repositories."""

    token: Required[str]
    """GitHub PAT or installation access token"""

    method: Required[Literal["github_token"]]
    """Auth method"""


class Source(TypedDict, total=False):
    """Source from which to fetch application code."""

    entrypoint: Required[str]
    """Relative path to the application entrypoint within the selected path."""

    ref: Required[str]
    """Git ref (branch, tag, or commit SHA) to fetch."""

    type: Required[Literal["github"]]
    """Source type identifier."""

    url: Required[str]
    """Base repository URL (without blob/tree suffixes)."""

    auth: SourceAuth
    """Authentication for private repositories."""

    path: str
    """Path within the repo to deploy (omit to use repo root)."""
