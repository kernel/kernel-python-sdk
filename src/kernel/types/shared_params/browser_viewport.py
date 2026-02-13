# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserViewport"]


class BrowserViewport(TypedDict, total=False):
    """Initial browser window size in pixels with optional refresh rate.

    If omitted, image defaults apply (1920x1080@25).
    Arbitrary viewport dimensions are accepted, but the following configurations are known-good and fully tested:
    2560x1440@10, 1920x1080@25, 1920x1200@25, 1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60.
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
