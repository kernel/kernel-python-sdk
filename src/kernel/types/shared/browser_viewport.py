# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserViewport"]


class BrowserViewport(BaseModel):
    """Initial browser window size in pixels with optional refresh rate.

    If omitted, image defaults apply (1920x1080@25).
    Only specific viewport configurations are supported. The server will reject unsupported combinations.
    Supported resolutions are: 2560x1440@10, 1920x1080@25, 1920x1200@25, 1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60
    If refresh_rate is not provided, it will be automatically determined from the width and height if they match a supported configuration exactly.
    Note: Higher resolutions may affect the responsiveness of live view browser
    """

    height: int
    """Browser window height in pixels."""

    width: int
    """Browser window width in pixels."""

    refresh_rate: Optional[int] = None
    """Display refresh rate in Hz.

    If omitted, automatically determined from width and height.
    """
