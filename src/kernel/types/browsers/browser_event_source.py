# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrowserEventSource"]


class BrowserEventSource(BaseModel):
    """Provenance metadata identifying which producer emitted the event."""

    kind: Literal["cdp", "kernel_api", "extension", "local_process"]
    """Event producer.

    cdp: Chrome DevTools Protocol events from the browser. kernel_api: Kernel API
    server. extension: injected Chrome extension. local_process: system process
    running alongside the browser.
    """

    event: Optional[str] = None
    """Producer-specific event name (e.g.

    Runtime.consoleAPICalled for CDP-sourced console events, Runtime.exceptionThrown
    for uncaught exceptions).
    """

    metadata: Optional[Dict[str, str]] = None
    """Producer-specific context (e.g. CDP target/session/frame IDs)."""
