# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserReplParams"]


class BrowserReplParams(TypedDict, total=False):
    code: Required[str]
    """JavaScript evaluated in a persistent Node.js runtime.

    Top-level bindings persist until the browser VM's API process exits, the REPL is
    reset, or the REPL is terminated after a crash or timeout. Static top-level
    imports are unsupported; use dynamic `import()`. Expression values are ignored;
    emit output with `repl.write(...)`, console methods, or `repl.emitImage(...)`.
    May be empty only when `reset` is true.
    """

    reset: bool
    """Terminate the current REPL, start a fresh one, and then evaluate code."""

    timeout_sec: int
    """Maximum execution time in seconds. Default is 60."""
