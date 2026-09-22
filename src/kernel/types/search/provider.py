# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Provider",
    "Content",
    "Params",
    "ParamsCountry",
    "ParamsEndDate",
    "ParamsExcludeDomains",
    "ParamsIncludeDomains",
    "ParamsLanguage",
    "ParamsRecency",
    "ParamsSafeSearch",
    "ParamsStartDate",
    "ProviderOptions",
]


class Content(BaseModel):
    freshness_control: bool
    """Can enforce the requested maximum content age."""

    inline: bool
    """Supports content retrieval with the search request."""

    post_hoc: bool
    """Supports content retrieval after the search completes."""


class ParamsCountry(BaseModel):
    support: Literal["native", "emulated", "unsupported"]

    notes: Optional[str] = None
    """Translation behavior, limitations, and precision."""


class ParamsEndDate(BaseModel):
    support: Literal["native", "emulated", "unsupported"]

    notes: Optional[str] = None
    """Translation behavior, limitations, and precision."""


class ParamsExcludeDomains(BaseModel):
    support: Literal["native", "emulated", "unsupported"]

    notes: Optional[str] = None
    """Translation behavior, limitations, and precision."""


class ParamsIncludeDomains(BaseModel):
    support: Literal["native", "emulated", "unsupported"]

    notes: Optional[str] = None
    """Translation behavior, limitations, and precision."""


class ParamsLanguage(BaseModel):
    support: Literal["native", "emulated", "unsupported"]

    notes: Optional[str] = None
    """Translation behavior, limitations, and precision."""


class ParamsRecency(BaseModel):
    support: Literal["native", "emulated", "unsupported"]

    notes: Optional[str] = None
    """Translation behavior, limitations, and precision."""


class ParamsSafeSearch(BaseModel):
    support: Literal["native", "emulated", "unsupported"]

    notes: Optional[str] = None
    """Translation behavior, limitations, and precision."""


class ParamsStartDate(BaseModel):
    support: Literal["native", "emulated", "unsupported"]

    notes: Optional[str] = None
    """Translation behavior, limitations, and precision."""


class Params(BaseModel):
    country: ParamsCountry

    end_date: ParamsEndDate

    exclude_domains: ParamsExcludeDomains

    include_domains: ParamsIncludeDomains

    language: ParamsLanguage

    recency: ParamsRecency

    safe_search: ParamsSafeSearch

    start_date: ParamsStartDate


class ProviderOptions(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """JSON Schema for the provider-native options accepted by POST /search."""

    schema_ref: str
    """OpenAPI component name for the matching typed provider-options schema."""

    examples: Optional[List[Dict[str, object]]] = None


class Provider(BaseModel):
    content: Content

    max_results_cap: int

    params: Params

    provider_options: ProviderOptions

    slug: str

    notes: Optional[List[str]] = None
    """
    Provider-specific limitations, conditional filter support, and warnings about
    search modes.
    """
