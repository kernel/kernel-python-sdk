# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .browser_telemetry_cdp_control_config import BrowserTelemetryCdpControlConfig

__all__ = ["BrowserTelemetryControlConfig"]


class BrowserTelemetryControlConfig(BaseModel):
    """Configuration for the control category.

    Same enabled semantics as any other category, plus settings for the browser-control commands the CDP proxy reports.
    """

    cdp: Optional[BrowserTelemetryCdpControlConfig] = None
    """Settings for the cdp_command events the CDP proxy reports.

    Merged independently of enabled, so a later update that only sets enabled keeps
    the current exclusion list.
    """

    enabled: Optional[bool] = None
    """Whether this category is captured.

    Control is on by default; set false to opt out.
    """
