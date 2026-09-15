# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemRetrieveParams"]


class ItemRetrieveParams(TypedDict, total=False):
    id_or_name: Required[str]

    expand: List[Literal["payment_methods"]]
    """Live fields advertised by `available_expansions` to include in `expanded`."""

    wait: int
    """
    Hold for up to this many seconds while the item is pending authorization,
    approval, or credential collection. Return the current item when ready or when
    the wait elapses. This does not wait for edits to an already-ready credential;
    poll GET without wait and compare version to observe changes after collect.
    """
