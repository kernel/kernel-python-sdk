# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import TypedDict

from .shared_params.browser_viewport import BrowserViewport
from .shared_params.browser_extension import BrowserExtension
from .browsers.browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = ["BrowserPoolUpdateParams", "Profile", "Telemetry"]


class BrowserPoolUpdateParams(TypedDict, total=False):
    chrome_policy: Dict[str, object]
    """
    If provided, replaces the custom Chrome enterprise policy overrides applied to
    all browsers in this pool. Empty object clears any previously-set policy. Keys
    are Chrome enterprise policy names; values must match their expected types.
    Blocked: kernel-managed policies (extensions, proxy, CDP/automation). See
    https://chromeenterprise.google/policies/ The serialized JSON payload is capped
    at 5 MiB.
    """

    discard_all_idle: bool
    """
    Whether to discard all idle browsers and rebuild them immediately with the new
    configuration. Defaults to false. Only browsers that are idle when the update
    runs are rebuilt. A browser that is in use during the update keeps its original
    configuration, and if it is later released with `reuse: true` it returns to the
    pool with that stale configuration until it is discarded (by this flag on a
    later update, or by flushing the pool).
    """

    extensions: Iterable[BrowserExtension]
    """If provided, replaces the extension list.

    Empty array clears all previously-selected extensions. Omit this field to leave
    extensions unchanged.
    """

    fill_rate_per_minute: int
    """If provided, replaces the percentage of the pool to fill per minute.

    The cap is 25 for most organizations but can be raised per-organization, so only
    the lower bound is enforced here.
    """

    headless: bool
    """If provided, replaces whether browsers launch using a headless image."""

    kiosk_mode: bool
    """If provided, replaces whether browsers launch in kiosk mode."""

    name: str
    """If provided, replaces the pool name.

    Empty string is a no-op; the pool name cannot be cleared or reset to empty once
    assigned.
    """

    profile: Profile
    """Profile configuration for browsers in a pool.

    Provide either id or name. Profiles must be created beforehand. Unlike single
    browser sessions, pools load the profile read-only and never persist changes
    back to it, so save_changes is omitted here. Any save_changes value sent on a
    pool profile is silently ignored rather than rejected.
    """

    proxy_id: str
    """Empty string clears the previously-selected proxy.

    Omit this field to leave the proxy unchanged.
    """

    refresh_on_profile_update: bool
    """
    If provided, replaces whether idle browsers are flushed when the profile the
    pool uses is updated. When the pool's profile reference is changed (including
    newly attached) and this field is omitted, it defaults to true. Re-sending the
    same profile reference leaves this setting unchanged. Clearing the profile also
    disables this setting. Requires a profile to be set on the pool.
    """

    size: int
    """If provided, replaces the number of browsers to maintain in the pool.

    The maximum size is determined by your organization's pooled sessions limit (the
    sum of all pool sizes cannot exceed your limit).
    """

    start_url: str
    """
    If provided, replaces the URL to navigate to when a new browser is warmed into
    the pool. Empty string clears the previously-set URL. Omit this field to leave
    it unchanged.
    """

    stealth: bool
    """If provided, replaces whether browsers launch in stealth mode."""

    telemetry: Optional[Telemetry]
    """If provided, updates the pool's telemetry configuration.

    Omit, set to null, or set to an empty object ({}) to leave the existing
    configuration unchanged. Set enabled to true to enable capture using the default
    set. Set enabled to false to clear the pool's telemetry. Provide browser
    category settings for per-category updates, merged onto the pool's current
    configuration. Only applied to browsers warmed after the update; browsers
    already in the pool keep their configuration until discarded.
    """

    timeout_seconds: int
    """
    If provided, replaces the default idle timeout in seconds for browsers acquired
    from this pool before they are destroyed. Minimum 10, maximum 259200 (72 hours).
    """

    viewport: BrowserViewport
    """
    Initial browser window size in pixels with optional refresh rate. If omitted,
    image defaults apply (1920x1080@25). For GPU images, the default is
    1920x1080@60. Arbitrary viewport dimensions and refresh rates are accepted.
    Known-good presets include: 2560x1440@10, 1920x1080@25, 1920x1200@25,
    1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60, 768x1024@60, 390x844@60. For
    GPU images, recommended presets use one of these resolutions with refresh rates
    60, 30, 25, or 10: 800x600, 960x720, 1024x576, 1024x768, 1152x648, 1200x800,
    1280x720, 1368x768, 1440x900, 1600x900, 1920x1080, 1920x1200, 390x844, 360x250,
    768x1024, 800x1600. Viewports outside this list may exhibit unstable live view
    or recording behavior. If refresh_rate is not provided, it will be automatically
    determined based on the resolution (higher resolutions use lower refresh rates
    to keep bandwidth reasonable).
    """


class Profile(TypedDict, total=False):
    """Profile configuration for browsers in a pool.

    Provide either id or name. Profiles must
    be created beforehand. Unlike single browser sessions, pools load the profile read-only
    and never persist changes back to it, so save_changes is omitted here. Any save_changes
    value sent on a pool profile is silently ignored rather than rejected.
    """

    id: str
    """Profile ID to load for browsers in this pool"""

    name: str
    """Profile name to load for browsers in this pool (instead of id).

    Must be 1-255 characters, using letters, numbers, dots, underscores, or hyphens.
    """


class Telemetry(TypedDict, total=False):
    """If provided, updates the pool's telemetry configuration.

    Omit, set to null, or set to an empty object ({}) to leave the existing configuration unchanged. Set enabled to true to enable capture using the default set. Set enabled to false to clear the pool's telemetry. Provide browser category settings for per-category updates, merged onto the pool's current configuration. Only applied to browsers warmed after the update; browsers already in the pool keep their configuration until discarded.
    """

    browser: BrowserTelemetryCategoriesConfigParam
    """Per-category capture flags.

    The operational categories (control, connection, system, captcha) are captured
    whenever telemetry is enabled; set one to enabled=false to opt out. The CDP
    categories (console, network, page, interaction) and screenshot are off by
    default; set enabled=true to opt in. On create, provided categories layer onto
    the default set. On update, provided categories merge onto the session's current
    config; when no telemetry is active this falls back to the default set (matching
    create). If browser is omitted or empty, the default set is used. A browser
    config that disables every category stops capture on update and starts no
    capture on create.
    """

    enabled: bool
    """Request shortcut for browser telemetry capture.

    True enables capture; with no browser category settings it captures the default
    set (control, connection, system, captcha), and any browser category settings
    are layered onto that default set. On update, enabled=true resolves the config
    fresh from the default set plus any provided categories, replacing the session's
    current selection rather than merging onto it; omit enabled to merge categories
    onto the current selection instead. False stops capture on update and starts no
    capture on create. enabled=false cannot be combined with browser category
    settings.
    """
