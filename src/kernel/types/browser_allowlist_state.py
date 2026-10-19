# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BrowserAllowlistState"]


class BrowserAllowlistState(BaseModel):
    revision: str
    """Opaque revision to pass as network.expected_allowlist_revision on an update."""

    base_revision: Optional[str] = None
    """
    Revision against which that mutation was accepted; reuse it when retrying the
    mutation.
    """

    mutation_id: Optional[str] = None
    """ID of the last conditional allowlist update saved on this browser."""
