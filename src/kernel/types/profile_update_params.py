# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    name: Required[str]
    """New profile name.

    Must be unique within the logical project; during the default-project migration,
    unscoped profiles and profiles in the org default project are treated as the
    same project.
    """
