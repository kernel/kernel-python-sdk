from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import override

from ..._exceptions import KernelError

__all__ = ["WorkloadIdentityError"]


class WorkloadIdentityError(KernelError):
    """Raised when workload identity federation is misconfigured or the token exchange fails.

    For a response from the token endpoint, `status_code` is the HTTP status and
    `error` / `error_description` are the OAuth error fields. `body` holds only
    the OAuth error fields of the response, never the rest of it.
    """

    status_code: Optional[int]
    error: Optional[str]
    error_description: Optional[str]
    request_id: Optional[str]
    body: Optional[Dict[str, str]]

    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        error: Optional[str] = None,
        error_description: Optional[str] = None,
        request_id: Optional[str] = None,
        body: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error = error
        self.error_description = error_description
        self.request_id = request_id
        self.body = body

    @override
    def __str__(self) -> str:
        message = super().__str__()
        if self.request_id:
            return f"{message} [request_id={self.request_id}]"
        return message
