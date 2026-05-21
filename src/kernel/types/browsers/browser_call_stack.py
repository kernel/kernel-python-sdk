# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrowserCallStack", "CallFrame"]


class CallFrame(BaseModel):
    column_number: int = FieldInfo(alias="columnNumber")
    """Zero-based column number within the line."""

    function_name: str = FieldInfo(alias="functionName")
    """JavaScript function name, or empty string for anonymous functions."""

    line_number: int = FieldInfo(alias="lineNumber")
    """Zero-based line number within the script."""

    script_id: str = FieldInfo(alias="scriptId")
    """CDP script identifier."""

    url: str
    """URL or name of the script file."""


class BrowserCallStack(BaseModel):
    """
    CDP Runtime.StackTrace representing the JavaScript call stack at the time of an event. Fields use CDP naming conventions rather than snake_case to match the Chrome DevTools Protocol wire format.
    """

    call_frames: List[CallFrame] = FieldInfo(alias="callFrames")
    """Ordered list of call frames, outermost first."""

    description: Optional[str] = None
    """Optional label for the stack trace (e.g. async cause)."""

    parent: Optional["BrowserCallStack"] = None
    """Parent stack trace for async stacks."""
