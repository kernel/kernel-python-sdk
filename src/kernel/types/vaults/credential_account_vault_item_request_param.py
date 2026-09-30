# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .one_password_credential_account_spec_param import OnePasswordCredentialAccountSpecParam

__all__ = ["CredentialAccountVaultItemRequestParam"]


class CredentialAccountVaultItemRequestParam(TypedDict, total=False):
    spec: Required[OnePasswordCredentialAccountSpecParam]

    type: Required[Literal["credential_account"]]
