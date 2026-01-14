# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ProcessSpawnParams"]


class ProcessSpawnParams(TypedDict, total=False):
    command: Required[str]
    """Executable or shell command to run."""

    allocate_tty: bool
    """Allocate a pseudo-terminal (PTY) for interactive shells."""

    args: SequenceNotStr[str]
    """Command arguments."""

    as_root: bool
    """Run the process with root privileges."""

    as_user: Optional[str]
    """Run the process as this user."""

    cols: int
    """Initial terminal columns. Only used when allocate_tty is true."""

    cwd: Optional[str]
    """Working directory (absolute path) to run the command in."""

    env: Dict[str, str]
    """Environment variables to set for the process."""

    rows: int
    """Initial terminal rows. Only used when allocate_tty is true."""

    timeout_sec: Optional[int]
    """Maximum execution time in seconds."""
