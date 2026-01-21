# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CredentialProviderTestResult", "Vault"]


class Vault(BaseModel):
    id: str
    """Vault ID"""

    name: str
    """Vault name"""


class CredentialProviderTestResult(BaseModel):
    """Result of testing a credential provider connection"""

    success: bool
    """Whether the connection test was successful"""

    vaults: List[Vault]
    """List of vaults accessible by the service account"""

    error: Optional[str] = None
    """Error message if the test failed"""
