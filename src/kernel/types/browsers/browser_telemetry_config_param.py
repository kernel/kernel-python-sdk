# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = ["BrowserTelemetryConfigParam"]


class BrowserTelemetryConfigParam(TypedDict, total=False):
    """Telemetry configuration for a browser session."""

    browser: BrowserTelemetryCategoriesConfigParam
    """Per-category enable/disable flags. If omitted, all categories are captured."""
