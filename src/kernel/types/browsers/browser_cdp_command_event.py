# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .browser_event_source import BrowserEventSource

__all__ = [
    "BrowserCdpCommandEvent",
    "Data",
    "DataBrowserCdpInputDispatchMouseEventCommandData",
    "DataBrowserCdpInputDispatchKeyEventCommandData",
    "DataBrowserCdpInputInsertTextCommandData",
    "DataBrowserCdpInputImeSetCompositionCommandData",
    "DataBrowserCdpInputDispatchTouchEventCommandData",
    "DataBrowserCdpInputDispatchDragEventCommandData",
    "DataBrowserCdpInputCancelDraggingCommandData",
    "DataBrowserCdpInputEmulateTouchFromMouseEventCommandData",
    "DataBrowserCdpInputSynthesizePinchGestureCommandData",
    "DataBrowserCdpInputSynthesizeScrollGestureCommandData",
    "DataBrowserCdpInputSynthesizeTapGestureCommandData",
    "DataBrowserCdpDomSetFileInputFilesCommandData",
    "DataBrowserCdpDomFocusCommandData",
    "DataBrowserCdpDomScrollIntoViewIfNeededCommandData",
    "DataBrowserCdpPageBringToFrontCommandData",
    "DataBrowserCdpPageCaptureScreenshotCommandData",
    "DataBrowserCdpPageCaptureSnapshotCommandData",
    "DataBrowserCdpPageHandleJavaScriptDialogCommandData",
    "DataBrowserCdpPageNavigateCommandData",
    "DataBrowserCdpPageNavigateToHistoryEntryCommandData",
    "DataBrowserCdpPageReloadCommandData",
    "DataBrowserCdpPagePrintToPdfCommandData",
    "DataBrowserCdpPageStartScreencastCommandData",
    "DataBrowserCdpPageStopScreencastCommandData",
    "DataBrowserCdpPageStopLoadingCommandData",
    "DataBrowserCdpPageCloseCommandData",
    "DataBrowserCdpPageSetWebLifecycleStateCommandData",
    "DataBrowserCdpTargetActivateTargetCommandData",
    "DataBrowserCdpTargetCloseTargetCommandData",
    "DataBrowserCdpTargetCreateTargetCommandData",
    "DataBrowserCdpTargetCreateBrowserContextCommandData",
    "DataBrowserCdpTargetDisposeBrowserContextCommandData",
    "DataBrowserCdpTargetOpenDevToolsCommandData",
    "DataBrowserCdpBrowserCancelDownloadCommandData",
    "DataBrowserCdpBrowserCloseCommandData",
    "DataBrowserCdpBrowserSetWindowBoundsCommandData",
    "DataBrowserCdpBrowserSetContentsSizeCommandData",
    "DataBrowserCdpAutofillTriggerCommandData",
]


class DataBrowserCdpInputDispatchMouseEventCommandData(BaseModel):
    """Sanitized `Input.dispatchMouseEvent` arguments.

    Canonical input: `Input.dispatchMouseEvent` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    event_type: Literal["mousePressed", "mouseReleased", "mouseMoved", "mouseWheel", "other"]
    """Mouse event phase: `mousePressed`, `mouseReleased`, `mouseMoved` or
    `mouseWheel`.

    A value the protocol does not define is reported as `other`.
    """

    method: Literal["Input.dispatchMouseEvent"]

    button: Optional[Literal["none", "left", "middle", "right", "back", "forward", "other"]] = None
    """
    Button named by the command (`none`, `left`, `middle`, `right`, `back`,
    `forward`). A value the protocol does not define is reported as `other`.
    """

    buttons: Optional[int] = None
    """Bit field of buttons held down.

    Non-zero on a `mouseMoved` means the move is a drag path.
    """

    click_count: Optional[int] = None
    """Number of times the button was clicked (2 is a double click)."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    delta_x: Optional[float] = None
    """Horizontal scroll delta, for `mouseWheel`."""

    delta_y: Optional[float] = None
    """Vertical scroll delta, for `mouseWheel`."""

    force: Optional[float] = None
    """Normalized pressure, 0 to 1."""

    modifiers: Optional[int] = None
    """Bit field of held modifier keys (1=Alt, 2=Ctrl, 4=Meta, 8=Shift)."""

    pointer_type: Optional[Literal["mouse", "pen", "other"]] = None
    """Pointer that generated the event (`mouse` or `pen`).

    A value the protocol does not define is reported as `other`.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    tangential_pressure: Optional[float] = None
    """Normalized tangential pressure, -1 to 1."""

    tilt_x: Optional[float] = None
    """Pen tilt from the Y-Z plane, in degrees."""

    tilt_y: Optional[float] = None
    """Pen tilt from the X-Z plane, in degrees."""

    twist: Optional[int] = None
    """Pen clockwise rotation, in degrees."""

    x: Optional[float] = None
    """Viewport x coordinate in CSS pixels."""

    y: Optional[float] = None
    """Viewport y coordinate in CSS pixels."""


class DataBrowserCdpInputDispatchKeyEventCommandData(BaseModel):
    """Sanitized `Input.dispatchKeyEvent` arguments.

    Canonical input: `Input.dispatchKeyEvent` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    event_type: Literal["keyDown", "keyUp", "rawKeyDown", "char", "other"]
    """Key event phase: `keyDown`, `keyUp`, `rawKeyDown` or `char`.

    A value the protocol does not define is reported as `other`.
    """

    method: Literal["Input.dispatchKeyEvent"]

    auto_repeat: Optional[bool] = None
    """Whether the event was generated by key repeat."""

    command_count: Optional[int] = None
    """Number of editing commands (e.g. `selectAll`) carried by the event."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    is_keypad: Optional[bool] = None
    """Whether the key is on the numeric keypad."""

    is_system_key: Optional[bool] = None
    """Whether the event is a system key event."""

    location: Optional[int] = None
    """Keyboard location (1=left, 2=right, 3=numpad)."""

    modifiers: Optional[int] = None
    """Bit field of held modifier keys (1=Alt, 2=Ctrl, 4=Meta, 8=Shift)."""

    named_key: Optional[str] = None
    """Key that commands the page rather than typing into it (e.g.

    `Enter`, `Tab`, `ArrowDown`, `F5`). Keys that produce a character are never
    captured; those are counted by `text_length`.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    text_length: Optional[int] = None
    """Number of characters the command submitted. The text itself is never captured."""


class DataBrowserCdpInputInsertTextCommandData(BaseModel):
    """Sanitized `Input.insertText` arguments.

    Canonical input: `Input.insertText` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Input.insertText"]

    text_length: int
    """Number of characters inserted. The text itself is never captured."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpInputImeSetCompositionCommandData(BaseModel):
    """Sanitized `Input.imeSetComposition` arguments.

    Canonical input: `Input.imeSetComposition` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Input.imeSetComposition"]

    text_length: int
    """Number of characters in the composition. The text itself is never captured."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    replacement_end: Optional[int] = None
    """Replacement range end offset."""

    replacement_start: Optional[int] = None
    """Replacement range start offset."""

    selection_end: Optional[int] = None
    """Selection end offset within the composition."""

    selection_start: Optional[int] = None
    """Selection start offset within the composition."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpInputDispatchTouchEventCommandData(BaseModel):
    """Sanitized `Input.dispatchTouchEvent` arguments.

    Canonical input: `Input.dispatchTouchEvent` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    event_type: Literal["touchStart", "touchEnd", "touchMove", "touchCancel", "other"]
    """Touch event phase: `touchStart`, `touchEnd`, `touchMove` or `touchCancel`.

    A value the protocol does not define is reported as `other`.
    """

    method: Literal["Input.dispatchTouchEvent"]

    touch_point_count: int
    """Number of active touch points the command carried."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    force: Optional[float] = None
    """Normalized pressure of the first touch point, 0 to 1."""

    modifiers: Optional[int] = None
    """Bit field of held modifier keys (1=Alt, 2=Ctrl, 4=Meta, 8=Shift)."""

    radius_x: Optional[float] = None
    """Horizontal radius of the first touch point."""

    radius_y: Optional[float] = None
    """Vertical radius of the first touch point."""

    rotation_angle: Optional[float] = None
    """Rotation of the first touch point, in degrees."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    tangential_pressure: Optional[float] = None
    """Normalized tangential pressure of the first touch point, -1 to 1."""

    tilt_x: Optional[float] = None
    """Tilt of the first touch point from the Y-Z plane, in degrees."""

    tilt_y: Optional[float] = None
    """Tilt of the first touch point from the X-Z plane, in degrees."""

    twist: Optional[int] = None
    """Clockwise rotation of the first touch point, in degrees."""

    x: Optional[float] = None
    """Viewport x coordinate of the first touch point.

    Touch coordinates live inside `touchPoints`, so this is the primary point rather
    than a command-level argument.
    """

    y: Optional[float] = None
    """Viewport y coordinate of the first touch point."""


class DataBrowserCdpInputDispatchDragEventCommandData(BaseModel):
    """Sanitized `Input.dispatchDragEvent` arguments.

    Canonical input: `Input.dispatchDragEvent` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    event_type: Literal["dragEnter", "dragOver", "drop", "dragCancel", "other"]
    """Drag event phase: `dragEnter`, `dragOver`, `drop` or `dragCancel`.

    A value the protocol does not define is reported as `other`.
    """

    method: Literal["Input.dispatchDragEvent"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    drag_file_count: Optional[int] = None
    """Number of files in the drag payload. File paths are never captured."""

    drag_item_count: Optional[int] = None
    """Number of items in the drag payload. Item contents are never captured."""

    drag_mime_categories: Optional[
        List[
            Literal["text", "image", "audio", "video", "application", "font", "model", "multipart", "message", "other"]
        ]
    ] = None
    """Distinct top-level MIME categories of the drag items (e.g.

    `text`, `image`, `application`). Subtypes and contents are never captured. A
    value the protocol does not define is reported as `other`.
    """

    drag_operations_mask: Optional[int] = None
    """Bit field of allowed drag operations (1=copy, 2=link, 16=move)."""

    modifiers: Optional[int] = None
    """Bit field of held modifier keys (1=Alt, 2=Ctrl, 4=Meta, 8=Shift)."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    x: Optional[float] = None
    """Viewport x coordinate in CSS pixels."""

    y: Optional[float] = None
    """Viewport y coordinate in CSS pixels."""


class DataBrowserCdpInputCancelDraggingCommandData(BaseModel):
    """Sanitized `Input.cancelDragging` arguments.

    Canonical input: `Input.cancelDragging` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Input.cancelDragging"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpInputEmulateTouchFromMouseEventCommandData(BaseModel):
    """Sanitized `Input.emulateTouchFromMouseEvent` arguments.

    Canonical input: `Input.emulateTouchFromMouseEvent` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    event_type: Literal["mousePressed", "mouseReleased", "mouseMoved", "mouseWheel", "other"]
    """Mouse event phase being emulated as touch.

    A value the protocol does not define is reported as `other`.
    """

    method: Literal["Input.emulateTouchFromMouseEvent"]

    button: Optional[Literal["none", "left", "middle", "right", "back", "forward", "other"]] = None
    """Button named by the command.

    A value the protocol does not define is reported as `other`.
    """

    click_count: Optional[int] = None
    """Number of times the button was clicked."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    delta_x: Optional[float] = None
    """Horizontal scroll delta."""

    delta_y: Optional[float] = None
    """Vertical scroll delta."""

    modifiers: Optional[int] = None
    """Bit field of held modifier keys (1=Alt, 2=Ctrl, 4=Meta, 8=Shift)."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    x: Optional[float] = None
    """Viewport x coordinate in CSS pixels."""

    y: Optional[float] = None
    """Viewport y coordinate in CSS pixels."""


class DataBrowserCdpInputSynthesizePinchGestureCommandData(BaseModel):
    """Sanitized `Input.synthesizePinchGesture` arguments.

    Canonical input: `Input.synthesizePinchGesture` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Input.synthesizePinchGesture"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    gesture_source_type: Optional[Literal["default", "touch", "mouse", "other"]] = None
    """Input source the synthesized gesture emulates.

    A value the protocol does not define is reported as `other`.
    """

    relative_speed: Optional[int] = None
    """Relative pointer speed, in pixels per second."""

    scale_factor: Optional[float] = None
    """Relative scale of the pinch (>1 zooms in)."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    x: Optional[float] = None
    """Viewport x coordinate in CSS pixels."""

    y: Optional[float] = None
    """Viewport y coordinate in CSS pixels."""


class DataBrowserCdpInputSynthesizeScrollGestureCommandData(BaseModel):
    """Sanitized `Input.synthesizeScrollGesture` arguments.

    Canonical input: `Input.synthesizeScrollGesture` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Input.synthesizeScrollGesture"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    gesture_source_type: Optional[Literal["default", "touch", "mouse", "other"]] = None
    """Input source the synthesized gesture emulates.

    A value the protocol does not define is reported as `other`.
    """

    prevent_fling: Optional[bool] = None
    """Whether fling was suppressed."""

    repeat_count: Optional[int] = None
    """Number of additional repeats of the scroll."""

    repeat_delay_ms: Optional[int] = None
    """Delay between repeats, in milliseconds."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    speed: Optional[int] = None
    """Swipe speed in pixels per second."""

    x: Optional[float] = None
    """Viewport x coordinate in CSS pixels."""

    x_distance: Optional[float] = None
    """Horizontal scroll distance in CSS pixels; positive scrolls left."""

    x_overscroll: Optional[float] = None
    """Additional horizontal distance scrolled past the end."""

    y: Optional[float] = None
    """Viewport y coordinate in CSS pixels."""

    y_distance: Optional[float] = None
    """Vertical scroll distance in CSS pixels; positive scrolls up."""

    y_overscroll: Optional[float] = None
    """Additional vertical distance scrolled past the end."""


class DataBrowserCdpInputSynthesizeTapGestureCommandData(BaseModel):
    """Sanitized `Input.synthesizeTapGesture` arguments.

    Canonical input: `Input.synthesizeTapGesture` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Input.synthesizeTapGesture"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    duration: Optional[int] = None
    """Duration between touchdown and touchup, in milliseconds."""

    gesture_source_type: Optional[Literal["default", "touch", "mouse", "other"]] = None
    """Input source the synthesized gesture emulates.

    A value the protocol does not define is reported as `other`.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    tap_count: Optional[int] = None
    """Number of times to tap (2 is a double tap)."""

    x: Optional[float] = None
    """Viewport x coordinate in CSS pixels."""

    y: Optional[float] = None
    """Viewport y coordinate in CSS pixels."""


class DataBrowserCdpDomSetFileInputFilesCommandData(BaseModel):
    """Sanitized `DOM.setFileInputFiles` arguments.

    Canonical input: `DOM.setFileInputFiles` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    file_count: int
    """Number of files handed to the input. File paths are never captured."""

    method: Literal["DOM.setFileInputFiles"]

    backend_node_id: Optional[int] = None
    """Opaque backend DOM node identifier the command targeted."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    node_id: Optional[int] = None
    """Opaque DOM node identifier the command targeted."""

    object_id: Optional[str] = None
    """Opaque Runtime remote object identifier the command targeted.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpDomFocusCommandData(BaseModel):
    """Sanitized `DOM.focus` arguments.

    Canonical input: `DOM.focus` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["DOM.focus"]

    backend_node_id: Optional[int] = None
    """Opaque backend DOM node identifier the command targeted."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    node_id: Optional[int] = None
    """Opaque DOM node identifier the command targeted."""

    object_id: Optional[str] = None
    """Opaque Runtime remote object identifier the command targeted.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpDomScrollIntoViewIfNeededCommandData(BaseModel):
    """Sanitized `DOM.scrollIntoViewIfNeeded` arguments.

    Canonical input: `DOM.scrollIntoViewIfNeeded` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["DOM.scrollIntoViewIfNeeded"]

    backend_node_id: Optional[int] = None
    """Opaque backend DOM node identifier the command targeted."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    node_id: Optional[int] = None
    """Opaque DOM node identifier the command targeted."""

    object_id: Optional[str] = None
    """Opaque Runtime remote object identifier the command targeted.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    rect_height: Optional[float] = None
    """Height of the rect the command scrolled to."""

    rect_width: Optional[float] = None
    """Width of the rect the command scrolled to."""

    rect_x: Optional[float] = None
    """X offset of the rect the command scrolled to, relative to the node."""

    rect_y: Optional[float] = None
    """Y offset of the rect the command scrolled to, relative to the node."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageBringToFrontCommandData(BaseModel):
    """Sanitized `Page.bringToFront` arguments.

    Canonical input: `Page.bringToFront` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.bringToFront"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageCaptureScreenshotCommandData(BaseModel):
    """Sanitized `Page.captureScreenshot` arguments.

    Canonical input: `Page.captureScreenshot` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.captureScreenshot"]

    capture_beyond_viewport: Optional[bool] = None
    """Whether the capture extended past the viewport."""

    clip_height: Optional[float] = None
    """Clip region height in CSS pixels."""

    clip_scale: Optional[float] = None
    """Clip region page scale factor."""

    clip_width: Optional[float] = None
    """Clip region width in CSS pixels."""

    clip_x: Optional[float] = None
    """Clip region x offset in CSS pixels."""

    clip_y: Optional[float] = None
    """Clip region y offset in CSS pixels."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    format: Optional[Literal["jpeg", "png", "webp", "other"]] = None
    """Image format requested (`jpeg`, `png` or `webp`).

    A value the protocol does not define is reported as `other`.
    """

    from_surface: Optional[bool] = None
    """Whether the capture was taken from the surface rather than the view."""

    optimize_for_speed: Optional[bool] = None
    """Whether encoding favored speed over size."""

    quality: Optional[int] = None
    """Compression quality, 0 to 100, for lossy formats."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageCaptureSnapshotCommandData(BaseModel):
    """Sanitized `Page.captureSnapshot` arguments.

    Canonical input: `Page.captureSnapshot` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.captureSnapshot"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    format: Optional[Literal["mhtml", "other"]] = None
    """Snapshot format requested (`mhtml`).

    A value the protocol does not define is reported as `other`.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageHandleJavaScriptDialogCommandData(BaseModel):
    """Sanitized `Page.handleJavaScriptDialog` arguments.

    Canonical input: `Page.handleJavaScriptDialog` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    accept: bool
    """Whether the dialog was accepted or dismissed."""

    method: Literal["Page.handleJavaScriptDialog"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    prompt_text_length: Optional[int] = None
    """Number of characters entered into a prompt dialog.

    The text itself is never captured.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageNavigateCommandData(BaseModel):
    """Sanitized `Page.navigate` arguments.

    Canonical input: `Page.navigate` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.navigate"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    frame_id: Optional[str] = None
    """Opaque frame identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    referrer_policy: Optional[
        Literal[
            "noReferrer",
            "noReferrerWhenDowngrade",
            "origin",
            "originWhenCrossOrigin",
            "sameOrigin",
            "strictOrigin",
            "strictOriginWhenCrossOrigin",
            "unsafeUrl",
            "other",
        ]
    ] = None
    """Referrer policy named by the command.

    A value the protocol does not define is reported as `other`.
    """

    referrer_present: Optional[bool] = None
    """Whether the command carried a referrer. The referrer itself is never captured."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    transition_type: Optional[
        Literal[
            "link",
            "typed",
            "address_bar",
            "auto_bookmark",
            "auto_subframe",
            "manual_subframe",
            "generated",
            "auto_toplevel",
            "form_submit",
            "reload",
            "keyword",
            "keyword_generated",
            "other",
        ]
    ] = None
    """Navigation reason reported by the caller (e.g.

    `link`, `typed`, `reload`). A value the protocol does not define is reported as
    `other`.
    """

    url_scheme: Optional[str] = None
    """Scheme of the destination URL (e.g.

    `https`, `about`, `data`). The rest of the URL is never captured.
    """


class DataBrowserCdpPageNavigateToHistoryEntryCommandData(BaseModel):
    """Sanitized `Page.navigateToHistoryEntry` arguments.

    Canonical input: `Page.navigateToHistoryEntry` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    entry_id: int
    """History entry the command navigated to."""

    method: Literal["Page.navigateToHistoryEntry"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageReloadCommandData(BaseModel):
    """Sanitized `Page.reload` arguments.

    Canonical input: `Page.reload` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.reload"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    ignore_cache: Optional[bool] = None
    """Whether the reload bypassed the cache."""

    loader_id: Optional[str] = None
    """Opaque document loader identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    script_length: Optional[int] = None
    """Number of characters in the injected script."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPagePrintToPdfCommandData(BaseModel):
    """Sanitized `Page.printToPDF` arguments.

    Canonical input: `Page.printToPDF` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.printToPDF"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    display_header_footer: Optional[bool] = None
    """Whether a header and footer were rendered."""

    footer_template_present: Optional[bool] = None
    """Whether a footer template was supplied. The template itself is never captured."""

    generate_document_outline: Optional[bool] = None
    """Whether a document outline was embedded."""

    generate_tagged_pdf: Optional[bool] = None
    """Whether a tagged (accessible) PDF was requested."""

    header_template_present: Optional[bool] = None
    """Whether a header template was supplied. The template itself is never captured."""

    landscape: Optional[bool] = None
    """Whether the page was laid out in landscape."""

    margin_bottom: Optional[float] = None
    """Bottom margin in inches."""

    margin_left: Optional[float] = None
    """Left margin in inches."""

    margin_right: Optional[float] = None
    """Right margin in inches."""

    margin_top: Optional[float] = None
    """Top margin in inches."""

    page_ranges_present: Optional[bool] = None
    """Whether a page range was supplied."""

    paper_height: Optional[float] = None
    """Paper height in inches."""

    paper_width: Optional[float] = None
    """Paper width in inches."""

    prefer_css_page_size: Optional[bool] = None
    """Whether the CSS page size was preferred over the paper size."""

    print_background: Optional[bool] = None
    """Whether background graphics were printed."""

    scale: Optional[float] = None
    """Page render scale."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    transfer_mode: Optional[Literal["ReturnAsBase64", "ReturnAsStream", "other"]] = None
    """How the PDF was returned (`ReturnAsBase64` or `ReturnAsStream`).

    A value the protocol does not define is reported as `other`.
    """


class DataBrowserCdpPageStartScreencastCommandData(BaseModel):
    """Sanitized `Page.startScreencast` arguments.

    Canonical input: `Page.startScreencast` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.startScreencast"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    every_nth_frame: Optional[int] = None
    """Frame sampling interval."""

    format: Optional[Literal["jpeg", "png", "other"]] = None
    """Frame format requested (`jpeg` or `png`).

    A value the protocol does not define is reported as `other`.
    """

    max_height: Optional[int] = None
    """Maximum frame height in pixels."""

    max_width: Optional[int] = None
    """Maximum frame width in pixels."""

    quality: Optional[int] = None
    """Compression quality, 0 to 100."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageStopScreencastCommandData(BaseModel):
    """Sanitized `Page.stopScreencast` arguments.

    Canonical input: `Page.stopScreencast` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.stopScreencast"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageStopLoadingCommandData(BaseModel):
    """Sanitized `Page.stopLoading` arguments.

    Canonical input: `Page.stopLoading` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.stopLoading"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageCloseCommandData(BaseModel):
    """Sanitized `Page.close` arguments.

    Canonical input: `Page.close` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.close"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpPageSetWebLifecycleStateCommandData(BaseModel):
    """Sanitized `Page.setWebLifecycleState` arguments.

    Canonical input: `Page.setWebLifecycleState` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Page.setWebLifecycleState"]

    state: Literal["frozen", "active", "other"]
    """Lifecycle state applied (`frozen` or `active`).

    A value the protocol does not define is reported as `other`.
    """

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpTargetActivateTargetCommandData(BaseModel):
    """Sanitized `Target.activateTarget` arguments.

    Canonical input: `Target.activateTarget` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Target.activateTarget"]

    target_id: str
    """Opaque target identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpTargetCloseTargetCommandData(BaseModel):
    """Sanitized `Target.closeTarget` arguments.

    Canonical input: `Target.closeTarget` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Target.closeTarget"]

    target_id: str
    """Opaque target identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpTargetCreateTargetCommandData(BaseModel):
    """Sanitized `Target.createTarget` arguments.

    Canonical input: `Target.createTarget` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Target.createTarget"]

    background: Optional[bool] = None
    """Whether the target was created in the background."""

    browser_context_id: Optional[str] = None
    """Opaque browser context identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    enable_begin_frame_control: Optional[bool] = None
    """Whether BeginFrame control was enabled (headless only)."""

    focus: Optional[bool] = None
    """Whether the new target was focused."""

    for_tab: Optional[bool] = None
    """Whether a tab target rather than a page target was created."""

    height: Optional[int] = None
    """Window height in DIP."""

    hidden: Optional[bool] = None
    """Whether the target was created hidden."""

    left: Optional[int] = None
    """Window x position in screen coordinates."""

    new_window: Optional[bool] = None
    """Whether a new window was requested."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    top: Optional[int] = None
    """Window y position in screen coordinates."""

    url_scheme: Optional[str] = None
    """Scheme of the destination URL (e.g.

    `https`, `about`, `data`). The rest of the URL is never captured.
    """

    width: Optional[int] = None
    """Window width in DIP."""

    window_state: Optional[Literal["normal", "minimized", "maximized", "fullscreen", "other"]] = None
    """Window state requested (`normal`, `minimized`, `maximized`, `fullscreen`).

    A value the protocol does not define is reported as `other`.
    """


class DataBrowserCdpTargetCreateBrowserContextCommandData(BaseModel):
    """Sanitized `Target.createBrowserContext` arguments.

    Canonical input: `Target.createBrowserContext` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Target.createBrowserContext"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    dispose_on_detach: Optional[bool] = None
    """Whether the context is disposed when the debugging session detaches."""

    proxy_bypass_list_present: Optional[bool] = None
    """Whether a proxy bypass list was configured."""

    proxy_server_present: Optional[bool] = None
    """Whether a proxy was configured. The proxy address is never captured."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    universal_network_access_origin_count: Optional[int] = None
    """Number of origins granted universal network access.

    The origins themselves are never captured.
    """


class DataBrowserCdpTargetDisposeBrowserContextCommandData(BaseModel):
    """Sanitized `Target.disposeBrowserContext` arguments.

    Canonical input: `Target.disposeBrowserContext` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    browser_context_id: str
    """Opaque browser context identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    method: Literal["Target.disposeBrowserContext"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpTargetOpenDevToolsCommandData(BaseModel):
    """Sanitized `Target.openDevTools` arguments.

    Canonical input: `Target.openDevTools` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Target.openDevTools"]

    target_id: str
    """Opaque target identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    panel_id: Optional[str] = None
    """DevTools panel opened.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpBrowserCancelDownloadCommandData(BaseModel):
    """Sanitized `Browser.cancelDownload` arguments.

    Canonical input: `Browser.cancelDownload` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    download_guid: str
    """Opaque identifier of the download that was cancelled.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    method: Literal["Browser.cancelDownload"]

    browser_context_id: Optional[str] = None
    """Opaque browser context identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpBrowserCloseCommandData(BaseModel):
    """Sanitized `Browser.close` arguments.

    Canonical input: `Browser.close` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Browser.close"]

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


class DataBrowserCdpBrowserSetWindowBoundsCommandData(BaseModel):
    """Sanitized `Browser.setWindowBounds` arguments.

    Canonical input: `Browser.setWindowBounds` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Browser.setWindowBounds"]

    window_id: int
    """Browser window identifier."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    height: Optional[int] = None
    """Window height in DIP."""

    left: Optional[int] = None
    """Window x position in screen coordinates."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    top: Optional[int] = None
    """Window y position in screen coordinates."""

    width: Optional[int] = None
    """Window width in DIP."""

    window_state: Optional[Literal["normal", "minimized", "maximized", "fullscreen", "other"]] = None
    """Window state requested (`normal`, `minimized`, `maximized`, `fullscreen`).

    A value the protocol does not define is reported as `other`.
    """


class DataBrowserCdpBrowserSetContentsSizeCommandData(BaseModel):
    """Sanitized `Browser.setContentsSize` arguments.

    Canonical input: `Browser.setContentsSize` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    method: Literal["Browser.setContentsSize"]

    window_id: int
    """Browser window identifier."""

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    height: Optional[int] = None
    """Contents height in DIP."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """

    width: Optional[int] = None
    """Contents width in DIP."""


class DataBrowserCdpAutofillTriggerCommandData(BaseModel):
    """Sanitized `Autofill.trigger` arguments.

    Canonical input: `Autofill.trigger` in devtools-protocol@2d019e73, pinned at https://github.com/ChromeDevTools/devtools-protocol/blob/2d019e73eb371d1d6985d26d395d78bd8f8a22ba/json/browser_protocol.json. Every argument of this command has a retained or redacted decision in lib/devtoolsproxy/testdata/cdp_arguments.yaml.
    """

    field_id: int
    """Opaque backend node identifier of the field that was autofilled."""

    method: Literal["Autofill.trigger"]

    address_field_count: Optional[int] = None
    """Number of address fields the command filled.

    Their names and values are never captured.
    """

    command_id: Optional[int] = None
    """
    The command's JSON-RPC id, so the command can be joined to the result the
    browser returned for it. Absent when the client sent none.
    """

    connection_id: Optional[str] = None
    """
    Identifies the CDP proxy connection the command arrived on, matching
    `cdp_connect` and `cdp_disconnect`. Two clients driving the same browser are
    told apart by this.
    """

    frame_id: Optional[str] = None
    """Opaque frame identifier.

    Clipped to 128 characters; a longer value is not a real identifier.
    """

    mode: Optional[Literal["card", "address"]] = None
    """What was filled: `card` or `address`. The values themselves are never captured."""

    session_id: Optional[str] = None
    """CDP session identifier the command was addressed to.

    Absent for browser-level commands. Clipped to 128 characters.
    """


Data: TypeAlias = Annotated[
    Union[
        DataBrowserCdpInputDispatchMouseEventCommandData,
        DataBrowserCdpInputDispatchKeyEventCommandData,
        DataBrowserCdpInputInsertTextCommandData,
        DataBrowserCdpInputImeSetCompositionCommandData,
        DataBrowserCdpInputDispatchTouchEventCommandData,
        DataBrowserCdpInputDispatchDragEventCommandData,
        DataBrowserCdpInputCancelDraggingCommandData,
        DataBrowserCdpInputEmulateTouchFromMouseEventCommandData,
        DataBrowserCdpInputSynthesizePinchGestureCommandData,
        DataBrowserCdpInputSynthesizeScrollGestureCommandData,
        DataBrowserCdpInputSynthesizeTapGestureCommandData,
        DataBrowserCdpDomSetFileInputFilesCommandData,
        DataBrowserCdpDomFocusCommandData,
        DataBrowserCdpDomScrollIntoViewIfNeededCommandData,
        DataBrowserCdpPageBringToFrontCommandData,
        DataBrowserCdpPageCaptureScreenshotCommandData,
        DataBrowserCdpPageCaptureSnapshotCommandData,
        DataBrowserCdpPageHandleJavaScriptDialogCommandData,
        DataBrowserCdpPageNavigateCommandData,
        DataBrowserCdpPageNavigateToHistoryEntryCommandData,
        DataBrowserCdpPageReloadCommandData,
        DataBrowserCdpPagePrintToPdfCommandData,
        DataBrowserCdpPageStartScreencastCommandData,
        DataBrowserCdpPageStopScreencastCommandData,
        DataBrowserCdpPageStopLoadingCommandData,
        DataBrowserCdpPageCloseCommandData,
        DataBrowserCdpPageSetWebLifecycleStateCommandData,
        DataBrowserCdpTargetActivateTargetCommandData,
        DataBrowserCdpTargetCloseTargetCommandData,
        DataBrowserCdpTargetCreateTargetCommandData,
        DataBrowserCdpTargetCreateBrowserContextCommandData,
        DataBrowserCdpTargetDisposeBrowserContextCommandData,
        DataBrowserCdpTargetOpenDevToolsCommandData,
        DataBrowserCdpBrowserCancelDownloadCommandData,
        DataBrowserCdpBrowserCloseCommandData,
        DataBrowserCdpBrowserSetWindowBoundsCommandData,
        DataBrowserCdpBrowserSetContentsSizeCommandData,
        DataBrowserCdpAutofillTriggerCommandData,
    ],
    PropertyInfo(discriminator="method"),
]


class BrowserCdpCommandEvent(BaseModel):
    """
    A browser-control command a client sent over the CDP WebSocket proxy: input gestures, navigation, dialog handling, file selection and screenshots. Configuration commands and the DOM/Runtime traffic a client library issues on the caller's behalf are not reported.
    One event per browser-control command that reached the browser. The command stream is not sampled, coalesced or reordered. An event is lost only when the method is excluded by telemetry configuration, when the command's arguments do not decode, or when classification cannot keep up. Exclusions are counted in `cdp_disconnect.telemetry_excluded`; the rest in `cdp_disconnect.telemetry_dropped`.
    """

    category: Literal["control"]

    data: Data
    """Per-command payload for `cdp_command` events, discriminated by `method`.

    Each variant carries only the arguments approved for that command: values that
    could hold a secret — typed and composition text, URLs, referrers, scripts,
    templates, file paths, drag contents and autofill values — are replaced by a
    length, a count, a presence flag, an enum or a URL scheme and host.
    """

    source: BrowserEventSource
    """Provenance metadata identifying which producer emitted the event."""

    ts: int
    """Event timestamp in Unix microseconds."""

    type: Literal["cdp_command"]

    truncated: Optional[bool] = None
    """True if the data field was truncated due to size limits."""
