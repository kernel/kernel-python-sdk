# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .kernel_card_state import KernelCardState

__all__ = ["PaymentRequestVaultItemState", "LinkCardState", "LinkCardStateMasks"]


class LinkCardStateMasks(BaseModel):
    brand: Optional[str] = None

    last4: Optional[str] = None

    token_last4: Optional[str] = None
    """Last four digits of the network token presented to the merchant."""

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
    """Issued Link cards retain encrypted card material for the fill operation.

    Link cards do not expose aliases or support egress substitution.
    """

    provider: Literal["link"]

    status: Literal[
        "requested", "pending_authorization", "ready", "consumed", "expired", "declined", "recovery_required"
    ]
    """
    recovery_required means an original provider operation has an unresolved outcome
    and the card cannot be used. Reads keep observing a known provider request and
    may clear the recovery. To continue, delete this card and create a new one;
    deleting cancels the original request when its ID is known and keeps the
    recovery evidence. The user may see an approval request for the original card
    and should approve only the new one.
    """

    domains: Optional[List[str]] = None

    masks: Optional[LinkCardStateMasks] = None

    status_reason: Optional[str] = None


PaymentRequestVaultItemState: TypeAlias = Annotated[
    Union[LinkCardState, KernelCardState], PropertyInfo(discriminator="provider")
]
