# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ReplayStartParams"]


class ReplayStartParams(TypedDict, total=False):
    framerate: int
    """Recording framerate in fps.

    Values above 20 require GPU to be enabled on the browser session.
    """

    max_duration_in_seconds: int
    """Maximum recording duration in seconds."""
