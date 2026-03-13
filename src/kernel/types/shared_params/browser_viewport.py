# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserViewport"]


class BrowserViewport(TypedDict, total=False):
    """
    Initial browser window size in pixels with optional refresh rate.
    If omitted, image defaults apply (1920x1080@25).
    For GPU images, the default is 1920x1080@60.
    Arbitrary viewport dimensions and refresh rates are accepted.
    Known-good presets include:
    2560x1440@10, 1920x1080@25, 1920x1200@25, 1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60.
    For GPU images, recommended presets use one of these resolutions with refresh rates 60, 30, 25, or 10:
    800x600, 960x720, 1024x576, 1024x768, 1152x648, 1200x800, 1280x720, 1368x768, 1440x900, 1600x900, 1920x1080, 1920x1200, 390x844, 360x250, 768x1024, 800x1600.
    Viewports outside this list may exhibit unstable live view or recording behavior.
    If refresh_rate is not provided, it will be automatically determined based on the resolution
    (higher resolutions use lower refresh rates to keep bandwidth reasonable).
    """

    height: Required[int]
    """Browser window height in pixels."""

    width: Required[int]
    """Browser window width in pixels."""

    refresh_rate: int
    """Display refresh rate in Hz.

    If omitted, automatically determined from width and height.
    """
