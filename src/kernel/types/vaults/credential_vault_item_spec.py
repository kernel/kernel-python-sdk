# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .kernel_credential_vault_item_spec import KernelCredentialVaultItemSpec
from .one_password_credential_vault_item_spec import OnePasswordCredentialVaultItemSpec

__all__ = ["CredentialVaultItemSpec"]

CredentialVaultItemSpec: TypeAlias = Annotated[
    Union[KernelCredentialVaultItemSpec, OnePasswordCredentialVaultItemSpec], PropertyInfo(discriminator="provider")
]
