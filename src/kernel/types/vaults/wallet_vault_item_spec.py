# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "WalletVaultItemSpec",
    "LinkWalletVaultItemSpec",
    "LinkWalletVaultItemSpecAuthorization",
    "LinkWalletVaultItemSpecAuthorizationClient",
    "LinkWalletVaultItemSpecAuthorizationClientKernelManagedOAuthClient",
    "LinkWalletVaultItemSpecAuthorizationClientCustomerManagedOAuthClient",
    "LinkWalletVaultItemSpecAuthorizationClientCustomerManagedOAuthClientProviderConfig",
    "AgentCardWalletVaultItemSpec",
    "AgentCardWalletVaultItemSpecProviderConfig",
]


class LinkWalletVaultItemSpecAuthorizationClientKernelManagedOAuthClient(BaseModel):
    type: Literal["kernel_managed"]


class LinkWalletVaultItemSpecAuthorizationClientCustomerManagedOAuthClientProviderConfig(BaseModel):
    """Select a provider config by ID or name.

    Responses return the ID. Renaming a config does not change existing wallet bindings; a wallet cannot switch to a different config after creation.
    """

    id: Optional[str] = None

    name: Optional[str] = None


class LinkWalletVaultItemSpecAuthorizationClientCustomerManagedOAuthClient(BaseModel):
    provider_config: LinkWalletVaultItemSpecAuthorizationClientCustomerManagedOAuthClientProviderConfig
    """Select a provider config by ID or name.

    Responses return the ID. Renaming a config does not change existing wallet
    bindings; a wallet cannot switch to a different config after creation.
    """

    type: Literal["customer_managed"]


LinkWalletVaultItemSpecAuthorizationClient: TypeAlias = Annotated[
    Union[
        LinkWalletVaultItemSpecAuthorizationClientKernelManagedOAuthClient,
        LinkWalletVaultItemSpecAuthorizationClientCustomerManagedOAuthClient,
    ],
    PropertyInfo(discriminator="type"),
]


class LinkWalletVaultItemSpecAuthorization(BaseModel):
    client: LinkWalletVaultItemSpecAuthorizationClient

    method: Literal["oauth"]


class LinkWalletVaultItemSpec(BaseModel):
    authorization: LinkWalletVaultItemSpecAuthorization

    provider: Literal["link"]


class AgentCardWalletVaultItemSpecProviderConfig(BaseModel):
    """Select an AgentCard configuration.

    The wallet's configuration cannot be changed after creation.
    """

    id: Optional[str] = None

    name: Optional[str] = None


class AgentCardWalletVaultItemSpec(BaseModel):
    """AgentCard wallet.

    Omit provider_config to use Kernel-managed credentials, or select a customer-owned configuration. Mode (sandbox vs live) is determined by the selected credential; there is no per-item test flag. Without user_id, creation returns a hosted enrollment action and Kernel polls until the user connects. user_id may only reference a user already enrolled by a wallet in this organization under the same configuration.
    """

    provider: Literal["agentcard"]

    provider_config: Optional[AgentCardWalletVaultItemSpecProviderConfig] = None
    """Select an AgentCard configuration.

    The wallet's configuration cannot be changed after creation.
    """

    user_id: Optional[str] = None


WalletVaultItemSpec: TypeAlias = Annotated[
    Union[LinkWalletVaultItemSpec, AgentCardWalletVaultItemSpec], PropertyInfo(discriminator="provider")
]
