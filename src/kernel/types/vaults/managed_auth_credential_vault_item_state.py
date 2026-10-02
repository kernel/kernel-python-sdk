# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .managed_auth_credential_vault_field import ManagedAuthCredentialVaultField

__all__ = ["ManagedAuthCredentialVaultItemState"]


class ManagedAuthCredentialVaultItemState(BaseModel):
    provider: Literal["managed_auth"]

    status: Literal["ready", "unavailable"]
    """
    Items are created ready, which means the connection has a saved Kernel
    credential that stores values or a TOTP seed (what has_values or has_totp_secret
    report on credentials), not that a login succeeded. Unavailable means it no
    longer does; such items advertise no operations.
    """

    fields: Optional[Dict[str, ManagedAuthCredentialVaultField]] = None
    """
    One entry per non-empty value on the connection's saved credential, keyed by the
    field name to use in fill bindings. Included on single-item responses (create
    and get) and omitted from list responses, like `value_keys` on credentials.
    Empty when unavailable or when every stored value is empty. A stored value named
    totp_secret is never listed or filled. Values are never returned. A totp entry
    is present when the credential has a TOTP seed; fill writes a generated code for
    it. Entries follow the connection's credential.
    """

    status_reason: Optional[Literal["connection_not_found", "no_credential", "external_credential"]] = None
    """Present when status is unavailable.

    connection_not_found means the connection was deleted. no_credential means the
    connection's credential was deleted or emptied after the item was created.
    external_credential means the connection was moved to an external credential
    provider.
    """
