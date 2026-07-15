# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .tags_param import TagsParam
from .browsers.browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = ["BrowserPoolAcquireParams", "Telemetry"]


class BrowserPoolAcquireParams(TypedDict, total=False):
    acquire_timeout_seconds: int
    """Maximum number of seconds to wait for a browser to be available.

    Defaults to the calculated time it would take to fill the pool at the currently
    configured fill rate.
    """

    name: str
    """
    Optional human-readable name for the acquired browser session, used to find it
    later in the dashboard. Must be unique among active sessions within the pool's
    project. Applies to this lease only and is cleared when the browser is released
    back to the pool.
    """

    start_url: str
    """Optional URL to navigate the acquired browser to.

    Overrides the pool's start_url for this acquire only. Best-effort: failures to
    navigate do not fail the acquire.
    """

    tags: TagsParam
    """
    Optional user-defined key-value tags for the acquired browser session, used to
    find and group sessions later. Applies to this lease only and are cleared when
    the browser is released back to the pool. Up to 50 pairs.
    """

    telemetry: Optional[Telemetry]
    """Telemetry override for the acquired browser, applied to this lease only.

    Merges onto the browser's current (pool-inherited) telemetry using the same
    per-category semantics as PATCH /browsers: provided categories override the
    current configuration, omitted categories are inherited. Set enabled to true to
    resolve the config fresh from the default set, or enabled to false to stop
    capture. When the browser is released back to the pool with reuse, its telemetry
    is reset to the pool's baseline, so the override does not carry over to the next
    lease.
    """


class Telemetry(TypedDict, total=False):
    """Telemetry override for the acquired browser, applied to this lease only.

    Merges onto the browser's current (pool-inherited) telemetry using the same per-category semantics as PATCH /browsers: provided categories override the current configuration, omitted categories are inherited. Set enabled to true to resolve the config fresh from the default set, or enabled to false to stop capture. When the browser is released back to the pool with reuse, its telemetry is reset to the pool's baseline, so the override does not carry over to the next lease.
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
