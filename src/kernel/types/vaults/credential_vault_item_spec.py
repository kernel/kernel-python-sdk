# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .credential_vault_field_definition import CredentialVaultFieldDefinition

__all__ = ["CredentialVaultItemSpec"]


class CredentialVaultItemSpec(BaseModel):
    fields: Dict[str, CredentialVaultFieldDefinition]

    description: Optional[str] = None
    """
    Recognizable site or service name displayed verbatim as the form title, without
    suffixes such as sign-in credentials. Display text only, not an enforced
    destination policy.
    """
