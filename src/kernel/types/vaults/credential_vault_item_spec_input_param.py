# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .kernel_credential_vault_item_spec_input_param import KernelCredentialVaultItemSpecInputParam
from .managed_auth_credential_vault_item_spec_input_param import ManagedAuthCredentialVaultItemSpecInputParam
from .one_password_credential_vault_item_spec_input_param import OnePasswordCredentialVaultItemSpecInputParam

__all__ = ["CredentialVaultItemSpecInputParam"]

CredentialVaultItemSpecInputParam: TypeAlias = Union[
    KernelCredentialVaultItemSpecInputParam,
    OnePasswordCredentialVaultItemSpecInputParam,
    ManagedAuthCredentialVaultItemSpecInputParam,
]
