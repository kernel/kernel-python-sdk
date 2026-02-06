# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SubmitFieldsResponse"]


class SubmitFieldsResponse(BaseModel):
    """Response from submitting field values"""

    accepted: bool
    """Whether the submission was accepted for processing"""
