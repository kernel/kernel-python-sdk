# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .browser_repl_content import BrowserReplContent

__all__ = ["BrowserReplResult"]


class BrowserReplResult(BaseModel):
    """Result of Browser REPL code execution."""

    repl_id: str
    """CUID2 identifying the exact state-holding REPL process used for this execution.

    Stable across calls and Chromium reconnects; changes after an API restart,
    explicit reset, execution timeout, or REPL crash.
    """

    success: bool
    """Whether the code executed successfully."""

    content: Optional[List[BrowserReplContent]] = None
    """Optional ordered text/image output produced by the execution."""

    content_truncated: Optional[bool] = None
    """True if text or image output was dropped or truncated due to response limits."""

    duration_ms: Optional[int] = None
    """Wall-clock execution time in milliseconds."""

    error: Optional[str] = None
    """Error message if execution failed."""

    repl_terminated: Optional[bool] = None
    """
    True if the REPL identified by `repl_id` was terminated by this request. The
    next request lazily starts a fresh REPL with a new `repl_id`.
    """

    stack: Optional[str] = None
    """Stack trace if execution failed."""
