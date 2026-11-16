# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserCaptchaSolverParam"]


class BrowserCaptchaSolverParam(TypedDict, total=False):
    """Automatic CAPTCHA solving configuration."""

    enabled: Required[bool]
    """Whether the browser automatically solves CAPTCHAs."""
