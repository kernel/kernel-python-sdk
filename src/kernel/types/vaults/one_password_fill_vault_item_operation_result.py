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
    authentication; check the page. fill_failed means 1Password reported a failure,
    named by error_code; with fillFailed the form may already have been filled or
    submitted, so check the page. fill_unknown means the form may have been filled
    or submitted without a conclusive result; inspect the page to see the result of
    the fill.
    """

    type: Literal["1pw_fill"]

    error_code: Optional[str] = None
    """The 1Password extension's error code, passed through unchanged.

    Present for fill_failed, and for fill_unknown when the extension reported one.
    Codes 1Password adds later are returned with fill_unknown, because the form may
    have been filled or submitted. Codes are short identifiers, never raw errors,
    secrets, or page content.

    autosubmitFailed (fill_unknown): 1Password filled the form, saw no new page and
    no removed fields for 10 seconds, and cleared what it filled. If the login has a
    one-time password the site didn't ask for, the sign-in may still have worked.
    The approval is still valid: do not request access again. Check the page:
    continue if signed in or on a verification step; if the form is still showing,
    1Password cannot sign in to this site, so ask the user or use another sign-in
    method rather than filling again.

    internal (fill_unknown): an unexpected 1Password error that may have happened
    after the fill. Inspect the page.

    noActiveGrant, credentialNotFound: the approval expired or was revoked, or the
    login was deleted or moved. Kernel returns the credential to
    pending_authorization and drops its approval; create a new access request with
    1pw_create_access_request.

    fillFailed: 1Password couldn't complete the fill, and the form may already have
    been filled or submitted. Check the page before filling again.

    websiteMismatch: the page isn't on the login's website. Navigate to the login
    page and fill again.

    rateLimitExceeded: wait at least a minute before filling again.
    serviceUnavailable and networkError: fill again with backoff.

    extensionUnavailable: the 1Password extension failed to start in this browser.
    Create a new browser with the vault attached and fill there.

    invalidToken: 1Password rejected the access token. For a credential linked to a
    1Password account, Kernel has already refreshed the token and filled once more;
    if that refresh failed, the account is now reconnect_required, so link it again
    with PUT. For a credential with a stored token, replace the token with
    1pw_update_access_token, then fill again.

    integrationKeyInvalid: the 1Password connection was removed or is out of date.
    Invoke 1pw_disconnect on the credential_account item, then link it again with
    PUT.

    insufficientScope, permissionDenied, featureEntitlementMissing: the 1Password
    account or plan doesn't allow this. Tell the user; filling again won't help.
    """
