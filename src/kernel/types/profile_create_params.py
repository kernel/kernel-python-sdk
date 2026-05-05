# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileCreateParams"]


class ProfileCreateParams(TypedDict, total=False):
    name: str
    """Optional name of the profile. Must be unique within the project."""
