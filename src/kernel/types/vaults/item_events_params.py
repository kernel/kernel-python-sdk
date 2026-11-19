# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ItemEventsParams"]


class ItemEventsParams(TypedDict, total=False):
    id_or_name: Required[str]

    after: str
    """Return events after this event ID."""

    include_deleted: bool
    """When true, also finds deleted items, and deleted vaults by ID only.

    `key` then also accepts an item ID, which takes precedence over a key with the
    same value; the lookup order is the item ID, then the live item with that key,
    then the most recently deleted one. `wait` is ignored for a deleted item or
    vault.
    """

    wait: int
    """Long-poll for new events for up to this many seconds."""
