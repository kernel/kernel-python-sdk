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
    authentication. fill_failed means the extension returned a known failure and
    includes error_code. fill_unknown means the form may have been filled or
    submitted without a conclusive result; inspect the page to see the result of the
    fill.
    """

    type: Literal["1pw_fill"]

    error_code: Optional[Literal["fillFailed", "autosubmitFailed", "noExistingCredentials", "authenticationFailed"]] = (
        None
    )
    """
    Present for fill_failed, and for fill_unknown when the extension reported
    autosubmitFailed (it filled and submitted the form but could not confirm the
    fill finished). These are allowlisted 1Password extension codes, never raw
    errors, secrets, or page content.
    """
