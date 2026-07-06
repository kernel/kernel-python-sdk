# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel
from .shared.app_action import AppAction

__all__ = ["AppListResponse"]


class AppListResponse(BaseModel):
    """Summary of an application version."""

    id: str
    """Unique identifier for the app version"""

    actions: List[AppAction]
    """List of actions available on the app"""

    app_name: str
    """Name of the application"""

    deployment: str
    """Deployment ID"""

    env_vars: Dict[str, str]
    """Environment variables configured for this app version.

    Values are redacted for API key, OAuth, and managed-auth callers, which receive
    every key with an empty string value. Only dashboard sessions receive the actual
    values.
    """

    region: Literal["aws.us-east-1a"]
    """Deployment region code"""

    version: str
    """Version label for the application"""
