# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvocationStateEvent", "Invocation"]


class Invocation(BaseModel):
    id: str
    """ID of the invocation"""

    action_name: str
    """Name of the action invoked"""

    app_name: str
    """Name of the application"""

    started_at: datetime
    """RFC 3339 Nanoseconds timestamp when the invocation started"""

    status: Literal["queued", "running", "succeeded", "failed"]
    """Status of the invocation"""

    version: str
    """Version label for the application"""

    finished_at: Optional[datetime] = None
    """
    RFC 3339 Nanoseconds timestamp when the invocation finished (null if still
    running)
    """

    output: Optional[str] = None
    """The action result or detailed failure output.

    Often a JSON-encoded value, but failures may contain plain text. May contain
    sensitive application data.
    """

    payload: Optional[str] = None
    """Payload provided to the invocation.

    This is a string that can be parsed as JSON.
    """

    status_reason: Optional[str] = None
    """
    A nonempty, customer-safe summary of the recorded failure output, always present
    when status is failed and omitted otherwise, including in the first failed
    invocation_state event. Recognized messages receive a specific summary; other
    failures receive a generic summary. Message matching does not establish whether
    the failure originated in the platform or action code. Does not include raw
    action output or internal error details. Available for historical invocations as
    well. Human-readable text, not a stable identifier for retry logic.
    """


class InvocationStateEvent(BaseModel):
    """An event representing the current state of an invocation."""

    event: Literal["invocation_state"]
    """Event type identifier (always "invocation_state")."""

    invocation: Invocation

    timestamp: datetime
    """Time the state was reported."""
