# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .task_metadata_param import TaskMetadataParam

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    description: Required[str]
    """What the task is meant to accomplish, at most 4 KB."""

    metadata: TaskMetadataParam
    """
    Caller-defined string key-value pairs for grouping and filtering tasks, such as
    a user or thread ID. At most 20 keys; keys are 1-64 characters, values at most
    256 characters, and keys and values together at most 4 KB.
    """

    session_ids: SequenceNotStr[str]
    """IDs of browsers to link to the task.

    Each must belong to the request's project; deleted browsers can be linked.
    """

    started_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When work on the task started.

    Defaults to the time the task is created. Must be no more than 5 minutes in the
    future or 30 days in the past.
    """

    target_website: str
    """Hostname of the website the task targets, without a scheme or path."""
