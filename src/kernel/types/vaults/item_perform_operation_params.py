# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .vault_fill_field_param import VaultFillFieldParam
from .vault_checkout_context_param import VaultCheckoutContextParam

__all__ = [
    "ItemPerformOperationParams",
    "AuthorizeVaultItemOperationRequest",
    "CollectVaultItemOperationRequest",
    "PrepareCheckoutVaultItemOperationRequest",
    "FillVaultItemOperationRequest",
    "OnePasswordRequestAccessVaultItemOperationRequest",
    "OnePasswordPollAccessVaultItemOperationRequest",
    "OnePasswordFillVaultItemOperationRequest",
    "OnePasswordRecoverVaultItemOperationRequest",
    "OnePasswordUpdateAccessTokenVaultItemOperationRequest",
]


class AuthorizeVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    type: Required[Literal["authorize"]]


class CollectVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    type: Required[Literal["collect"]]


class PrepareCheckoutVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    checkout: Required[VaultCheckoutContextParam]
    """
    Required when preparing an unused AgentCard card for a supported checkout
    processor. Consent is bound to this browser and declared merchant origin, not a
    tab. Wait for the item's ready_to_submit status before native Pay and submit
    within its readiness deadline. Unused preparations expire automatically; every
    preparation is single-use, including after failure or expiry.
    """

    type: Required[Literal["prepare_checkout"]]


class FillVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    browser_id: Required[str]
    """Browser session ID, not a reusable browser name."""

    fields: Required[Iterable[VaultFillFieldParam]]
    """Field bindings for this step. No two bindings may resolve to the same element."""

    type: Required[Literal["fill"]]

    page_url: str
    """Exact current top-level page URL, including path, query, and fragment.

    Must match exactly one open page in the browser; zero or multiple matches fail.
    No prefix or glob matching. Required for cards, which must use HTTPS without
    embedded credentials. Optional for credentials, where omission requires exactly
    one open page.
    """

    timeout_ms: int
    """Total operation deadline in milliseconds, not a per-field timeout."""


class OnePasswordRequestAccessVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    browser_id: Required[str]
    """Kernel browser session used to invoke the extension."""

    type: Required[Literal["1pw_create_access_request"]]

    goal: str

    keywords: SequenceNotStr[str]

    reason: str


class OnePasswordPollAccessVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    browser_id: Required[str]

    type: Required[Literal["1pw_access_request_status"]]

    timeout_seconds: int


class OnePasswordFillVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    browser_id: Required[str]
    """Browser session ID, not a reusable browser name."""

    page_url: Required[str]
    """Exact current top-level page URL.

    Must match exactly one open page in the browser.
    """

    type: Required[Literal["1pw_fill"]]

    entry_id: str
    """ID of an approved request entry.

    Required when several approved entries have the page's origin.
    """

    timeout_ms: int


class OnePasswordRecoverVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    type: Required[Literal["1pw_recover"]]


class OnePasswordUpdateAccessTokenVaultItemOperationRequest(TypedDict, total=False):
    id_or_name: Required[str]

    access_token: Required[str]

    type: Required[Literal["1pw_update_access_token"]]

    access_token_expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional supplied expiry. Omit to clear the old expiry."""


ItemPerformOperationParams: TypeAlias = Union[
    AuthorizeVaultItemOperationRequest,
    CollectVaultItemOperationRequest,
    PrepareCheckoutVaultItemOperationRequest,
    FillVaultItemOperationRequest,
    OnePasswordRequestAccessVaultItemOperationRequest,
    OnePasswordPollAccessVaultItemOperationRequest,
    OnePasswordFillVaultItemOperationRequest,
    OnePasswordRecoverVaultItemOperationRequest,
    OnePasswordUpdateAccessTokenVaultItemOperationRequest,
]
