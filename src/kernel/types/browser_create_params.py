# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import TypedDict

from .shared_params.browser_profile import BrowserProfile
from .shared_params.browser_viewport import BrowserViewport
from .shared_params.browser_extension import BrowserExtension
from .browsers.browser_telemetry_request_config_param import BrowserTelemetryRequestConfigParam

__all__ = ["BrowserCreateParams"]


class BrowserCreateParams(TypedDict, total=False):
    chrome_policy: Dict[str, object]
    """Custom Chrome enterprise policy overrides applied to this browser session.

    Keys are Chrome enterprise policy names; values must match their expected types.
    Blocked: kernel-managed policies (extensions, proxy, CDP/automation). See
    https://chromeenterprise.google/policies/
    """

    extensions: Iterable[BrowserExtension]
    """List of browser extensions to load into the session.

    Provide each by id or name.
    """

    gpu: bool
    """If true, enables GPU acceleration for the browser session.

    Requires Start-Up or Enterprise plan and headless=false.
    """

    headless: bool
    """If true, launches the browser using a headless image (no VNC/GUI).

    Defaults to false.
    """

    invocation_id: str
    """action invocation ID"""

    kiosk_mode: bool
    """
    If true, launches the browser in kiosk mode to hide address bar and tabs in live
    view.
    """

    profile: BrowserProfile
    """Profile selection for the browser session.

    Provide either id or name. If specified, the matching profile will be loaded
    into the browser session. Profiles must be created beforehand.
    """

    proxy_id: str
    """Optional proxy to associate to the browser session.

    Must reference a proxy belonging to the caller's org.
    """

    start_url: str
    """Optional URL to open when the browser session is created.

    Navigation is best-effort, so navigation failures do not prevent the session
    from being created.
    """

    stealth: bool
    """
    If true, launches the browser in stealth mode to reduce detection by anti-bot
    mechanisms.
    """

    telemetry: Optional[BrowserTelemetryRequestConfigParam]
    """Telemetry configuration for the browser session.

    Set enabled to true to start capture using VM defaults, or provide browser
    category settings. If omitted, null, set to an empty object ({}), set to
    enabled: false without browser category settings, or all four categories are
    explicitly disabled, capture is not started.
    """

    timeout_seconds: int
    """The number of seconds of inactivity before the browser session is terminated.

    Activity includes CDP connections and live view connections. Defaults to 60
    seconds. Minimum allowed is 10 seconds. Maximum allowed is 259200 (72 hours). We
    check for inactivity every 5 seconds, so the actual timeout behavior you will
    see is +/- 5 seconds around the specified value.
    """

    viewport: BrowserViewport
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
