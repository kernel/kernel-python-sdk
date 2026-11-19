# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkloadIdentityKeySourceParam"]


class WorkloadIdentityKeySourceParam(TypedDict, total=False):
    type: Required[Literal["discovery", "explicit_url", "inline"]]

    ca_cert_pem: str
    """Optional public CA certificates.

    When set, only these CAs are trusted for key retrieval, in place of the system
    roots. Private keys and private-network retrieval are not supported.
    """

    discovery_base_url: str

    keys: Iterable[Dict[str, object]]

    url: str
