# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VaultProviderConfigUpdateParams", "Credentials"]


class VaultProviderConfigUpdateParams(TypedDict, total=False):
    credentials: Credentials
    """Fields to update.

    Omitted credentials are left unchanged. A rejected update leaves existing
    credentials unchanged.
    """

    name: str
    """Unique within the organization."""


class Credentials(TypedDict, total=False):
    """Fields to update.

    Omitted credentials are left unchanged. A rejected update leaves existing credentials unchanged.
    """

    client_secret: str
