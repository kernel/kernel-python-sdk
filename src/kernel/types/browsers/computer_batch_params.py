# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ComputerBatchParams",
    "Action",
    "ActionClickMouse",
    "ActionDragMouse",
    "ActionMoveMouse",
    "ActionPressKey",
    "ActionScroll",
    "ActionSetCursor",
    "ActionSleep",
    "ActionTypeText",
]


class ComputerBatchParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]
    """Ordered list of actions to execute. Execution stops on the first error."""


class ActionClickMouse(TypedDict, total=False):
    x: Required[int]
    """X coordinate of the click position"""

    y: Required[int]
    """Y coordinate of the click position"""

    button: Literal["left", "right", "middle", "back", "forward"]
    """Mouse button to interact with"""

    click_type: Literal["down", "up", "click"]
    """Type of click action"""

    hold_keys: SequenceNotStr[str]
    """Modifier keys to hold during the click"""

    num_clicks: int
    """Number of times to repeat the click"""


class ActionDragMouse(TypedDict, total=False):
    path: Required[Iterable[Iterable[int]]]
    """Ordered list of [x, y] coordinate pairs to move through while dragging.

    Must contain at least 2 points.
    """

    button: Literal["left", "middle", "right"]
    """Mouse button to drag with"""

    delay: int
    """Delay in milliseconds between button down and starting to move along the path."""

    hold_keys: SequenceNotStr[str]
    """Modifier keys to hold during the drag"""

    step_delay_ms: int
    """
    Delay in milliseconds between relative steps while dragging (not the initial
    delay).
    """

    steps_per_segment: int
    """Number of relative move steps per segment in the path. Minimum 1."""


class ActionMoveMouse(TypedDict, total=False):
    x: Required[int]
    """X coordinate to move the cursor to"""

    y: Required[int]
    """Y coordinate to move the cursor to"""

    hold_keys: SequenceNotStr[str]
    """Modifier keys to hold during the move"""


class ActionPressKey(TypedDict, total=False):
    keys: Required[SequenceNotStr[str]]
    """List of key symbols to press.

    Each item should be a key symbol supported by xdotool (see X11 keysym
    definitions). Examples include "Return", "Shift", "Ctrl", "Alt", "F5". Items in
    this list could also be combinations, e.g. "Ctrl+t" or "Ctrl+Shift+Tab".
    """

    duration: int
    """Duration to hold the keys down in milliseconds.

    If omitted or 0, keys are tapped.
    """

    hold_keys: SequenceNotStr[str]
    """Optional modifier keys to hold during the key press sequence."""


class ActionScroll(TypedDict, total=False):
    x: Required[int]
    """X coordinate at which to perform the scroll"""

    y: Required[int]
    """Y coordinate at which to perform the scroll"""

    delta_x: int
    """Horizontal scroll amount. Positive scrolls right, negative scrolls left."""

    delta_y: int
    """Vertical scroll amount. Positive scrolls down, negative scrolls up."""

    hold_keys: SequenceNotStr[str]
    """Modifier keys to hold during the scroll"""


class ActionSetCursor(TypedDict, total=False):
    hidden: Required[bool]
    """Whether the cursor should be hidden or visible"""


class ActionSleep(TypedDict, total=False):
    """Pause execution for a specified duration."""

    duration_ms: Required[int]
    """Duration to sleep in milliseconds."""


class ActionTypeText(TypedDict, total=False):
    text: Required[str]
    """Text to type on the browser instance"""

    delay: int
    """Delay in milliseconds between keystrokes"""


class Action(TypedDict, total=False):
    """A single computer action to execute as part of a batch.

    The `type` field selects which
    action to perform, and the corresponding field contains the action parameters.
    Exactly one action field matching the type must be provided.
    """

    type: Required[
        Literal["click_mouse", "move_mouse", "type_text", "press_key", "scroll", "drag_mouse", "set_cursor", "sleep"]
    ]
    """The type of action to perform."""

    click_mouse: ActionClickMouse

    drag_mouse: ActionDragMouse

    move_mouse: ActionMoveMouse

    press_key: ActionPressKey

    scroll: ActionScroll

    set_cursor: ActionSetCursor

    sleep: ActionSleep
    """Pause execution for a specified duration."""

    type_text: ActionTypeText
