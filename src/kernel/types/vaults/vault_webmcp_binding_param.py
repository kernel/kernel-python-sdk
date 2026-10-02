# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VaultWebmcpBindingParam"]


class VaultWebmcpBindingParam(TypedDict, total=False):
    field: Required[str]
    """A declared, populated credential field or supported card field.

    A TOTP field supplies a fresh code, never its seed.
    """

    input_path: Required[str]
    """RFC 6901 JSON Pointer to an existing null value in input.

    Object keys are exact; array indices must be canonical and in range. No root or
    array-append paths. Each path and each field may occur only once.
    """

    format: str
    """Required for card expiration (MM/YY or MM/YYYY), forbidden for other fields.

    Invalid formats are rejected before invocation.
    """
