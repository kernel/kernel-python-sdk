# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BrowserLocationUpdateRequestParam"]


class BrowserLocationUpdateRequestParam(TypedDict, total=False):
    """
    Omit a field to leave it unchanged, set a string override, or set null to clear the override and use the default for the browser's region.
    """

    locale: Optional[str]
    """Session-only supported canonical BCP 47 locale override.

    Null clears the override and uses the browser region's default.
    """

    timezone: Optional[str]
    """Session-only IANA timezone override.

    Null clears the override and uses the browser region's default.
    """
