# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BrowserUsage"]


class BrowserUsage(BaseModel):
    """Session usage metrics."""

    uptime_ms: int
    """Time in milliseconds the session was actively running."""
