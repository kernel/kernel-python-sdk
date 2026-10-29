# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrowserFingerprintParam"]


class BrowserFingerprintParam(TypedDict, total=False):
    """Overrides for browser attributes presented to websites."""

    os: Required[Literal["macos"]]
    """Operating system the browser reports to websites."""
