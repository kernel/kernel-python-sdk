# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .report_type_version_summary import ReportTypeVersionSummary

__all__ = ["ReportType"]


class ReportType(BaseModel):
    """
    A kind of report agents can submit against a task, with its versions and the JSON Schema of its latest version. A shipped version never changes; changes ship as new versions.
    """

    description: str
    """What the report type records and when to submit it"""

    latest_version: int
    """Highest version that is not retired.

    A report submitted without a schema_version uses this version. It is 0 when
    every version is retired.
    """

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """
    JSON Schema (draft 2020-12) of the latest version, which a report's data must
    match. Its field descriptions and examples describe what to send. Null when
    every version is retired.
    """

    type: str
    """Report type name, such as task.result"""

    versions: List[ReportTypeVersionSummary]
    """Every version of the type, oldest first, including retired versions."""
