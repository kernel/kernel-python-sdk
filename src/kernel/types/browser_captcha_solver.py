# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BrowserCaptchaSolver"]


class BrowserCaptchaSolver(BaseModel):
    """Automatic CAPTCHA solving configuration."""

    enabled: bool
    """Whether the browser automatically solves CAPTCHAs."""
