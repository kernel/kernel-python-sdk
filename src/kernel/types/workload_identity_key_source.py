# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkloadIdentityKeySource"]


class WorkloadIdentityKeySource(BaseModel):
    type: Literal["discovery", "explicit_url", "inline"]

    ca_cert_pem: Optional[str] = None
    """Optional public CA certificates.

    When set, only these CAs are trusted for key retrieval, in place of the system
    roots. Private keys and private-network retrieval are not supported.
    """

    discovery_base_url: Optional[str] = None

    keys: Optional[List[Dict[str, object]]] = None

    url: Optional[str] = None
