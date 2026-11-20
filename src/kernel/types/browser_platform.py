# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .browser_os import BrowserOs

__all__ = ["BrowserPlatform"]


class BrowserPlatform(BaseModel):
    """Host platform settings for the browser session."""

    os: BrowserOs
    """Operating system of the browser's host."""
