# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["VaultCardFillFieldParam", "VaultCardStoredFillField", "VaultCardExpirationFillField"]


class VaultCardStoredFillField(TypedDict, total=False):
    field: Required[
        Literal[
            "number",
            "exp_month",
            "exp_year",
            "cvc",
            "billing_name",
            "billing_line1",
            "billing_line2",
            "billing_city",
            "billing_state",
            "billing_postal_code",
            "billing_country",
        ]
    ]
    """Field in the decrypted card, not an alias.

    Number and CVC preserve leading zeros; month uses two digits and year uses four
    digits. Billing fields use the provider's stored billing address (name, line1,
    line2, city, state, postal_code, country) without reformatting. Request only
    needed billing fields. An absent or empty requested billing field returns 400
    field_unavailable before any browser writes; it does not make other card fields
    unavailable.
    """

    selector: Required[str]
    """CSS selector for an editable input or select, or a containing element.

    Must resolve to one unique editable element across all page frames.
    """


class VaultCardExpirationFillField(TypedDict, total=False):
    """
    Combined expiration derived from the stored month and year; not a separate stored secret.
    """

    field: Required[Literal["expiration"]]

    format: Required[Literal["MM/YY", "MM/YYYY"]]

    selector: Required[str]
    """CSS selector for an editable input or select, or a containing element.

    Must resolve to one unique editable element across all page frames.
    """


VaultCardFillFieldParam: TypeAlias = Union[VaultCardStoredFillField, VaultCardExpirationFillField]
