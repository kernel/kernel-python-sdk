# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .browser_telemetry_cdp_control_config_param import BrowserTelemetryCdpControlConfigParam

__all__ = ["BrowserTelemetryControlConfigParam"]


class BrowserTelemetryControlConfigParam(TypedDict, total=False):
    """Configuration for the control category.

    Same enabled semantics as any other category, plus settings for the browser-control commands the CDP proxy reports.
    """

    cdp: BrowserTelemetryCdpControlConfigParam
    """Settings for the cdp_command events the CDP proxy reports.

    Merged independently of enabled, so a later update that only sets enabled keeps
    the current exclusion list.
    """

    enabled: bool
    """Whether this category is captured.

    Control is on by default; set false to opt out.
    """
