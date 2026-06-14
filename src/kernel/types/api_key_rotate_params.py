# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["APIKeyRotateParams"]


class APIKeyRotateParams(TypedDict, total=False):
    days_to_expire: Optional[int]
    """Lifetime in days for the new key, up to 3650.

    Omit to reuse the rotated key's original lifetime, or never-expires if it had
    none.
    """

    expire_in_days: Optional[int]
    """Grace period in days before the rotated key expires.

    Use 0 to expire it immediately. Omit for the default grace period of 7 days.
    """
