# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserTelemetryCategoryConfigParam"]


class BrowserTelemetryCategoryConfigParam(TypedDict, total=False):
    """Per-category telemetry configuration."""

    enabled: bool
    """Whether this category is captured.

    Operational categories (control, connection, system, captcha) default to true;
    set false to opt out. CDP categories (console, network, page, interaction) and
    screenshot default to false; set true to opt in.
    """
