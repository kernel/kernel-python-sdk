# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["APIKeyRetrieveParams"]


class APIKeyRetrieveParams(TypedDict, total=False):
    include_deleted: bool
    """
    When true, return the API key even if it has been deleted (soft-deleted), for
    audit purposes. Defaults to false, which returns 404 for a deleted key.
    """
