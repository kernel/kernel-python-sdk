# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WorkloadIdentityMatchParam"]


class WorkloadIdentityMatchParam(TypedDict, total=False):
    type: Required[Literal["github_actions", "aws", "google_cloud", "microsoft_entra", "kubernetes", "custom_oidc"]]
    """Must be the issuer's preset_type."""

    claims: Dict[str, str]
    """Exact string conditions keyed by RFC 6901 JSON Pointers.

    All conditions are ANDed.
    """

    environment: str

    event_names: SequenceNotStr[str]

    job_workflow_ref: str

    namespace: str

    ref: str

    repository: str
    """Friendly display name. Immutable IDs define the repository identity."""

    repository_id: str

    repository_owner_id: str

    service_account: str

    subject: str

    subject_prefix: str

    workflow: str

    workflow_ref: str
