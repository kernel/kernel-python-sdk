# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["AppAction"]


class AppAction(BaseModel):
    """An action available on the app"""

    name: str
    """Name of the action"""

    input_schema: Optional[Dict[str, object]] = None
    """JSON Schema (draft-07) describing the expected input payload.

    Null if schema could not be automatically generated.
    """

    output_schema: Optional[Dict[str, object]] = None
    """JSON Schema (draft-07) describing the expected output payload.

    Null if schema could not be automatically generated.
    """
