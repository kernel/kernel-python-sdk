# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ReportTypeSummary"]


class ReportTypeSummary(BaseModel):
    """A kind of report agents can submit against a task.

    Retrieve the type for the JSON Schema of its data.
    """

    description: str
    """What the report type records and when to submit it"""

    latest_version: int
    """Highest version that is not retired.

    A report submitted without a schema_version uses this version. It is 0 when
    every version is retired.
    """

    type: str
    """Report type name, such as task.result"""
