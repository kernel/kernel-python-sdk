# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .browser_location_source import BrowserLocationSource

__all__ = ["BrowserLocation"]


class BrowserLocation(BaseModel):
    locale: str
    """Effective canonical BCP 47 formatting locale selected for the browser session."""

    locale_source: BrowserLocationSource
    """Where one effective browser location field came from.

    `override` is set explicitly on the session; `default` comes from the browser's
    region.
    """

    timezone: str
    """Effective IANA timezone selected for the browser session."""

    timezone_source: BrowserLocationSource
    """Where one effective browser location field came from.

    `override` is set explicitly on the session; `default` comes from the browser's
    region.
    """
