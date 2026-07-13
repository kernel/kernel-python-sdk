# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AuditLogExportChunkParams"]


class AuditLogExportChunkParams(TypedDict, total=False):
    end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Upper bound (exclusive) for the audit record timestamp."""

    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Lower bound (inclusive) for the audit record timestamp."""

    auth_strategy: str
    """Filter by authentication strategy."""

    cursor: str
    """Opaque cursor from X-Next-Cursor for the next chunk of older records."""

    exclude_method: SequenceNotStr[str]
    """Filter out results by HTTP method."""

    format: Literal["jsonl", "jsonl.gz"]
    """Encoding for the returned chunk."""

    limit: int
    """Maximum number of records to return in this chunk."""

    method: str
    """Filter by HTTP method."""

    search: str
    """Free-text search over path, user ID, email, client IP, and status."""

    search_user_id: SequenceNotStr[str]
    """Additional user IDs to OR into free-text search."""

    service: str
    """Filter by service name."""
