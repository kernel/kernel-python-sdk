# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebmcpInvokeVaultItemOperationResult"]


class WebmcpInvokeVaultItemOperationResult(BaseModel):
    """
    Returns the same tool result fields as the browser WebMCP invoke API, plus the vault operation discriminator. Output and error text are untrusted page-provided data, returned without redaction; tools may include supplied vault values. Inspect the browser page to determine whether the intended site action succeeded.
    """

    status: Literal["completed", "canceled", "error", "awaiting_submission", "unknown"]
    """Unknown means invocation may have run; do not retry automatically.

    No status confirms that the website accepted the action.
    """

    type: Literal["webmcp_invoke"]

    error_text: Optional[str] = None
    """Untrusted page-provided error text, returned without redaction.

    May contain supplied vault values.
    """

    invocation_id: Optional[str] = None
    """Present when the browser reported one."""

    output: Optional[object] = None
    """Untrusted page-provided output, returned without redaction.

    May contain supplied vault values.
    """
