# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .workload_identity_key_source import WorkloadIdentityKeySource
from .workload_identity_preset_type import WorkloadIdentityPresetType
from .workload_identity_token_validation import WorkloadIdentityTokenValidation

__all__ = ["WorkloadIdentityIssuer"]


class WorkloadIdentityIssuer(BaseModel):
    id: str

    archived_at: Optional[datetime] = None

    created_at: datetime

    created_by_user_id: Optional[str] = None

    description: str

    enabled: bool

    issuer_url: str
    """Exact expected signed issuer.

    Optional for github_actions and google_cloud, which each have one fixed issuer.
    """

    jwks: WorkloadIdentityKeySource

    name: str

    org_id: str

    preset_type: WorkloadIdentityPresetType
    """The kind of identity provider.

    GitHub Actions, Google Cloud and Microsoft Entra issuers are recognized by their
    issuer URL and must use their own type. Defaults to the type the issuer URL
    belongs to, or custom_oidc.
    """

    security_version: int
    """Authority revision. Cosmetic updates do not widen permissions."""

    token_validation: WorkloadIdentityTokenValidation

    updated_at: datetime
