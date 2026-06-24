# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AuditLogEntry"]


class AuditLogEntry(BaseModel):
    auth_strategy: str
    """Authentication strategy used for the request."""

    client_ip: str
    """Client IP address."""

    domain: str
    """Request host."""

    duration_ms: int
    """Request duration in milliseconds."""

    email: str
    """Email of the authenticated user at request time, if any."""

    method: str
    """HTTP method."""

    path: str
    """Request path."""

    route: str
    """Matched API route pattern, if available."""

    status: int
    """HTTP response status code."""

    timestamp: datetime
    """UTC time when the request was received."""

    user_agent: str
    """User agent header."""

    user_id: str
    """ID of the authenticated user, if any."""
