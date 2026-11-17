# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TaskLinkBrowsersParams"]


class TaskLinkBrowsersParams(TypedDict, total=False):
    session_ids: Required[SequenceNotStr[str]]
    """IDs of browsers to link.

    Each must belong to the task's project; deleted browsers can be linked. Browsers
    already linked are ignored. A task can have at most 100 linked browsers.
    """
