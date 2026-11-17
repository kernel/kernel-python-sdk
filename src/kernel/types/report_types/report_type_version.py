# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ReportTypeVersion"]


class ReportTypeVersion(BaseModel):
    """One immutable schema version of a report type."""

    retired: bool
    """Whether the version is retired.

    Retired versions are no longer accepted for new reports; existing reports keep
    them.
    """

    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """JSON Schema (draft 2020-12) that a report's data must match.

    Its field descriptions and examples describe what to send.
    """

    type: str
    """Report type name, such as task.result"""

    version: int
    """Schema version number, starting at 1."""
