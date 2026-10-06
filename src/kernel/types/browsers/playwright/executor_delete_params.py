# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExecutorDeleteParams"]


class ExecutorDeleteParams(TypedDict, total=False):
    id_or_name: Required[str]

    close_tab: bool
    """Close the executor's tab. Defaults to true."""
