# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .browser_telemetry_categories_config import BrowserTelemetryCategoriesConfig

__all__ = ["BrowserTelemetryConfig"]


class BrowserTelemetryConfig(BaseModel):
    """Active telemetry configuration for a browser session."""

    browser: Optional[BrowserTelemetryCategoriesConfig] = None
    """Per-category enable/disable flags."""
