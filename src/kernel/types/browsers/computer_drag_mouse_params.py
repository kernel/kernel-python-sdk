# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ComputerDragMouseParams"]


class ComputerDragMouseParams(TypedDict, total=False):
    path: Required[Iterable[Iterable[int]]]
    """Ordered list of [x, y] coordinate pairs to move through while dragging.

    Must contain at least 2 points.
    """

    button: Literal["left", "middle", "right"]
    """Mouse button to drag with"""

    delay: int
    """Delay in milliseconds between button down and starting to move along the path."""

    duration_ms: int
    """
    Target total duration in milliseconds for the entire drag movement when
    smooth=true. Omit for automatic timing based on total path length.
    """

    hold_keys: SequenceNotStr[str]
    """Modifier keys to hold during the drag"""

    smooth: bool
    """
    Use human-like Bezier curves between path waypoints instead of linear
    interpolation. When true, steps_per_segment and step_delay_ms are ignored.
    """

    step_delay_ms: int
    """
    Delay in milliseconds between relative steps while dragging (not the initial
    delay).
    """

    steps_per_segment: int
    """Number of relative move steps per segment in the path. Minimum 1."""
