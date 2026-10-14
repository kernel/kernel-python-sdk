# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .vault_fill_field_param import VaultFillFieldParam

__all__ = ["FillVaultItemOperationRequestParam"]


class FillVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Use a vault item in a browser session, for example to fill a login or
    payment form. Only invoke when the item advertises `fill`; the advertised
    operation describes the inputs that item needs. Requires `browser_id` and
    usually `page_url`; some items also require `fields`. Browser and vault must
    belong to the same project. Kernel checks access and allowed destinations
    before filling; providing a page URL does not authorize a destination.

    Fill never submits forms or clicks buttons, though input and change events
    may trigger site behavior. It is not atomic: completed steps are not rolled
    back. Fill does not consume the item, so a failed or indeterminate fill is
    safe to retry. A retry right after an indeterminate fill may wait up to 15
    seconds for the earlier attempt's browser lock to expire.

    Secret values are never returned or included in operation logs, traces,
    audit events, or error details. This does not prevent an agent with
    unrestricted browser access from reading values from the page or other
    browser observation surfaces.
    """

    browser_id: Required[str]
    """Browser session ID, not a reusable browser name."""

    type: Required[Literal["fill"]]

    fields: Iterable[VaultFillFieldParam]
    """
    Field bindings, when the item's advertised fill operation requires them. Each
    selector is searched in the main frame and all descendant frames and must
    resolve to exactly one editable input or select, matched directly or through a
    containing element; zero or multiple candidates fail, and no two bindings may
    resolve to the same element. Select elements match an option by value, not
    label. All bindings are validated before any write, then filled in request
    order, stopping at the first failure. If the page navigates or a target
    disappears, fill stops rather than choosing another page or element.
    """

    page_url: str
    """Exact current top-level page URL, including path, query, and fragment.

    Must match exactly one open page in the browser; zero or multiple matches fail.
    No prefix or glob matching. When an item allows omitting it, the browser must
    have exactly one open page.
    """

    timeout_ms: int
    """Total operation deadline in milliseconds, not a per-field timeout."""
