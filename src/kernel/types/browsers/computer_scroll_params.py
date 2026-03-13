# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ComputerScrollParams"]


class ComputerScrollParams(TypedDict, total=False):
    x: Required[int]
    """X coordinate at which to perform the scroll"""

    y: Required[int]
    """Y coordinate at which to perform the scroll"""

    delta_x: int
    """
    Horizontal scroll amount in xdotool "wheel units." Positive scrolls right,
    negative scrolls left.
    """

    delta_y: int
    """
    Vertical scroll amount in xdotool "wheel units." Positive scrolls down, negative
    scrolls up.
    """

    hold_keys: SequenceNotStr[str]
    """Modifier keys to hold during the scroll"""
