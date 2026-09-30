# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VaultProviderConfigCreateParams",
    "VaultLinkProviderConfigRequest",
    "VaultLinkProviderConfigRequestCredentials",
    "VaultAgentCardProviderConfigRequest",
    "VaultAgentCardProviderConfigRequestCredentials",
]


class VaultLinkProviderConfigRequest(TypedDict, total=False):
    credentials: Required[VaultLinkProviderConfigRequestCredentials]

    name: Required[str]
    """Unique within the organization."""

    provider: Required[Literal["link"]]


class VaultLinkProviderConfigRequestCredentials(TypedDict, total=False):
    client_id: Required[str]

    client_secret: Required[str]

    publishable_key: str
    """Stripe publishable key for the account that owns the Link OAuth client.

    Link requires it as the bearer credential when Kernel refreshes or revokes
    imported wallet grants; without it, those wallets stop working when the imported
    access token expires.
    """


class VaultAgentCardProviderConfigRequest(TypedDict, total=False):
    credentials: Required[VaultAgentCardProviderConfigRequestCredentials]

    name: Required[str]
    """Unique within the organization."""

    provider: Required[Literal["agentcard"]]


class VaultAgentCardProviderConfigRequestCredentials(TypedDict, total=False):
    client_id: Required[str]

    client_secret: Required[str]


VaultProviderConfigCreateParams: TypeAlias = Union[VaultLinkProviderConfigRequest, VaultAgentCardProviderConfigRequest]
