# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["APIKey", "CreatedBy", "Policy", "PolicyStatement"]


class CreatedBy(BaseModel):
    id: str
    """Kernel user ID of the creator."""

    email: str
    """Email address of the creator."""

    name: Optional[str] = None
    """Display name of the creator, if available."""


class PolicyStatement(BaseModel):
    action: str
    """Permitted action, such as browsers:use or vaults:read."""

    resource: str
    """Resource the action applies to, in the format projects/{project_id}/{kind}/{id}.

    Wildcards are supported.
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

    created_by: CreatedBy

    deleted_at: Optional[datetime] = None
    """When the API key was deleted (soft-deleted).

    Null for keys that have not been deleted.
    """

    expires_at: Optional[datetime] = None
    """When the API key expires"""

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
