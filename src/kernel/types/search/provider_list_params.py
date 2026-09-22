# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProviderListParams"]


class ProviderListParams(TypedDict, total=False):
    slug: Literal["brave", "exa", "perplexity", "context", "parallel", "valyu", "octen", "you", "tavily", "serpapi"]
    """Optional concrete provider slug filter. Omit to list every provider."""
