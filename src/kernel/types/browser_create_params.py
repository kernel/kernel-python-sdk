# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .browser_persistence_param import BrowserPersistenceParam
from .shared_params.browser_profile import BrowserProfile
from .shared_params.browser_viewport import BrowserViewport
from .shared_params.browser_extension import BrowserExtension

__all__ = ["BrowserCreateParams"]


class BrowserCreateParams(TypedDict, total=False):
    extensions: Iterable[BrowserExtension]
    """List of browser extensions to load into the session.

    Provide each by id or name.
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

    persistence: BrowserPersistenceParam
    """DEPRECATED: Use timeout_seconds (up to 72 hours) and Profiles instead."""

    profile: BrowserProfile
    """Profile selection for the browser session.

    Provide either id or name. If specified, the matching profile will be loaded
    into the browser session. Profiles must be created beforehand.
    """

    proxy_id: str
    """Optional proxy to associate to the browser session.

    Must reference a proxy belonging to the caller's org.
    """

    stealth: bool
    """
    If true, launches the browser in stealth mode to reduce detection by anti-bot
    mechanisms.
    """

    timeout_seconds: int
    """The number of seconds of inactivity before the browser session is terminated.

    Activity includes CDP connections and live view connections. Defaults to 60
    seconds. Minimum allowed is 10 seconds. Maximum allowed is 259200 (72 hours). We
    check for inactivity every 5 seconds, so the actual timeout behavior you will
    see is +/- 5 seconds around the specified value.
    """

    viewport: BrowserViewport
    """Initial browser window size in pixels with optional refresh rate.

    If omitted, image defaults apply (1920x1080@25). Only specific viewport
    configurations are supported. The server will reject unsupported combinations.
    Supported resolutions are: 2560x1440@10, 1920x1080@25, 1920x1200@25,
    1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60 If refresh_rate is not
    provided, it will be automatically determined from the width and height if they
    match a supported configuration exactly. Note: Higher resolutions may affect the
    responsiveness of live view browser
    """
