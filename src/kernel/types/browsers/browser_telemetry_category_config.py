# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserTelemetryCategoryConfig"]


class BrowserTelemetryCategoryConfig(BaseModel):
    """Per-category telemetry configuration."""

    enabled: Optional[bool] = None
    """Whether this category is captured.

    Selection is opt-in, so an omitted category is not captured.
    """
