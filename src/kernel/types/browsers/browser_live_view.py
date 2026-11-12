# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .browser_live_view_scope import BrowserLiveViewScope

__all__ = ["BrowserLiveView"]


class BrowserLiveView(BaseModel):
    scope: BrowserLiveViewScope
    """`read` shows the browser without accepting input.

    `control` also lets the viewer drive the browser through the live view.
    """

    url: str
    """Live view URL. Treat it as a credential."""

    expires_at: Optional[datetime] = None
    """When the URL expires. Absent when it stays valid until the browser is deleted."""
