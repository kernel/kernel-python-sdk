# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeploymentCreateResponse"]


class DeploymentCreateResponse(BaseModel):
    """Deployment record information."""

    id: str
    """Unique identifier for the deployment"""

    created_at: datetime
    """Timestamp when the deployment was created"""

    region: Literal["aws.us-east-1a"]
    """Deployment region code"""

    status: Literal["queued", "in_progress", "running", "failed", "stopped"]
    """Current status of the deployment"""

    entrypoint_rel_path: Optional[str] = None
    """Relative path to the application entrypoint"""

    env_vars: Optional[Dict[str, str]] = None
    """Environment variables configured for this deployment.

    Values are redacted for API key, OAuth, and managed-auth callers, which receive
    every key with an empty string value. Only dashboard sessions receive the actual
    values.
    """

    status_reason: Optional[str] = None
    """Status reason"""

    updated_at: Optional[datetime] = None
    """Timestamp when the deployment was last updated"""
