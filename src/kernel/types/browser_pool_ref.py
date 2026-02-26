# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BrowserPoolRef"]


class BrowserPoolRef(BaseModel):
    """Browser pool this session was acquired from, if any."""

    id: str
    """Browser pool ID"""

    name: Optional[str] = None
    """Browser pool name, if set"""
