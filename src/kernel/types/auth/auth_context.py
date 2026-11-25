# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .auth_context_workload_identity import AuthContextWorkloadIdentity

__all__ = [
    "AuthContext",
    "Authentication",
    "Authorization",
    "AuthorizationCredentialScope",
    "AuthorizationEffectiveScope",
    "AuthorizationEffectivePolicy",
    "AuthorizationEffectivePolicyStatement",
    "AuthorizationEffectivePolicyStatementCondition",
    "Organization",
    "Principal",
]


class Authentication(BaseModel):
    credential_id: Optional[str] = None
    """
    The API key ID when authenticated with an API key; null for session credentials.
    """

    method: Literal["api_key", "jwt"]
    """The credential format used to authenticate the request."""

    source: Literal["api_key", "oauth", "dashboard"]
    """The source classification resolved by authentication middleware."""


class AuthorizationCredentialScope(BaseModel):
    """A scope within the authenticated organization.

    A null project_id represents organization-wide scope.
    """

    project_id: Optional[str] = None
    """The Kernel project ID, or null when the scope is organization-wide."""


class AuthorizationEffectiveScope(BaseModel):
    """A scope within the authenticated organization.

    A null project_id represents organization-wide scope.
    """

    project_id: Optional[str] = None
    """The Kernel project ID, or null when the scope is organization-wide."""


class AuthorizationEffectivePolicyStatementCondition(BaseModel):
    """
    A condition narrows a policy statement to requests matching its constraint: the request attribute, a comparison operator, and that operator's values.
    """

    key: Literal["source_ip"]
    """Request attribute the condition constrains.

    `source_ip` restricts the statement to requests whose client address falls
    inside one of `values`.
    """

    operator: Literal["in"]
    """Comparison the condition applies between the request attribute and values."""

    values: List[str]
    """Values the request attribute must match.

    For `source_ip`, CIDR networks: a bare address without a mask is rejected, and
    so are an entry with host bits set and an IPv4 network written in IPv6 notation.
    """


class AuthorizationEffectivePolicyStatement(BaseModel):
    action: str
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

    resource: str
    """Resource the action applies to, in the format projects/{project_id}/{kind}/{id}.

    Wildcards are supported.
    """

    condition: Optional[AuthorizationEffectivePolicyStatementCondition] = None
    """
    A condition narrows a policy statement to requests matching its constraint: the
    request attribute, a comparison operator, and that operator's values.
    """


class AuthorizationEffectivePolicy(BaseModel):
    """Current effective paired policy for a service-account principal.

    Omitted for legacy human/client identities.
    """

    statements: List[AuthorizationEffectivePolicyStatement]
    """Allow statements. Every action and resource not listed is denied."""


class Authorization(BaseModel):
    """The credential's maximum scope and the effective scope selected for this request.

    Future permission data can be added without changing scope semantics.
    """

    credential_scope: AuthorizationCredentialScope
    """A scope within the authenticated organization.

    A null project_id represents organization-wide scope.
    """

    effective_scope: AuthorizationEffectiveScope
    """A scope within the authenticated organization.

    A null project_id represents organization-wide scope.
    """

    effective_policy: Optional[AuthorizationEffectivePolicy] = None
    """Current effective paired policy for a service-account principal.

    Omitted for legacy human/client identities.
    """


class Organization(BaseModel):
    id: str
    """The authenticated Kernel organization ID."""


class Principal(BaseModel):
    id: str
    """The authenticated API key, user or organization-owned service-account ID."""

    type: Literal["api_key", "user", "service_account"]
    """The kind of principal authenticated for the request."""


class AuthContext(BaseModel):
    """The identity and authorization context resolved for the current request."""

    authentication: Authentication

    authorization: Authorization
    """The credential's maximum scope and the effective scope selected for this
    request.

    Future permission data can be added without changing scope semantics.
    """

    organization: Organization

    principal: Principal

    workload_identity: Optional[AuthContextWorkloadIdentity] = None
