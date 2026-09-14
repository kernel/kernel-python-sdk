# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from ..._models import BaseModel
from .credential_vault_field_state import CredentialVaultFieldState

__all__ = ["CredentialVaultItemState"]


class CredentialVaultItemState(BaseModel):
    fields: Dict[str, CredentialVaultFieldState]
    """Exactly one entry for each declared field."""

    status: Literal["pending_collection", "ready"]
    """Ready means all required fields have values, not that a login succeeded.

    Optional fields may remain unset.
    """
