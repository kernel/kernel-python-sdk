# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.log_event import LogEvent
from .shared.app_action import AppAction
from .shared.error_event import ErrorEvent
from .deployment_state_event import DeploymentStateEvent
from .shared.heartbeat_event import HeartbeatEvent

__all__ = ["DeploymentFollowResponse", "AppVersionSummaryEvent"]


class AppVersionSummaryEvent(BaseModel):
    """Summary of an application version."""

    id: str
    """Unique identifier for the app version"""

    actions: List[AppAction]
    """List of actions available on the app"""

    app_name: str
    """Name of the application"""

    event: Literal["app_version_summary"]
    """Event type identifier (always "app_version_summary")."""

    region: Literal["aws.us-east-1a"]
    """Deployment region code"""

    timestamp: datetime
    """Time the state was reported."""

    version: str
    """Version label for the application"""

    env_vars: Optional[Dict[str, str]] = None
    """Environment variables configured for this app version.

    Not currently populated on streamed app_version_summary events.
    """


DeploymentFollowResponse: TypeAlias = Annotated[
    Union[LogEvent, DeploymentStateEvent, AppVersionSummaryEvent, ErrorEvent, HeartbeatEvent],
    PropertyInfo(discriminator="event"),
]
