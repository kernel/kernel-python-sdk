# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .credential_vault_field_definition import CredentialVaultFieldDefinition

__all__ = ["CredentialVaultItemSpec"]


class CredentialVaultItemSpec(BaseModel):
    fields: List[CredentialVaultFieldDefinition]
    """
    Ordered field definitions rendered in this order by credential collection forms.
    """

    description: Optional[str] = None
    """
    Recognizable site or service name displayed verbatim as the form title, without
    suffixes such as sign-in credentials. Display text only, not an enforced
    destination policy.
    """
