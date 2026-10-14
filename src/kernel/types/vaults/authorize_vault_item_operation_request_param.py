# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuthorizeVaultItemOperationRequestParam"]


class AuthorizeVaultItemOperationRequestParam(TypedDict, total=False):
    """Authorize a Link or Kernel card using its existing purchase specification.

    Use only after explicit user approval and when the item advertises authorize; follow the advertised operation's description. For a Link card, pass browser_id and page_url together while the browser is on the final checkout page: Kernel inspects that checkout, chooses how the credential is delivered, and limits fill to that checkout's origin in any browser with this vault attached. Omitting both issues a virtual card that fills any page on the merchant origin. Once approval has been requested, browser_id and page_url are ignored and authorize only re-checks the request. Browser and checkout inspection errors occur before any provider request and can be retried once the browser is on the checkout page. Kernel cards do not accept browser_id or page_url.
    """

    type: Required[Literal["authorize"]]

    browser_id: str
    """Browser session ID, not a reusable browser name.

    The browser must have this vault attached.
    """

    page_url: str
    """Exact current top-level URL of the final checkout page open in browser_id."""
