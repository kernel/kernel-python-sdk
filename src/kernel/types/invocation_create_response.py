# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvocationCreateResponse"]


class InvocationCreateResponse(BaseModel):
    id: str
    """ID of the invocation"""

    action_name: str
    """Name of the action invoked"""

    status: Literal["queued", "running", "succeeded", "failed"]
    """Status of the invocation"""

    output: Optional[str] = None
    """The action result or detailed failure output.

    Often a JSON-encoded value, but failures may contain plain text. May contain
    sensitive application data.
    """

    status_reason: Optional[str] = None
    """
    A nonempty, customer-safe summary of the recorded failure output, always present
    when status is failed and omitted otherwise. Recognized messages receive a
    specific summary; other failures receive a generic summary. Message matching
    does not establish whether the failure originated in the platform or action
    code. Does not include raw action output or internal error details.
    Human-readable text, not a stable identifier for retry logic.
    """
