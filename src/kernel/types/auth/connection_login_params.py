# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectionLoginParams", "Proxy"]


class ConnectionLoginParams(TypedDict, total=False):
    proxy: Proxy
    """Proxy selection.

    Provide either id or name. The proxy must be in the same project as the resource
    referencing it. When selecting by name, the name must match exactly one active
    proxy in the project. Ambiguous names return a 400; use id for stable
    references.
    """

    record_session: bool
    """Override the connection's default for recording this login's browser session.

    When omitted, the connection's record_session default is used.
    """


class Proxy(TypedDict, total=False):
    """Proxy selection.

    Provide either id or name. The proxy must be in the same project as the resource referencing it.
    When selecting by name, the name must match exactly one active proxy in the project. Ambiguous names return a 400; use id for stable references.
    """

    id: str
    """Proxy ID"""

    name: str
    """Proxy name"""
