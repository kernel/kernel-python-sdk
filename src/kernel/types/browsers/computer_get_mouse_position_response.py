# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ComputerGetMousePositionResponse"]


class ComputerGetMousePositionResponse(BaseModel):
    x: int
    """X coordinate of the cursor"""

    y: int
    """Y coordinate of the cursor"""
