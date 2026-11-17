# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ReportTypeVersionSummary"]


class ReportTypeVersionSummary(BaseModel):
    """One schema version of a report type, without its schema."""

    retired: bool
    """Whether the version is retired.

    Retired versions are no longer accepted for new reports; existing reports keep
    them.
    """

    version: int
    """Schema version number, starting at 1."""
