# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .one_password_oauth_action import OnePasswordOAuthAction

__all__ = [
    "VaultItemAction",
    "LinkOAuthAction",
    "SpendApprovalAction",
    "PushApprovalAction",
    "CollectAction",
    "MfaAction",
    "EmbeddedCeremonyAction",
    "CardEnrollmentAction",
]


class LinkOAuthAction(BaseModel):
    name: Literal["link_oauth"]

    url: str


class SpendApprovalAction(BaseModel):
    name: Literal["spend_approval"]

    url: str


class PushApprovalAction(BaseModel):
    name: Literal["push_approval"]


class CollectAction(BaseModel):
    name: Literal["collect"]


class MfaAction(BaseModel):
    name: Literal["mfa"]


class EmbeddedCeremonyAction(BaseModel):
    name: Literal["embedded_ceremony"]


class CardEnrollmentAction(BaseModel):
    name: Literal["card_enrollment"]

    url: str

    capture_token: Optional[str] = None
    """Secret bearer capability for embedded card capture with @onkernel/vault-react.

    Present only for Kernel wallets; never for AgentCard. Treat it like the
    enrollment URL and do not log or persist it in browser storage.
    """


VaultItemAction: TypeAlias = Annotated[
    Union[
        LinkOAuthAction,
        OnePasswordOAuthAction,
        SpendApprovalAction,
        PushApprovalAction,
        CollectAction,
        MfaAction,
        EmbeddedCeremonyAction,
        CardEnrollmentAction,
    ],
    PropertyInfo(discriminator="name"),
]
