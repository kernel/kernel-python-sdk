# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .browser_telemetry_export_config import BrowserTelemetryExportConfig
from .browser_telemetry_storage_config import BrowserTelemetryStorageConfig
from .browser_telemetry_categories_config import BrowserTelemetryCategoriesConfig

__all__ = ["BrowserTelemetryConfig"]


class BrowserTelemetryConfig(BaseModel):
    """Active telemetry configuration for a browser session."""

    browser: Optional[BrowserTelemetryCategoriesConfig] = None
    """Per-category enable/disable flags."""

    export: Optional[BrowserTelemetryExportConfig] = None
    """Where the session's captured telemetry is being exported.

    Omitted when the export state is unknown.
    """

    storage: Optional[BrowserTelemetryStorageConfig] = None
    """Whether the session's captured telemetry is persisted to Kernel storage.

    Omitted for browsers created before this setting existed, which persist it.
    """
