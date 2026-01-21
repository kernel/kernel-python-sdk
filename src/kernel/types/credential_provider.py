# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CredentialProvider"]


class CredentialProvider(BaseModel):
    """
    An external credential provider (e.g., 1Password) for automatic credential lookup
    """

    id: str
    """Unique identifier for the credential provider"""

    created_at: datetime
    """When the credential provider was created"""

    enabled: bool
    """Whether the provider is enabled for credential lookups"""

    priority: int
    """Priority order for credential lookups (lower numbers are checked first)"""

    provider_type: Literal["onepassword"]
    """Type of credential provider"""

    updated_at: datetime
    """When the credential provider was last updated"""
