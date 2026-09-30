# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OnePasswordFillVaultItemOperationRequestParam"]


class OnePasswordFillVaultItemOperationRequestParam(TypedDict, total=False):
    """Fill and submit an approved 1Password login in the selected browser page.

    The page must share the selected entry's login origin. Supply entry_id when more than one approved entry matches the page origin. The extension selects fields; callers cannot supply selectors or secret values. Submission does not confirm website authentication.
    """

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
