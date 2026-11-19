# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .workload_identity_match import WorkloadIdentityMatch
from .workload_identity_target import WorkloadIdentityTarget
from .workload_identity_authorization import WorkloadIdentityAuthorization

__all__ = ["WorkloadIdentityFederationRule"]


class WorkloadIdentityFederationRule(BaseModel):
    id: str

    archived_at: Optional[datetime] = None

    authorization: WorkloadIdentityAuthorization

    created_at: datetime

    created_by_user_id: Optional[str] = None

    description: str

    enabled: bool

    expected_audience: str

    issuer_id: str

    last_exchange_at: Optional[datetime] = None

    match: WorkloadIdentityMatch

    name: str

    org_id: str

    security_version: int
    """Authority revision. Cosmetic updates do not widen permissions."""

    target: WorkloadIdentityTarget

    updated_at: datetime
