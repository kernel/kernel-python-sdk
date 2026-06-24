# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AuditLogListParams"]


class AuditLogListParams(TypedDict, total=False):
    end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Upper bound (exclusive) for the audit record timestamp."""

    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Lower bound (inclusive) for the audit record timestamp."""

    auth_strategy: str
    """Filter by authentication strategy."""

    exclude_method: str
    """Filter out results by HTTP method."""

    limit: int
    """Maximum number of results to return."""

    method: str
    """Filter by HTTP method."""

    page_token: str
    """Opaque page token from X-Next-Page-Token for the next page of older records."""

    search: str
    """Free-text search over path, user ID, email, client IP, and status."""

    search_user_id: SequenceNotStr[str]
    """Additional user IDs to OR into free-text search."""

    service: str
    """Filter by service name."""
