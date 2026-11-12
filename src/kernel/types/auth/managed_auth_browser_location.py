# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ManagedAuthBrowserLocation"]


class ManagedAuthBrowserLocation(BaseModel):
    """
    Browser locale applied to browser sessions created for a managed auth connection.
    """

    locale: Optional[str] = None
    """
    Supported canonical BCP 47 locale for the browser's language and Accept-Language
    header. Omit to use the default for the browser's region, or omit on update to
    keep the current locale. Null clears it on update.
    """
