# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .credential_vault_field_input_param import CredentialVaultFieldInputParam

__all__ = ["CredentialVaultItemSpecInputParam"]


class CredentialVaultItemSpecInputParam(TypedDict, total=False):
    """Credential fields are for login and other non-payment credentials.

    Do not store, collect, or fill credit card data in credential items. Use wallet and card item types for credit cards and payment checkout instead.
    """

    fields: Required[Dict[str, CredentialVaultFieldInputParam]]

    description: str
    """
    The site's recognizable display name, used verbatim as the user-facing form
    title (for example, Hacker News). Use only the site or service name; do not
    append sign-in, login, credentials, or task instructions. This is display text,
    not an enforced destination policy. At most 16 KiB in UTF-8 bytes.
    """
