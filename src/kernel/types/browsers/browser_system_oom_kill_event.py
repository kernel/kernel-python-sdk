# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = ["BrowserSystemOomKillEvent", "Data", "DataTopTask"]


class DataTopTask(BaseModel):
    name: str
    """Comm of the process (max 15 chars, truncated by the kernel)."""

    pid: int
    """PID of the process."""

    rss_kb: int
    """Resident set size in KiB at the moment of the kill."""


class Data(BaseModel):
    pid: int
    """PID of the killed process."""

    process_name: str
    """
    Comm of the killed process as reported by the kernel (max 15 chars, truncated by
    the kernel).
    """

    rss_kb: int
    """
    Resident set size of the killed process in KiB (sum of anon-rss, file-rss, and
    shmem-rss).
    """

    constraint: Optional[Literal["none", "memcg", "cpuset", "memory_policy"]] = None
    """Why the kernel decided to OOM-kill.

    none means global memory exhaustion; memcg means a cgroup memory limit was hit;
    cpuset / memory_policy are NUMA/policy-driven kills. Absent on kernels older
    than 5.0.
    """

    mem_free_kb: Optional[int] = None
    """Free system memory in KiB at the time of the kill.

    Assumes a 4 KiB page size. Does not include reclaimable caches. Absent if the
    kernel did not emit a parseable Mem-Info section.
    """

    mem_total_kb: Optional[int] = None
    """Total system memory in KiB at the time of the kill.

    Assumes a 4 KiB page size. Absent if the kernel did not emit a parseable
    Mem-Info section.
    """

    top_tasks: Optional[List[DataTopTask]] = None
    """Top processes by resident-set-size at the moment of the kill, sorted descending.

    Empty if the kernel did not emit the Tasks state table. Capped at 5 entries.
    """

    trigger_pid: Optional[int] = None
    """PID of the triggering process.

    Absent if the kernel did not emit the standard header line.
    """

    trigger_process_name: Optional[str] = None
    """
    Comm of the process whose allocation request caused the kernel to invoke the
    OOM-killer. Often the same as process_name but can differ. Max 15 chars.
    """


class BrowserSystemOomKillEvent(BaseModel):
    """The Linux kernel OOM-killer terminated a process inside the VM.

    Fires for any process killed by the kernel due to memory exhaustion, including Chrome renderer subprocesses that are not supervised.
    """

    category: Literal["system"]

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["system_oom_kill"]

    data: Optional[Data] = None

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
