# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .api_key_principal import APIKeyPrincipal

__all__ = ["APIKey", "CreatedBy", "Policy", "PolicyStatement", "PolicyStatementCondition"]


class CreatedBy(BaseModel):
    """Human audit creator, or null after creator deletion.

    Not the service credential's principal.
    """

    id: str
    """Kernel user ID of the creator."""

    email: str
    """Email address of the creator."""

    name: Optional[str] = None
    """Display name of the creator, if available."""


class PolicyStatementCondition(BaseModel):
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


class PolicyStatement(BaseModel):
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

    condition: Optional[PolicyStatementCondition] = None
    """
    A condition narrows a policy statement to requests matching its constraint: the
    request attribute, a comparison operator, and that operator's values.
    """


class Policy(BaseModel):
    """Permissions granted to a scoped API key.

    Absent for an ordinary key, which keeps unrestricted access within its organization or project.
    """

    statements: List[PolicyStatement]
    """Allow statements. Every action and resource not listed is denied."""


class APIKey(BaseModel):
    id: str
    """Unique API key identifier"""

    created_at: datetime
    """When the API key was created"""

    created_by: Optional[CreatedBy] = None
    """Human audit creator, or null after creator deletion.

    Not the service credential's principal.
    """

    deleted_at: Optional[datetime] = None
    """When the API key was deleted (soft-deleted).

    Null for keys that have not been deleted.
    """

    expires_at: Optional[datetime] = None
    """When the API key expires"""

    last_used_at: Optional[datetime] = None
    """
    When the API key last authenticated a request, accurate to within about 20
    minutes. Null if the key has not been used since last-use tracking began.
    """

    masked_key: str
    """Masked version of the API key"""

    name: str
    """Label for the API key.

    API keys are not addressable by name; use the ID or key identifier for stable
    references.
    """

    project_id: Optional[str] = None
    """Project identifier for project-scoped API keys. Null means org-wide."""

    project_name: Optional[str] = None
    """Project name for project-scoped API keys.

    Null means the key is org-wide or the project name is unavailable.
    """

    policy: Optional[Policy] = None
    """Permissions granted to a scoped API key.

    Absent for an ordinary key, which keeps unrestricted access within its
    organization or project.
    """

    principal: Optional[APIKeyPrincipal] = None

    service_account_id: Optional[str] = None
    """Organization-owned service principal, when linked."""
