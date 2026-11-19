# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrowserFingerprint"]


class BrowserFingerprint(BaseModel):
    """Overrides for browser attributes presented to websites."""

    os: Literal["linux", "macos"]
    """Operating system the browser reports to websites."""
