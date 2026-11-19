# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkloadIdentityMatch"]


class WorkloadIdentityMatch(BaseModel):
    type: Literal["github_actions", "aws", "google_cloud", "microsoft_entra", "kubernetes", "custom_oidc"]
    """Must be the issuer's preset_type."""

    claims: Optional[Dict[str, str]] = None
    """Exact string conditions keyed by RFC 6901 JSON Pointers.

    All conditions are ANDed.
    """

    environment: Optional[str] = None

    event_names: Optional[List[str]] = None

    job_workflow_ref: Optional[str] = None

    namespace: Optional[str] = None

    ref: Optional[str] = None

    repository: Optional[str] = None
    """Friendly display name. Immutable IDs define the repository identity."""

    repository_id: Optional[str] = None

    repository_owner_id: Optional[str] = None

    service_account: Optional[str] = None

    subject: Optional[str] = None

    subject_prefix: Optional[str] = None

    workflow: Optional[str] = None

    workflow_ref: Optional[str] = None
