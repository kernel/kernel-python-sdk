# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkloadIdentityAuthenticationEvent"]


class WorkloadIdentityAuthenticationEvent(BaseModel):
    id: str

    correlation_id: str

    created_at: datetime

    credential_id: Optional[str] = None

    federation_rule_id: Optional[str] = None

    issuer_id: Optional[str] = None

    org_id: str

    outcome: Literal["success", "failure"]

    project_id: Optional[str] = None

    reason: str

    service_account_id: Optional[str] = None
