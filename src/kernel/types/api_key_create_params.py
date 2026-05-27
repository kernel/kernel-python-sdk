# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """API key name (1-255 characters)"""

    days_to_expire: Optional[int]
    """Number of days until expiry, up to 3650. Use null for never."""

    project_id: Optional[str]
    """Unique project identifier"""
