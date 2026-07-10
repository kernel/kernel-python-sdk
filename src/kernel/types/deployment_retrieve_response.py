# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeploymentRetrieveResponse"]


class DeploymentRetrieveResponse(BaseModel):
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

    source_checksum: Optional[str] = None
    """Hex-encoded SHA-256 checksum of the source archive.

    For file uploads, this hashes the uploaded archive; for GitHub-sourced
    deployments, this hashes the GitHub archive downloaded by the API. Omitted for
    deployments created before this field was recorded.
    """

    source_path: Optional[str] = None
    """
    For GitHub-sourced deployments, the subpath within the repository that was used
    as the deploy root. Omitted when the repo root was used or for file uploads.
    """

    source_ref: Optional[str] = None
    """
    For GitHub-sourced deployments, the git ref as requested at deploy time (branch,
    tag, or commit SHA — not resolved to a commit). Omitted for file uploads.
    """

    source_type: Optional[Literal["file", "github"]] = None
    """Origin of the deployed source code.

    This is read-only response provenance; `file` indicates an uploaded archive and
    `github` indicates a repository fetched by the API.
    """

    source_url: Optional[str] = None
    """For GitHub-sourced deployments, the repository URL that was fetched.

    Omitted for file uploads.
    """

    status_reason: Optional[str] = None
    """Status reason"""

    updated_at: Optional[datetime] = None
    """Timestamp when the deployment was last updated"""
