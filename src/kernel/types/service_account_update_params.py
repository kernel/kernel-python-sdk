# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServiceAccountUpdateParams"]


class ServiceAccountUpdateParams(TypedDict, total=False):
    expected_version: Required[int]

    description: str

    name: str
