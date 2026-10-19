# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserAllowlistStateParam"]


class BrowserAllowlistStateParam(TypedDict, total=False):
    revision: Required[str]
    """Opaque revision to pass as network.expected_allowlist_revision on an update."""

    base_revision: str
    """
    Revision against which that mutation was accepted; reuse it when retrying the
    mutation.
    """

    mutation_id: str
    """ID of the last conditional allowlist update saved on this browser."""
