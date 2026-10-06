# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .executor import Executor
from ...._models import BaseModel

__all__ = ["ExecutorList"]


class ExecutorList(BaseModel):
    """The default executor followed by the named executors"""

    executors: List[Executor]
