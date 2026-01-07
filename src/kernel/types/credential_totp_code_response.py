# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["CredentialTotpCodeResponse"]


class CredentialTotpCodeResponse(BaseModel):
    code: str
    """Current 6-digit TOTP code"""

    expires_at: datetime
    """When this code expires (ISO 8601 timestamp)"""
