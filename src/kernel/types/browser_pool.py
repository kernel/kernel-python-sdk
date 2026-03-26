# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.browser_profile import BrowserProfile
from .shared.browser_viewport import BrowserViewport
from .shared.browser_extension import BrowserExtension

__all__ = ["BrowserPool", "BrowserPoolConfig"]


class BrowserPoolConfig(BaseModel):
    """Configuration used to create all browsers in this pool"""

    size: int
    """Number of browsers to maintain in the pool.

    The maximum size is determined by your organization's pooled sessions limit (the
    sum of all pool sizes cannot exceed your limit).
    """

    chrome_policy: Optional[Dict[str, object]] = None
    """Custom Chrome enterprise policy overrides applied to all browsers in this pool.

    Keys are Chrome enterprise policy names; values must match their expected types.
    Blocked: kernel-managed policies (extensions, proxy, CDP/automation). See
    https://chromeenterprise.google/policies/
    """

    extensions: Optional[List[BrowserExtension]] = None
    """List of browser extensions to load into the session.

    Provide each by id or name.
    """

    fill_rate_per_minute: Optional[int] = None
    """Percentage of the pool to fill per minute. Defaults to 10%."""

    headless: Optional[bool] = None
    """If true, launches the browser using a headless image. Defaults to false."""

    kiosk_mode: Optional[bool] = None
    """
    If true, launches the browser in kiosk mode to hide address bar and tabs in live
    view.
    """

    name: Optional[str] = None
    """Optional name for the browser pool. Must be unique within the organization."""

    profile: Optional[BrowserProfile] = None
    """Profile selection for the browser session.

    Provide either id or name. If specified, the matching profile will be loaded
    into the browser session. Profiles must be created beforehand.
    """

    proxy_id: Optional[str] = None
    """Optional proxy to associate to the browser session.

    Must reference a proxy belonging to the caller's org.
    """

    stealth: Optional[bool] = None
    """
    If true, launches the browser in stealth mode to reduce detection by anti-bot
    mechanisms.
    """

    timeout_seconds: Optional[int] = None
    """
    Default idle timeout in seconds for browsers acquired from this pool before they
    are destroyed. Defaults to 600 seconds if not specified
    """

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


class BrowserPool(BaseModel):
    """A browser pool containing multiple identically configured browsers."""

    id: str
    """Unique identifier for the browser pool"""

    acquired_count: int
    """Number of browsers currently acquired from the pool"""

    available_count: int
    """Number of browsers currently available in the pool"""

    browser_pool_config: BrowserPoolConfig
    """Configuration used to create all browsers in this pool"""

    created_at: datetime
    """Timestamp when the browser pool was created"""

    name: Optional[str] = None
    """Browser pool name, if set"""
