# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserTelemetryStorageConfig"]


class BrowserTelemetryStorageConfig(BaseModel):
    """Kernel storage state for a session's captured telemetry."""

    enabled: Optional[bool] = None
    """Whether captured telemetry is persisted to Kernel storage.

    When off, the session's events are only available on the live stream and through
    any configured export.
    """
