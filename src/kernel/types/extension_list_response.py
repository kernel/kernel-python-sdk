# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ExtensionListResponse", "ExtensionListResponseItem"]


class ExtensionListResponseItem(BaseModel):
    """A browser extension uploaded to Kernel."""

    id: str
    """Unique identifier for the extension"""

    created_at: datetime
    """Timestamp when the extension was created"""

    size_bytes: int
    """Size of the extension archive in bytes"""

    last_used_at: Optional[datetime] = None
    """Timestamp when the extension was last used"""

    name: Optional[str] = None
    """Optional, easier-to-reference name for the extension.

    Must be unique within the project.
    """


ExtensionListResponse: TypeAlias = List[ExtensionListResponseItem]
