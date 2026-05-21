# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .browser_telemetry_category_config import BrowserTelemetryCategoryConfig

__all__ = ["BrowserTelemetryCategoriesConfig"]


class BrowserTelemetryCategoriesConfig(BaseModel):
    """Per-category telemetry capture settings."""

    console: Optional[BrowserTelemetryCategoryConfig] = None
    """Console output (log, warn, error) and uncaught exceptions."""

    interaction: Optional[BrowserTelemetryCategoryConfig] = None
    """User interaction events including clicks, keydowns, and scroll-settled events."""

    network: Optional[BrowserTelemetryCategoryConfig] = None
    """
    HTTP request and response metadata including URL, method, status code, and
    timing. Request post data is forwarded as-is from CDP. Text response bodies are
    truncated at 8 KB for structured types (JSON, XML, form data) and 4 KB for other
    text types. Binary responses (images, fonts, media) are excluded.
    """

    page: Optional[BrowserTelemetryCategoryConfig] = None
    """
    Page lifecycle events including navigation, DOMContentLoaded, load, layout
    shifts, and LCP.
    """
