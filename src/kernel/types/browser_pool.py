# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.browser_viewport import BrowserViewport
from .shared.browser_extension import BrowserExtension

__all__ = ["BrowserPool", "BrowserPoolConfig", "BrowserPoolConfigProfile"]


class BrowserPoolConfigProfile(BaseModel):
    """Profile selection for browsers in a pool.

    Provide either id or name. The matching profile is
    loaded into every browser in the pool. Profiles must be created beforehand. Unlike single
    browser sessions, pools load the profile read-only and never persist changes back to it, so
    save_changes is omitted here. Any save_changes value sent on a pool profile is silently
    ignored rather than rejected, so callers reusing a single-session profile object will not error.
    """

    id: Optional[str] = None
    """Profile ID to load for browsers in this pool"""

    name: Optional[str] = None
    """Profile name to load for browsers in this pool (instead of id).

    Must be 1-255 characters, using letters, numbers, dots, underscores, or hyphens.
    """


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
    """Percentage of the pool to fill per minute.

    Defaults to 10. The cap is 25 for most organizations but can be raised
    per-organization, so only the lower bound is enforced here.
    """

    headless: Optional[bool] = None
    """If true, launches the browser using a headless image. Defaults to false."""

    kiosk_mode: Optional[bool] = None
    """
    If true, launches the browser in kiosk mode to hide address bar and tabs in live
    view.
    """

    name: Optional[str] = None
    """Optional name for the browser pool. Must be unique within the project."""

    profile: Optional[BrowserPoolConfigProfile] = None
    """Profile selection for browsers in a pool.

    Provide either id or name. The matching profile is loaded into every browser in
    the pool. Profiles must be created beforehand. Unlike single browser sessions,
    pools load the profile read-only and never persist changes back to it, so
    save_changes is omitted here. Any save_changes value sent on a pool profile is
    silently ignored rather than rejected, so callers reusing a single-session
    profile object will not error.
    """

    proxy_id: Optional[str] = None
    """Optional proxy to associate to the browser session.

    Must reference a proxy in the same project as the browser session.
    """

    start_url: Optional[str] = None
    """Optional URL to navigate to when a new browser is warmed into the pool.

    Best-effort: failures to navigate do not fail pool fill. Only applied to
    newly-warmed browsers; browsers reused via release/acquire keep whatever URL the
    previous lease left them on. Accepts any URL Chromium can resolve, including
    chrome:// pages.
    """

    stealth: Optional[bool] = None
    """
    If true, launches the browser in stealth mode to reduce detection by anti-bot
    mechanisms.
    """

    timeout_seconds: Optional[int] = None
    """
    Default idle timeout in seconds for browsers acquired from this pool before they
    are destroyed. Defaults to 600 seconds. Minimum 10, maximum 259200 (72 hours).
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
