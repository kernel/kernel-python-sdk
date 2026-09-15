# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .credential_vault_field_update_param import CredentialVaultFieldUpdateParam

__all__ = ["CredentialVaultItemSpecUpdateParam"]


class CredentialVaultItemSpecUpdateParam(TypedDict, total=False):
    description: str
    """
    Recognizable site or service name used as the form title, without suffixes such
    as sign-in credentials. An empty string clears it. Display text only, not an
    enforced destination policy. The server also enforces a 16 KiB UTF-8 byte limit.
    """

    fields: Dict[str, CredentialVaultFieldUpdateParam]
