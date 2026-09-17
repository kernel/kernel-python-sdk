from __future__ import annotations

import math
import time
import random
from datetime import datetime

from .._types import Omit, Headers
from .._exceptions import KernelError
from ..types.config_registry_response import ConfigRegistryResponse

DEFAULT_CONFIG_REGISTRY_POLL_INTERVAL = 5.0
_TERMINAL_STATUSES = frozenset({"completed", "failed", "canceled", "expired"})


def validate_wait_options(poll_interval: float, max_wait_seconds: float | None) -> None:
    if not math.isfinite(poll_interval) or poll_interval <= 0:
        raise ValueError("Expected a finite, positive value for `poll_interval`")
    if max_wait_seconds is not None and (not math.isfinite(max_wait_seconds) or max_wait_seconds < 0):
        raise ValueError("Expected a finite, non-negative value for `max_wait_seconds`")


def poll_headers(extra_headers: Headers | None) -> Headers:
    headers: dict[str, str | Omit] = dict(extra_headers or {})
    headers["X-Stainless-Poll-Helper"] = "true"
    return headers


def poll_delay(poll_interval: float) -> float:
    return poll_interval * random.uniform(0.9, 1.1)


def wait_timeout_error(id: str, polls: int, last_status: str | None, started_at: float) -> TimeoutError:
    elapsed = time.monotonic() - started_at
    return TimeoutError(
        f"Timed out waiting for config registry analysis {id!r} after {elapsed:.1f}s "
        f"and {polls} polls; last status was {last_status!r}"
    )


def analysis_finished(response: ConfigRegistryResponse, requested_id: str) -> tuple[bool, str]:
    analysis = response.analysis
    if analysis is None:
        raise KernelError(f"Config registry response for {requested_id!r} is missing an analysis")

    analysis_id = getattr(analysis, "id", None)
    if not isinstance(analysis_id, str) or not analysis_id:
        raise KernelError(f"Config registry response for {requested_id!r} has no valid analysis ID")
    if analysis_id != requested_id:
        raise KernelError(f"Config registry response for {requested_id!r} returned analysis {analysis_id!r}")

    status = getattr(analysis, "status", None)
    if not isinstance(status, str) or not status:
        raise KernelError(f"Config registry analysis {requested_id!r} has no valid status")

    if "finished_at" not in analysis.model_fields_set:
        raise KernelError(f"Config registry analysis {requested_id!r} is missing `finished_at`")

    finished_at = getattr(analysis, "finished_at", None)
    if finished_at is not None and not isinstance(finished_at, datetime):
        raise KernelError(f"Config registry analysis {requested_id!r} has an invalid `finished_at`")

    return finished_at is not None or status in _TERMINAL_STATUSES, status
