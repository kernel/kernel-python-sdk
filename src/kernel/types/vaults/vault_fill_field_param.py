# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VaultFillFieldParam"]


class VaultFillFieldParam(TypedDict, total=False):
    field: Required[str]
    """A declared credential field name or a supported card field.

    Unset credential fields cannot be filled.
    """

    selector: Required[str]

    format: Literal["MM/YY", "MM/YYYY"]
    """Required only for a card's combined expiration field.

    Forbidden for other card fields and all credential fields.
    """
