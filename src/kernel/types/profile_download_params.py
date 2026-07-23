# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProfileDownloadParams"]


class ProfileDownloadParams(TypedDict, total=False):
    format: Literal["tar.zst", "tar"]
    """Response format for current profile archives.

    Legacy profiles are always returned as JSON.
    """
