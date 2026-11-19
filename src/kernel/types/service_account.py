# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ServiceAccount"]


class ServiceAccount(BaseModel):
    id: str

    archived_at: Optional[datetime] = None

    created_at: datetime

    created_by_user_id: Optional[str] = None

    description: str

    last_used_at: Optional[datetime] = None
    """
    When one of the account's API keys last authenticated or one of its rules last
    issued a token. Recorded at most once every 15 minutes, so it can lag. Null if
    the account has never been used.
    """

    name: str

    org_id: str

    security_version: int
    """Authority revision. Cosmetic updates do not widen permissions."""

    updated_at: datetime
