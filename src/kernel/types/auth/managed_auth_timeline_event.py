# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ManagedAuthTimelineEvent"]


class ManagedAuthTimelineEvent(BaseModel):
    """
    A single event in an auth connection's history — a login attempt, an automatic re-auth attempt, or a health check.
    """

    id: str
    """Identifier of the underlying login/reauth session or health check."""

    status: Literal["IN_PROGRESS", "SUCCESS", "EXPIRED", "CANCELED", "FAILED", "AUTHENTICATED", "NEEDS_AUTH"]
    """Outcome of the event.

    For login/reauth events this is the flow status (IN_PROGRESS, SUCCESS, EXPIRED,
    CANCELED, FAILED). For health_check events it is the observed session state
    (AUTHENTICATED, NEEDS_AUTH).
    """

    timestamp: datetime
    """When the event occurred."""

    type: Literal["login", "reauth", "health_check"]
    """The kind of event.

    "login" and "reauth" are authentication attempts; "health_check" is a periodic
    session-validity check.
    """

    error_code: Optional[str] = None
    """Machine-readable error code. Present when a login/reauth event failed."""

    error_message: Optional[str] = None
    """Human-readable error message. Present when a login/reauth event failed."""

    previous_status: Optional[Literal["AUTHENTICATED", "NEEDS_AUTH"]] = None
    """The session state observed before this event.

    Present for health_check events that recorded a prior state.
    """

    replay_id: Optional[str] = None
    """
    Replay recording ID for the event's browser session, if session recording was
    enabled.
    """

    step: Optional[
        Literal[
            "INITIALIZED",
            "DISCOVERING",
            "AWAITING_INPUT",
            "AWAITING_EXTERNAL_ACTION",
            "AWAITING_HUMAN_INTERVENTION",
            "SUBMITTING",
            "COMPLETED",
            "EXPIRED",
        ]
    ] = None
    """The step the flow reached. Present for login/reauth events."""

    updated_at: Optional[datetime] = None
    """When the event was last updated. Present for login/reauth events."""

    website_error: Optional[str] = None
    """Visible error message from the website (e.g., 'Incorrect password').

    Present when the website displayed an error during the attempt.
    """
