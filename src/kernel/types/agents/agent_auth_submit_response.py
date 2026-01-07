# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AgentAuthSubmitResponse"]


class AgentAuthSubmitResponse(BaseModel):
    """
    Response from submit endpoint - returns immediately after submission is accepted
    """

    accepted: bool
    """Whether the submission was accepted for processing"""
