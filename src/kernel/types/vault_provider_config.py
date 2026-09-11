# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["VaultProviderConfig", "VaultLinkProviderConfig", "VaultAgentCardProviderConfig"]


class VaultLinkProviderConfig(BaseModel):
    """Response schema for a Link configuration, without secret credentials.

    Kernel generates the ID and timestamps. Configuration creation uses VaultLinkProviderConfigRequest.
    """

    id: str

    client_id: str
    """OAuth client identity; immutable. Secret credentials are never returned."""

    created_at: datetime

    name: str
    """Unique within the organization."""

    provider: Literal["link"]

    updated_at: datetime


class VaultAgentCardProviderConfig(BaseModel):
    """Response schema for an AgentCard configuration, without secret credentials.

    Kernel generates the ID and timestamps and introspects test_mode from the credentials. Configuration creation uses VaultAgentCardProviderConfigRequest.
    """

    id: str

    client_id: str

    created_at: datetime

    name: str

    provider: Literal["agentcard"]

    test_mode: bool
    """Introspected mode of the selected credential; true means sandbox objects."""

    updated_at: datetime


VaultProviderConfig: TypeAlias = Annotated[
    Union[VaultLinkProviderConfig, VaultAgentCardProviderConfig], PropertyInfo(discriminator="provider")
]
