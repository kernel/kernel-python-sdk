# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .browser_os import BrowserOs

__all__ = ["BrowserPlatformParam"]


class BrowserPlatformParam(TypedDict, total=False):
    """Host platform settings for the browser session."""

    os: Required[BrowserOs]
    """Operating system of the browser's host."""
