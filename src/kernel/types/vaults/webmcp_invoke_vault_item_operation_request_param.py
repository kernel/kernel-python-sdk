# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from .vault_webmcp_binding_param import VaultWebmcpBindingParam

__all__ = ["WebmcpInvokeVaultItemOperationRequestParam"]


class WebmcpInvokeVaultItemOperationRequestParam(TypedDict, total=False):
    """Invoke a WebMCP tool using values from a vaulted item.

    The browser must be
    attached to the item's vault. Discover the tool_ref, inputSchema, and source
    with GET /browsers/{id_or_name}/webmcp/tools or webmcp.listTools() in the
    Browser REPL (POST /browsers/{id_or_name}/repl) before invoking it.
    Input paths replace existing null slots in input. Tool output is returned
    without redaction and may include the supplied values. The tool may submit
    or perform other side effects. Any item destination
    restrictions apply to the tool's top-level page and registering frame (if any).
    """

    bindings: Required[Iterable[VaultWebmcpBindingParam]]

    browser_id: Required[str]
    """Browser session ID, not a reusable browser name."""

    input: Required[Dict[str, object]]
    """Public tool arguments with an existing null slot at each binding path.

    At most 64 KiB after JSON serialization, including substituted values. Never
    include vault values here.
    """

    page_url: Required[str]
    """Exact top-level URL from the discovered tool source (fragment omitted).

    This pins the target page; it does not authorize a destination.
    """

    tool_ref: Required[str]
    """Opaque reference to the exact live WebMCP registration."""

    type: Required[Literal["webmcp_invoke"]]

    timeout_sec: int
    """
    Tool invocation timeout in seconds; preflight and response handling have an
    additional bounded allowance. An indeterminate outcome is not retried.
    """
