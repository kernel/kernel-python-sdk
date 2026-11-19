# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Report"]


class Report(BaseModel):
    """A typed, schema-validated report an agent submitted against a task.

    Reports are immutable.
    """

    id: str
    """Unique identifier for the report"""

    created_at: datetime
    """When the report was submitted"""

    data: Dict[str, object]
    """Report data, matching the report type's schema"""

    occurred_at: datetime
    """When the reported event happened"""

    schema_version: int
    """Version of the report type's schema that data was validated against"""

    task_id: str
    """ID of the task the report belongs to"""

    type: str
    """Report type name"""

    session_id: Optional[str] = None
    """ID of the browser the report was observed in, if any"""
