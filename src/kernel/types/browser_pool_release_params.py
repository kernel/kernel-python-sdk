# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserPoolReleaseParams"]


class BrowserPoolReleaseParams(TypedDict, total=False):
    session_id: Required[str]
    """Browser session ID to release back to the pool"""

    reuse: bool
    """Whether to reuse the browser instance or destroy it and create a new one.

    Defaults to true. A reused browser keeps the configuration it was created with,
    so it does not pick up pool configuration changes made while it was in use.
    Release with `reuse: false`, or flush the pool afterward, to rebuild it with the
    current configuration.
    """
