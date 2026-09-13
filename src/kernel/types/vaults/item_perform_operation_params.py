# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .vault_card_fill_field_param import VaultCardFillFieldParam

__all__ = ["ItemPerformOperationParams", "AuthorizeVaultItemOperationRequest", "FillVaultItemOperationRequest"]


class AuthorizeVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    type: Required[Literal["authorize"]]


class FillVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    browser_id: Required[str]
    """Browser session ID, not a reusable browser name."""

    fields: Required[Iterable[VaultCardFillFieldParam]]
    """Field bindings for this step. No two bindings may resolve to the same element."""

    page_url: Required[str]
    """Exact current top-level page URL, including path, query, and fragment.

    Must match exactly one open page in the browser; zero or multiple matches fail.
    No prefix or glob matching. Must use HTTPS without embedded credentials.
    """

    type: Required[Literal["fill"]]

    timeout_ms: int
    """Total operation deadline in milliseconds, not a per-field timeout."""


ItemPerformOperationParams: TypeAlias = Union[AuthorizeVaultItemOperationRequest, FillVaultItemOperationRequest]
