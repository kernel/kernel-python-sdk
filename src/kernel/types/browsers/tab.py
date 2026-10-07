# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Tab"]


class Tab(BaseModel):
    """The tab 'page' was bound to for this call.

    Absent if the call failed before binding a tab.
    """

    created: bool
    """Whether this call opened the tab.

    For a named executor this happens on its first call and after its previous tab
    was closed. For the default executor it happens only when the browser had no
    open page.
    """

    target_id: str
    """CDP page target ID of the tab"""
