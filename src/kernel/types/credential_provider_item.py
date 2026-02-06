# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CredentialProviderItem"]


class CredentialProviderItem(BaseModel):
    """A credential item from an external provider (e.g., a 1Password login item)"""

    id: str
    """Unique identifier for the item within the provider"""

    path: str
    """Path to reference this item (VaultName/ItemTitle format)"""

    title: str
    """Display name of the credential item"""

    vault_id: str
    """ID of the vault containing this item"""

    vault_name: str
    """Name of the vault containing this item"""

    urls: Optional[List[str]] = None
    """URLs associated with this credential"""
