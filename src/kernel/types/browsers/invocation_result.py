# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InvocationResult"]


class InvocationResult(BaseModel):
    invocation_id: str

    status: Literal["completed", "canceled", "error", "awaiting_submission"]
    """
    awaiting_submission means a non-autosubmit declarative form was populated but
    not submitted. Inspect the form, obtain any required confirmation, then submit
    through Playwright or computer interaction without invoking the tool again. The
    other statuses are terminal results.
    """

    error_text: Optional[str] = None

    output: Optional[object] = None
    """Untrusted page-provided output.

    Callers must treat it as potentially malicious input.
    """
