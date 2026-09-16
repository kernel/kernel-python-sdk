# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .vault_fill_field_param import VaultFillFieldParam

__all__ = ["FillVaultItemOperationRequestParam"]


class FillVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Fill selected fields from one ready credential or ready, unexpired Link card
    into a browser linked to its vault.
    Only invoke when the item advertises `fill`. Browser and vault must belong
    to the same project. Kernel checks access and allowed destinations before
    filling; providing a page URL does not authorize a destination.

    Find exactly one open page matching `page_url`. Credential items may omit
    `page_url` to require exactly one open page; cards require an HTTPS page URL.
    Credentials have no destination allowlist. TOTP fields generate a current
    code immediately before writing; their seeds never enter the browser. For each selector, search
    the main frame and all descendant frames for editable inputs or selects
    matched directly or contained within matching elements. Each selector must
    resolve to one unique editable element across all frames; zero or multiple
    candidates fail. Count each element once, even if multiple matching
    containers contain it. Validate all bindings before filling.
    Select elements match an option by its value, not its label.
    If the page navigates or a target disappears during filling, stop rather
    than selecting a different page or element.

    Fill in request order and stop on the first failure. This operation is
    not atomic: previously filled fields are not rolled back. Never submit
    the form or click buttons, though input/change events may trigger site
    behavior. Link cards use fill for browser checkout and do not expose
    aliases or support egress substitution. Do not automatically retry a
    failed or indeterminate operation.

    Secret values are never returned or included in operation logs, traces,
    audit events, or error details. This does not prevent an agent with
    unrestricted browser access from reading values from the page or other
    browser observation surfaces.
    """

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
