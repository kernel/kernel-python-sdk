# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserLocationRequestParam"]


class BrowserLocationRequestParam(TypedDict, total=False):
    locale: str
    """Session-only supported canonical BCP 47 locale override.

    Omit to use the default for the browser's region.
    """

    timezone: str
    """Session-only IANA timezone override.

    Omit to use the default for the browser's region.
    """
