# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .browser_telemetry_category_config_param import BrowserTelemetryCategoryConfigParam

__all__ = ["BrowserTelemetryCategoriesConfigParam"]


class BrowserTelemetryCategoriesConfigParam(TypedDict, total=False):
    """Per-category telemetry capture settings."""

    console: BrowserTelemetryCategoryConfigParam
    """Console output (log, warn, error) and uncaught exceptions."""

    interaction: BrowserTelemetryCategoryConfigParam
    """User interaction events including clicks, keydowns, and scroll-settled events."""

    network: BrowserTelemetryCategoryConfigParam
    """
    HTTP request and response metadata including URL, method, status code, and
    timing. Request post data is forwarded as-is from CDP. Text response bodies are
    truncated at 8 KB for structured types (JSON, XML, form data) and 4 KB for other
    text types. Binary responses (images, fonts, media) are excluded.
    """

    page: BrowserTelemetryCategoryConfigParam
    """
    Page lifecycle events including navigation, DOMContentLoaded, load, layout
    shifts, and LCP.
    """
