# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .tab import Tab
from ..._models import BaseModel

__all__ = ["PlaywrightExecuteResponse"]


class PlaywrightExecuteResponse(BaseModel):
    """Result of Playwright code execution"""

    success: bool
    """Whether the code executed successfully"""

    error: Optional[str] = None
    """Error message if execution failed"""

    result: Optional[object] = None
    """The value returned by the code (if any)"""

    stderr: Optional[str] = None
    """Standard error from the execution"""

    stdout: Optional[str] = None
    """Standard output from the execution"""

    tab: Optional[Tab] = None
    """The tab 'page' was bound to for this call.

    Absent if the call failed before binding a tab.
    """
