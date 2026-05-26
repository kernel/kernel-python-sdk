# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = ["BrowserTelemetryRequestConfigParam"]


class BrowserTelemetryRequestConfigParam(TypedDict, total=False):
    """Telemetry request configuration for a browser session."""

    browser: BrowserTelemetryCategoriesConfigParam
    """Per-category enable/disable flags.

    If enabled is true and browser is omitted or empty, the VM default category set
    is used. Explicitly disabling all four categories stops capture on update and
    starts no capture on create.
    """

    enabled: bool
    """Request shortcut for browser telemetry capture.

    True enables capture using VM defaults. False stops capture on update and starts
    no capture on create. Cannot be combined with browser category settings.
    """
