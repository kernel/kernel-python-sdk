# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .tool_frame import ToolFrame
from .custom_tool_source import CustomToolSource

__all__ = ["ToolSource"]


class ToolSource(BaseModel):
    frame: Optional[ToolFrame] = None
    """
    Embedded frame that registered the tool, or null when the top-level page
    registered it.
    """

    page_title: str
    """Current title of the top-level page."""

    page_url: str
    """Current URL of the top-level page with the fragment omitted."""

    tab_id: int
    """
    Monotonically increasing identifier for the tab during the current browser
    process.
    """

    window_id: int
    """
    Monotonically increasing identifier for the browser window during the current
    browser process.
    """

    custom: Optional[CustomToolSource] = None

    target_id: Optional[str] = None
    """
    CDP target ID for a custom tool's registration tab; omitted for page-provided
    tools.
    """
