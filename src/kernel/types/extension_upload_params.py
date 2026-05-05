# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["ExtensionUploadParams"]


class ExtensionUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """ZIP file containing the browser extension."""

    name: str
    """Optional unique name within the project to reference this extension."""
