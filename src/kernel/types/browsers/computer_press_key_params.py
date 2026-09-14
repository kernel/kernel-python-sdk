# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ComputerPressKeyParams"]


class ComputerPressKeyParams(TypedDict, total=False):
    keys: Required[SequenceNotStr[str]]
    """List of key symbols to press.

    Each item should be a key symbol supported by xdotool (see X11 keysym
    definitions). Examples include "Return", "Shift", "Ctrl", "Alt", "F5". Items in
    this list could also be combinations, e.g. "Ctrl+t" or "Ctrl+Shift+Tab". Use X11
    names for punctuation in combinations, such as "Ctrl+minus" or "Ctrl+plus". A
    literal hyphen is also accepted as an alias, so "Ctrl+-" is normalized to
    "Ctrl+minus".
    """

    duration: int
    """Duration to hold the keys down in milliseconds.

    If omitted or 0, keys are tapped.
    """

    hold_keys: SequenceNotStr[str]
    """Optional modifier keys to hold during the key press sequence."""
