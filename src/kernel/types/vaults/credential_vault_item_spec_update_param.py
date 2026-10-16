# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import TypedDict

from ..._types import SequenceNotStr
from .credential_vault_field_update_param import CredentialVaultFieldUpdateParam
from .credential_vault_field_definition_input_param import CredentialVaultFieldDefinitionInputParam

__all__ = ["CredentialVaultItemSpecUpdateParam"]


class CredentialVaultItemSpecUpdateParam(TypedDict, total=False):
    add_fields: Iterable[CredentialVaultFieldDefinitionInputParam]
    """Field definitions to append, with the same defaults as creation.

    Set their values in `fields` in the same update. Names must be unique after
    removals; at most 32 fields may result. A required totp or passkey field needs a
    value in `fields`.
    """

    description: str
    """
    Recognizable site or service name used as the form title, without suffixes such
    as sign-in credentials. An empty string clears it. Display text only, not an
    enforced destination policy. The server also enforces a 16 KiB UTF-8 byte limit.
    """

    fields: Dict[str, CredentialVaultFieldUpdateParam]

    remove_fields: SequenceNotStr[str]
    """Names of fields to delete with their values.

    Unknown names return 400. At least one field must remain.
    """
