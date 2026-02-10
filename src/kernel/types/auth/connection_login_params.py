# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectionLoginParams", "Proxy"]


class ConnectionLoginParams(TypedDict, total=False):
    proxy: Proxy
    """Proxy selection.

    Provide either id or name. The proxy must belong to the caller's org.
    """

    save_credential_as: str
    """If provided, saves credentials under this name upon successful login"""


class Proxy(TypedDict, total=False):
    """Proxy selection.

    Provide either id or name. The proxy must belong to the caller's org.
    """

    id: str
    """Proxy ID"""

    name: str
    """Proxy name"""
