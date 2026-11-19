# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkloadIdentityAuthenticationEventListParams"]


class WorkloadIdentityAuthenticationEventListParams(TypedDict, total=False):
    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    federation_rule_id: str

    issuer_id: str

    limit: int

    offset: int

    outcome: Literal["success", "failure"]

    project_id: str

    service_account_id: str

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
