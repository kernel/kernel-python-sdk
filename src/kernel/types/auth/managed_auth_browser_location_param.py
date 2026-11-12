# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ManagedAuthBrowserLocationParam"]


class ManagedAuthBrowserLocationParam(TypedDict, total=False):
    """
    Browser locale applied to browser sessions created for a managed auth connection.
    """

    locale: Optional[str]
    """
    Supported canonical BCP 47 locale for the browser's language and Accept-Language
    header. Omit to use the default for the browser's region, or omit on update to
    keep the current locale. Null clears it on update.
    """
