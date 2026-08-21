# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .browser_cdp_command_method import BrowserCdpCommandMethod

__all__ = ["BrowserTelemetryCdpControlConfig"]


class BrowserTelemetryCdpControlConfig(BaseModel):
    """Settings for the cdp_command events the CDP proxy reports."""

    excluded_methods: Optional[List[BrowserCdpCommandMethod]] = None
    """Methods to leave out of the cdp_command stream.

    Omit the list to keep the current one; send an empty list to report every
    supported method again. Exclusion is a telemetry setting only: an excluded
    command is still relayed to the browser unchanged, it simply produces no event.
    Use it to drop the highest-volume methods — Input.dispatchMouseEvent during a
    humanized cursor path, or Page.captureScreenshot under a screencast — without
    turning the whole category off. Excluded commands are counted in
    cdp_disconnect.telemetry_excluded.
    """
