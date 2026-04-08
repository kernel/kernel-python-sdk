# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .profile import Profile
from .._models import BaseModel
from .browser_usage import BrowserUsage
from .browser_pool_ref import BrowserPoolRef
from .browser_persistence import BrowserPersistence
from .shared.browser_viewport import BrowserViewport

__all__ = ["BrowserListResponse"]


class BrowserListResponse(BaseModel):
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

    webdriver_ws_url: str
    """Websocket URL for WebDriver BiDi connections to the browser session"""

    base_url: Optional[str] = None
    """Metro-API HTTP base URL for this browser session."""

    browser_live_view_url: Optional[str] = None
    """Remote URL for live viewing the browser session.

    Only available for non-headless browsers.
    """

    deleted_at: Optional[datetime] = None
    """When the browser session was soft-deleted. Only present for deleted sessions."""

    gpu: Optional[bool] = None
    """
    Whether GPU acceleration is enabled for the browser session (only supported for
    headful sessions).
    """

    kiosk_mode: Optional[bool] = None
    """Whether the browser session is running in kiosk mode."""

    persistence: Optional[BrowserPersistence] = None
    """DEPRECATED: Use timeout_seconds (up to 72 hours) and Profiles instead."""

    pool: Optional[BrowserPoolRef] = None
    """Browser pool this session was acquired from, if any."""

    profile: Optional[Profile] = None
    """Browser profile metadata."""

    proxy_id: Optional[str] = None
    """ID of the proxy associated with this browser session, if any."""

    usage: Optional[BrowserUsage] = None
    """Session usage metrics."""

    viewport: Optional[BrowserViewport] = None
    """
    Initial browser window size in pixels with optional refresh rate. If omitted,
    image defaults apply (1920x1080@25). For GPU images, the default is
    1920x1080@60. Arbitrary viewport dimensions and refresh rates are accepted.
    Known-good presets include: 2560x1440@10, 1920x1080@25, 1920x1200@25,
    1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60. For GPU images, recommended
    presets use one of these resolutions with refresh rates 60, 30, 25, or 10:
    800x600, 960x720, 1024x576, 1024x768, 1152x648, 1200x800, 1280x720, 1368x768,
    1440x900, 1600x900, 1920x1080, 1920x1200, 390x844, 360x250, 768x1024, 800x1600.
    Viewports outside this list may exhibit unstable live view or recording
    behavior. If refresh_rate is not provided, it will be automatically determined
    based on the resolution (higher resolutions use lower refresh rates to keep
    bandwidth reasonable).
    """
