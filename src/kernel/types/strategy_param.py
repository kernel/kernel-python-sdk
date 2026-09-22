# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .provider_target_param import ProviderTargetParam

__all__ = ["StrategyParam", "SearchAutoStrategy", "SearchPinnedStrategy", "SearchFallbackStrategy"]


class SearchAutoStrategy(TypedDict, total=False):
    type: Required[Literal["auto"]]
    """Let Kernel choose an eligible provider by capability fit."""

    fallback_on: List[Literal["error", "timeout", "empty"]]
    """
    Conditions that advance to the next provider under auto routing or an explicit
    providers chain. Ignored when provider pins a single provider. error means a
    retryable provider failure, including rate limiting, not invalid caller input or
    caller quotas. empty means zero results after required filtering. An empty list
    disables fallback. If every attempt is empty or fails, the response is the first
    valid empty response with the full attempt trail, or a 502 if none succeeded.
    """

    provider_options: Iterable[ProviderTargetParam]
    """
    Provider targets available to auto routing, each paired with typed native
    options. Provider names must be unique.
    """


class SearchPinnedStrategy(TypedDict, total=False):
    provider: Required[ProviderTargetParam]
    """Provider name paired with its typed native options."""

    type: Required[Literal["pinned"]]
    """Use exactly the selected provider with no cross-provider fallback."""


class SearchFallbackStrategy(TypedDict, total=False):
    providers: Required[Iterable[ProviderTargetParam]]
    """Ordered provider targets. Provider names must be unique."""

    type: Required[Literal["fallback"]]
    """Try providers in order and advance when fallback_on matches the outcome."""

    fallback_on: List[Literal["error", "timeout", "empty"]]
    """
    Conditions that advance to the next provider under auto routing or an explicit
    providers chain. Ignored when provider pins a single provider. error means a
    retryable provider failure, including rate limiting, not invalid caller input or
    caller quotas. empty means zero results after required filtering. An empty list
    disables fallback. If every attempt is empty or fails, the response is the first
    valid empty response with the full attempt trail, or a 502 if none succeeded.
    """


StrategyParam: TypeAlias = Union[SearchAutoStrategy, SearchPinnedStrategy, SearchFallbackStrategy]
