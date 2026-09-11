# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .vault_card_aliases import VaultCardAliases
from .agentcard_checkout_authorization import AgentcardCheckoutAuthorization

__all__ = ["CardVaultItemState", "LinkCardState", "LinkCardStateMasks", "AgentCardCardState", "AgentCardCardStateMasks"]


class LinkCardStateMasks(BaseModel):
    brand: Optional[str] = None

    last4: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...
    else:
        __pydantic_extra__: Dict[str, str]


class LinkCardState(BaseModel):
    provider: Literal["link"]

    status: Literal[
        "requested", "pending_authorization", "ready", "consumed", "expired", "declined", "recovery_required"
    ]
    """recovery_required means an original provider operation has an unresolved
    outcome.

    Do not retry, delete, or replace it. Known references may be observed safely,
    but unknown creation without an ID and uncertain card-material retrieval require
    manual reconciliation with the provider or support. There is no reset or
    caller-asserted reconciliation operation.
    """

    aliases: Optional[VaultCardAliases] = None

    domains: Optional[List[str]] = None

    masks: Optional[LinkCardStateMasks] = None

    status_reason: Optional[str] = None


class AgentCardCardStateMasks(BaseModel):
    brand: Optional[str] = None

    last4: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...
    else:
        __pydantic_extra__: Dict[str, str]


class AgentCardCardState(BaseModel):
    provider: Literal["agentcard"]

    status: Literal["requested", "ready", "pending_approval", "degraded", "recovery_required"]
    """recovery_required means the original checkout outcome is unresolved.

    Do not retry, delete, or replace it. Known authorization IDs may be reconciled
    through provider observations; otherwise contact the provider or support for
    manual reconciliation. It does not mean declined or expired.
    """

    aliases: Optional[VaultCardAliases] = None

    authorization: Optional[AgentcardCheckoutAuthorization] = None
    """The in-flight or most recent checkout authorization.

    Present while a checkout is pending approval and after it settles.
    """

    masks: Optional[AgentCardCardStateMasks] = None

    status_reason: Optional[str] = None


CardVaultItemState: TypeAlias = Annotated[
    Union[LinkCardState, AgentCardCardState], PropertyInfo(discriminator="provider")
]
