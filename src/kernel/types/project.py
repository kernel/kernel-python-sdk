# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: str
    """Unique project identifier"""

    created_at: datetime
    """When the project was created"""

    name: str
    """Project name"""

    status: Literal["active", "archived"]
    """Project status"""

    updated_at: datetime
    """When the project was last updated"""
