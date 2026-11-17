# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    data: Required[Dict[str, object]]
    """Report data.

    It must match the schema of the report type's version and encode to at most 16
    KB of JSON.
    """

    task_id: Required[str]
    """ID of the task to report against."""

    type: Required[str]
    """Report type name.

    List report types to see the available types and their schemas.
    """

    occurred_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When the reported event happened.

    Defaults to the time the report is submitted. Must be no more than 5 minutes in
    the future or 30 days in the past.
    """

    schema_version: int
    """Version of the report type's schema to validate data against.

    Defaults to the type's latest version, which the response returns.
    """

    session_id: str
    """ID of the browser the report was observed in.

    It must belong to the task's project; deleted browsers are accepted. The browser
    is linked to the task if it is not already.
    """
