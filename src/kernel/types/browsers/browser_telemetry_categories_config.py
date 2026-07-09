# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .browser_telemetry_category_config import BrowserTelemetryCategoryConfig

__all__ = ["BrowserTelemetryCategoriesConfig"]


class BrowserTelemetryCategoriesConfig(BaseModel):
    """Per-category telemetry capture settings layered onto the default set.

    The operational signals (control, connection, system, captcha) are on by default and are opt-out: set one to enabled=false to stop capturing it. The CDP categories (console, network, page, interaction) and screenshot are off by default and are opt-in: set enabled=true to capture them.
    """

    captcha: Optional[BrowserTelemetryCategoryConfig] = None
    """Captcha solve attempt outcomes. On by default."""

    connection: Optional[BrowserTelemetryCategoryConfig] = None
    """Client attach/detach lifecycle for the CDP proxy and live view. On by default."""

    console: Optional[BrowserTelemetryCategoryConfig] = None
    """Console output (log, warn, error) and uncaught exceptions.

    CDP category; off by default.
    """

    control: Optional[BrowserTelemetryCategoryConfig] = None
    """Agent-driven actions against the browser, such as inbound calls to the in-VM
    API.

    On by default.
    """

    interaction: Optional[BrowserTelemetryCategoryConfig] = None
    """User interaction events including clicks, keydowns, and scroll-settled events.

    CDP category; off by default.
    """

    network: Optional[BrowserTelemetryCategoryConfig] = None
    """
    HTTP request and response metadata including URL, method, status code, and
    timing. Request post data is forwarded as-is from CDP. Text response bodies are
    truncated at 8 KB for structured types (JSON, XML, form data) and 4 KB for other
    text types. Binary responses (images, fonts, media) are excluded. CDP category;
    off by default.
    """

    page: Optional[BrowserTelemetryCategoryConfig] = None
    """
    Page lifecycle events including navigation, DOMContentLoaded, load, layout
    shifts, and LCP. CDP category; off by default.
    """

    screenshot: Optional[BrowserTelemetryCategoryConfig] = None
    """Periodic base64-encoded viewport screenshots.

    High volume; off by default and must be opted into.
    """

    system: Optional[BrowserTelemetryCategoryConfig] = None
    """Browser VM health, such as out-of-memory kills and managed-service crashes.

    On by default.
    """
