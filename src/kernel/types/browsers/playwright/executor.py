# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Executor"]


class Executor(BaseModel):
    """A Playwright executor on the browser"""

    busy: bool
    """Whether a call is running on the executor"""

    created_at: datetime
    """When the executor was created"""

    last_used_at: datetime
    """When the most recent call on the executor started"""

    name: str
    """Name of a Playwright executor.

    Calls with the same name run in the same executor, one at a time; the first call
    with a new name creates it. Calls on different executors run concurrently.
    'default' names the executor that runs calls without a name.
    """

    target_id: Optional[str] = None
    """CDP page target ID of the executor's tab, once it has one.

    The default executor owns no tab.
    """

    url: Optional[str] = None
    """Current URL of the executor's tab, when it is open"""
