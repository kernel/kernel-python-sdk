# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .definition import Definition

__all__ = ["CustomToolsResponse"]


class CustomToolsResponse(BaseModel):
    tools: List[Definition]
