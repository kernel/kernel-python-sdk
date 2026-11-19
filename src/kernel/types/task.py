# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .task_metadata import TaskMetadata

__all__ = ["Task"]


class Task(BaseModel):
    """A goal an agent works toward.

    Reports are submitted against a task, and browsers can be linked to it. Tasks are immutable apart from added browser links.
    """

    id: str
    """Unique identifier for the task"""

    created_at: datetime
    """When the task was created"""

    description: str
    """What the task is meant to accomplish"""

    metadata: TaskMetadata
    """
    Caller-defined string key-value pairs for grouping and filtering tasks, such as
    a user or thread ID. At most 20 keys; keys are 1-64 characters, values at most
    256 characters, and keys and values together at most 4 KB.
    """

    session_ids: List[str]
    """IDs of browsers linked to the task, oldest link first.

    Linked browsers may since have been deleted.
    """

    started_at: datetime
    """When work on the task started"""

    target_website: Optional[str] = None
    """Hostname of the website the task targets"""
