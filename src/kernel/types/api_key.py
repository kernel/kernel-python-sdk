# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["APIKey", "CreatedBy"]


class CreatedBy(BaseModel):
    id: str
    """Kernel user ID of the creator."""

    email: str
    """Email address of the creator."""

    name: Optional[str] = None
    """Display name of the creator, if available."""


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
    """API key name"""

    project_id: Optional[str] = None
    """Project identifier for project-scoped API keys. Null means org-wide."""

    project_name: Optional[str] = None
    """Project name for project-scoped API keys.

    Null means the key is org-wide or the project name is unavailable.
    """
