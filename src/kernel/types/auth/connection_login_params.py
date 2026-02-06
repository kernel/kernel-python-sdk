# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectionLoginParams"]


class ConnectionLoginParams(TypedDict, total=False):
    save_credential_as: str
    """If provided, saves credentials under this name upon successful login"""
