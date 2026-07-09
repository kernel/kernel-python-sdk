# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserTelemetryCategoryConfig"]


class BrowserTelemetryCategoryConfig(BaseModel):
    """Per-category telemetry configuration."""

    enabled: Optional[bool] = None
    """Whether this category is captured.

    Operational categories (control, connection, system, captcha) default to true;
    set false to opt out. CDP categories (console, network, page, interaction) and
    screenshot default to false; set true to opt in.
    """
