# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .profile import Profile
from .._models import BaseModel
from .browser_persistence import BrowserPersistence
from .shared.browser_viewport import BrowserViewport

__all__ = ["BrowserRetrieveResponse"]


class BrowserRetrieveResponse(BaseModel):
    cdp_ws_url: str
    """Websocket URL for Chrome DevTools Protocol connections to the browser session"""

    created_at: datetime
    """When the browser session was created."""

    headless: bool
    """Whether the browser session is running in headless mode."""

    session_id: str
    """Unique identifier for the browser session"""

    stealth: bool
    """Whether the browser session is running in stealth mode."""

    timeout_seconds: int
    """The number of seconds of inactivity before the browser session is terminated."""

    browser_live_view_url: Optional[str] = None
    """Remote URL for live viewing the browser session.

    Only available for non-headless browsers.
    """

    deleted_at: Optional[datetime] = None
    """When the browser session was soft-deleted. Only present for deleted sessions."""

    kiosk_mode: Optional[bool] = None
    """Whether the browser session is running in kiosk mode."""

    persistence: Optional[BrowserPersistence] = None
    """DEPRECATED: Use timeout_seconds (up to 72 hours) and Profiles instead."""

    profile: Optional[Profile] = None
    """Browser profile metadata."""

    proxy_id: Optional[str] = None
    """ID of the proxy associated with this browser session, if any."""

    viewport: Optional[BrowserViewport] = None
    """Initial browser window size in pixels with optional refresh rate.

    If omitted, image defaults apply (1920x1080@25). Only specific viewport
    configurations are supported. The server will reject unsupported combinations.
    Supported resolutions are: 2560x1440@10, 1920x1080@25, 1920x1200@25,
    1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60 If refresh_rate is not
    provided, it will be automatically determined from the width and height if they
    match a supported configuration exactly. Note: Higher resolutions may affect the
    responsiveness of live view browser
    """
