# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["BrowserNetworkUpdateParam"]


class BrowserNetworkUpdateParam(TypedDict, total=False):
    """Network configuration changes for a running browser session.

    Other network settings can only be set at creation.
    """

    allowed_hosts: Optional[SequenceNotStr[str]]
    """
    Replaces the session's egress allowlist, using the same entry rules as
    network.allowed_hosts on create. Only an allowlist the browser was created with
    can be changed: a browser created without one can't be given one, and an
    allowlist removed with null can't be added back. Omit to leave the allowlist
    unchanged, or set to null to remove it and return to unfiltered egress; an empty
    list is invalid. The new list applies without restarting the browser: new
    requests to destinations it no longer allows are refused within a few seconds,
    and open connections to them are closed within about 30 seconds, or up to 10
    minutes during a Kernel deploy. Connections to destinations it still allows,
    such as WebSockets, stay open. A start_url in the same request must be allowed
    by the updated list, and is loaded only after the list takes effect. Requires a
    browser created with proxy v3. Supported on leased pooled browsers; the pool's
    allowlist is restored before reuse, or the browser is destroyed if it cannot be
    safely restored. If the request fails, retry it: the new list may already apply
    to some requests.
    """
