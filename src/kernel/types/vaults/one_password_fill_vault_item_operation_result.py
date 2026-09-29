# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnePasswordFillVaultItemOperationResult"]


class OnePasswordFillVaultItemOperationResult(BaseModel):
    """The submission result reported by the 1Password extension when available.

    Kernel returns fill_unknown if the extension call has no conclusive result. Inspect the page to determine successful authentication on the website.
    """

    status: Literal["fill_submitted", "fill_failed", "fill_unknown"]
    """Kernel's outcome of the extension call.

    fill_submitted means the extension reported submission, not website
    authentication. fill_failed means the extension returned a known failure and may
    include error_code. fill_unknown means submission may have happened without a
    conclusive response; it has no error_code and must not be retried in the same
    browser.
    """

    type: Literal["1pw_fill"]

    error_code: Optional[Literal["fillFailed", "autosubmitFailed", "noExistingCredentials", "authenticationFailed"]] = (
        None
    )
    """Present only for a conclusive fill_failed response.

    These are allowlisted 1Password extension codes, never raw errors, secrets, or
    page content.
    """
