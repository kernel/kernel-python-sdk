# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ProviderTargetParam",
    "SearchBraveTarget",
    "SearchBraveTargetOptions",
    "SearchExaTarget",
    "SearchExaTargetOptions",
    "SearchExaTargetOptionsContents",
    "SearchPerplexityTarget",
    "SearchPerplexityTargetOptions",
    "SearchContextTarget",
    "SearchContextTargetOptions",
    "SearchContextTargetOptionsMarkdownOptions",
    "SearchContextTargetOptionsMarkdownOptionsPdf",
    "SearchParallelTarget",
    "SearchParallelTargetOptions",
    "SearchParallelTargetOptionsAdvancedSettings",
    "SearchParallelTargetOptionsAdvancedSettingsExcerptSettings",
    "SearchParallelTargetOptionsAdvancedSettingsFetchPolicy",
    "SearchParallelTargetOptionsAdvancedSettingsSourcePolicy",
    "SearchValyuTarget",
    "SearchValyuTargetOptions",
    "SearchOctenTarget",
    "SearchOctenTargetOptions",
    "SearchOctenTargetOptionsFullContent",
    "SearchOctenTargetOptionsHighlight",
    "SearchYouTarget",
    "SearchYouTargetOptions",
    "SearchYouTargetOptionsExtraction",
    "SearchYouTargetOptionsExtractionFullPage",
    "SearchTavilyTarget",
    "SearchTavilyTargetOptions",
    "SearchSerpAPITarget",
    "SearchSerpAPITargetOptions",
]


class SearchBraveTargetOptions(TypedDict, total=False):
    count: int
    """Provider-native count.

    Lower-only alias for max_results; cannot raise the effective result cap.
    """

    extra_snippets: bool
    """Request additional snippets from Brave."""

    goggles: str
    """Goggles re-ranking definition URL."""

    goggles_id: str
    """Deprecated Brave Goggle identifier. Prefer goggles."""

    include_fetch_metadata: bool
    """Include Brave's fetch metadata."""

    offset: int
    """Page offset supported by Brave."""

    operators: str
    """Brave search operators."""

    result_filter: str
    """Comma-separated result types to include, e.g. "web,news"."""

    search_lang: str
    """Language of the search, e.g. "en"."""

    spellcheck: bool
    """Apply Brave's query spellcheck."""

    ui_lang: str
    """Language for UI strings in the response."""

    units: Literal["metric", "imperial"]
    """Measurement units."""


class SearchBraveTarget(TypedDict, total=False):
    provider: Required[Literal["brave"]]

    options: SearchBraveTargetOptions


class SearchExaTargetOptionsContents(TypedDict, total=False):
    """Provider-native content retrieval.

    Available without requesting Kernel browser retrieval; may incur provider retrieval charges.
    """

    highlights: bool
    """Return query-relevant provider excerpts."""

    text: bool
    """Return provider page text."""


class SearchExaTargetOptions(TypedDict, total=False):
    category: str
    """Provider data-category hint."""

    compliance: str
    """Provider-native compliance controls.

    Requires support and authorization on the provider account.
    """

    contents: SearchExaTargetOptionsContents
    """Provider-native content retrieval.

    Available without requesting Kernel browser retrieval; may incur provider
    retrieval charges.
    """

    max_age_hours: Annotated[float, PropertyInfo(alias="maxAgeHours")]
    """Provider-native cache-age control.

    Unlike content.max_age_hours, this retains Exa semantics, including any native
    sentinel values. It does not imply a cross-provider freshness guarantee.
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Provider-native count. Lower-only alias for max_results."""

    type: Literal["auto", "fast", "instant"]
    """Search mode supported by Exa."""


class SearchExaTarget(TypedDict, total=False):
    provider: Required[Literal["exa"]]

    options: SearchExaTargetOptions


class SearchPerplexityTargetOptions(TypedDict, total=False):
    last_updated_after_filter: str
    """MM/DD/YYYY. Filters by last-updated date, not published date."""

    last_updated_before_filter: str
    """MM/DD/YYYY upper bound on last-updated date."""

    max_results: int
    """Provider-native count. Lower-only alias for max_results."""

    max_tokens: int
    """Values outside the documented range are rejected."""

    max_tokens_per_page: int
    """Per-page token cap."""

    query: SequenceNotStr[str]
    """Provider-native multi-query form, applied only to Perplexity.

    Other fallback providers receive the top-level query. Each query may incur a
    separate provider charge.
    """

    search_context_size: Literal["low", "medium", "high"]
    """Provider context size supported by the selected model."""

    search_language_filter: SequenceNotStr[str]
    """ISO 639-1 language codes, max 20."""


class SearchPerplexityTarget(TypedDict, total=False):
    provider: Required[Literal["perplexity"]]

    options: SearchPerplexityTargetOptions


class SearchContextTargetOptionsMarkdownOptionsPdf(TypedDict, total=False):
    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]


class SearchContextTargetOptionsMarkdownOptions(TypedDict, total=False):
    enabled: bool

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]

    pdf: SearchContextTargetOptionsMarkdownOptionsPdf

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]


class SearchContextTargetOptions(TypedDict, total=False):
    country: str
    """ISO 3166-1 alpha-2 country code."""

    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]
    """Blocklist of result domains."""

    freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"]
    """Restrict results to content published within this window."""

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]
    """Allowlist of result domains."""

    markdown_options: Annotated[SearchContextTargetOptionsMarkdownOptions, PropertyInfo(alias="markdownOptions")]

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to request from Context.dev."""

    query_fanout: Annotated[bool, PropertyInfo(alias="queryFanout")]
    """Expand the query into multiple parallel variants."""

    tags: SequenceNotStr[str]
    """Usage tracking tags."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Context.dev request timeout in milliseconds."""


class SearchContextTarget(TypedDict, total=False):
    provider: Required[Literal["context"]]

    options: SearchContextTargetOptions


class SearchParallelTargetOptionsAdvancedSettingsExcerptSettings(TypedDict, total=False):
    max_chars_per_result: Optional[int]


class SearchParallelTargetOptionsAdvancedSettingsFetchPolicy(TypedDict, total=False):
    disable_cache_fallback: bool
    """When false, the provider may return cached content after live fetching fails."""

    max_age_seconds: Optional[int]
    """Native live-fetch trigger; minimum 600 seconds.

    Not the unified hard-freshness control.
    """

    timeout_seconds: Optional[float]
    """Native live-fetch timeout, bounded by the remaining overall deadline."""


class SearchParallelTargetOptionsAdvancedSettingsSourcePolicy(TypedDict, total=False):
    after_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Native publication-date lower bound."""

    exclude_domains: SequenceNotStr[str]
    """
    Native exclusions; the provider ignores these when native include_domains is
    non-empty.
    """

    include_domains: SequenceNotStr[str]
    """Native domain/path restrictions.

    Explicit unified domain parameters take precedence. Combined include/exclude
    native lists cannot exceed 200 entries.
    """


class SearchParallelTargetOptionsAdvancedSettings(TypedDict, total=False):
    """Explicit search settings.

    Unified search parameters are re-applied to overlapping settings; native result counts are lower-only.
    """

    excerpt_settings: SearchParallelTargetOptionsAdvancedSettingsExcerptSettings

    fetch_policy: SearchParallelTargetOptionsAdvancedSettingsFetchPolicy

    location: Optional[str]
    """Native ISO 3166-1 alpha-2 location preference."""

    max_results: Optional[int]
    """Native count; lower-only alias for unified max_results."""

    source_policy: SearchParallelTargetOptionsAdvancedSettingsSourcePolicy


class SearchParallelTargetOptions(TypedDict, total=False):
    advanced_settings: SearchParallelTargetOptionsAdvancedSettings
    """Explicit search settings.

    Unified search parameters are re-applied to overlapping settings; native result
    counts are lower-only.
    """

    client_model: str
    """Client model hint."""

    max_chars_total: int
    """Cap total characters returned."""

    mode: Literal["turbo", "fast", "basic", "advanced"]
    """Search mode.

    Basic is used when omitted; each mode can have different latency and charges.
    """

    objective: str
    """The goal behind the search, stated separately from the query."""

    search_queries: SequenceNotStr[str]
    """Provider-native multi-query search. Defaults to [query] for this provider."""

    session_id: str
    """Group related searches."""


class SearchParallelTarget(TypedDict, total=False):
    provider: Required[Literal["parallel"]]

    options: SearchParallelTargetOptions


class SearchValyuTargetOptions(TypedDict, total=False):
    fast_mode: bool
    """Trade depth for latency."""

    historical_cache: bool
    """Allow historical cached results."""

    include_abstracts: bool
    """Include abstracts for academic sources."""

    instructions: str
    """Natural-language retrieval guidance."""

    is_tool_call: bool
    """Mark the search as an agent tool call."""

    max_num_results: int
    """Provider-native count. Lower-only alias for max_results."""

    max_price: float
    """Provider-native USD-per-thousand-results price ceiling. Forwarded to Valyu."""

    relevance_threshold: float
    """Provider-native minimum relevance threshold.

    Not a normalized cross-provider score.
    """

    response_length: Literal["short", "medium", "large", "max"]
    """Provider result-content length preset."""

    search_type: str
    """Corpus selector, including all, web, proprietary, and news.

    Provider corpus choice may change billing; Kernel does not force web-only
    searches.
    """

    source_biases: SequenceNotStr[str]
    """Bias retrieval toward these sources."""

    url_only: bool
    """Return URLs without content."""


class SearchValyuTarget(TypedDict, total=False):
    provider: Required[Literal["valyu"]]

    options: SearchValyuTargetOptions


class SearchOctenTargetOptionsFullContent(TypedDict, total=False):
    enable: bool

    max_tokens: int


class SearchOctenTargetOptionsHighlight(TypedDict, total=False):
    enable: bool

    max_tokens: int


class SearchOctenTargetOptions(TypedDict, total=False):
    count: int

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    exclude_domains: SequenceNotStr[str]

    exclude_text: SequenceNotStr[str]

    format: Literal["markdown", "text"]

    full_content: SearchOctenTargetOptionsFullContent

    highlight: SearchOctenTargetOptionsHighlight

    include_domains: SequenceNotStr[str]

    include_images: bool

    include_text: SequenceNotStr[str]

    language: SequenceNotStr[str]

    safesearch: Literal["off", "strict"]

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    time_basis: Literal["auto", "published", "crawled"]

    time_range: Literal["day", "week", "month", "year", "d", "w", "m", "y"]

    topic: Literal["general", "news"]


class SearchOctenTarget(TypedDict, total=False):
    provider: Required[Literal["octen"]]

    options: SearchOctenTargetOptions


class SearchYouTargetOptionsExtractionFullPage(TypedDict, total=False):
    extraction_formats: List[Literal["html", "markdown"]]


class SearchYouTargetOptionsExtraction(TypedDict, total=False):
    """Provider-native page extraction.

    Both modes may incur per-row charges; full_page may retrieve web and news rows.
    """

    extraction_mode: Required[Literal["highlights", "full_page"]]

    full_page: SearchYouTargetOptionsExtractionFullPage


class SearchYouTargetOptions(TypedDict, total=False):
    boost_domains: SequenceNotStr[str]
    """Prefer these domains without excluding others.

    Cannot be combined with include_domains if the provider does not accept the
    combination.
    """

    count: int
    """Provider-native per-section count.

    Lower-only alias for max_results. Web and news sections may produce more rows
    than Kernel returns.
    """

    crawl_timeout: int
    """
    Native extraction timeout in seconds, bounded by the remaining Kernel request
    deadline.
    """

    extraction: SearchYouTargetOptionsExtraction
    """Provider-native page extraction.

    Both modes may incur per-row charges; full_page may retrieve web and news rows.
    """

    knowledge: Literal["core"]
    """Request licensed-data output.

    URL-less knowledge entries are not converted into web results; include_raw
    exposes the full provider response separately.
    """

    language: str
    """BCP 47 result language from You.com's 51-value enum, e.g.

    "EN", "JA". Default EN.
    """

    offset: int
    """Page offset supported by You.com."""


class SearchYouTarget(TypedDict, total=False):
    provider: Required[Literal["you"]]

    options: SearchYouTargetOptions


class SearchTavilyTargetOptions(TypedDict, total=False):
    auto_parameters: bool
    """Allow the provider to choose search parameters.

    May select a different billing tier; explicit caller values retain
    provider-native precedence.
    """

    chunks_per_source: int
    """Provider excerpts per source, up to 500 characters each."""

    exact_match: bool
    """Require the quoted phrases in the query verbatim, bypassing semantic matches."""

    filter_by_language: bool
    """Strictly filter non-matching languages. Requires `language`."""

    include_answer: Union[bool, Literal["basic", "advanced"]]
    """Request the provider's generated answer.

    Returned as answer on the search response, independently of include_raw.
    """

    include_domains_mode: Literal["filter", "boost"]
    """Native filter versus ranking boost semantics.

    Boost influences ranking rather than restricting results to the listed domains.
    Requires include_domains.
    """

    include_favicon: bool
    """Favicon URL per result."""

    include_image_descriptions: bool
    """Describe each image. Needs include_images."""

    include_images: bool
    """Query-related images plus per-result images."""

    include_raw_content: Union[bool, Literal["markdown", "text"]]
    """Request native full-page content.

    Defaults to markdown when omitted for this provider, False disables that native
    retrieval; it does not disable explicitly requested Kernel browser retrieval.
    """

    language: str
    """ISO 639-1 code or English language name.

    Ranking boost unless filter_by_language.
    """

    max_results: int
    """Provider-native count. Lower-only alias for max_results."""

    search_depth: Literal["advanced", "basic", "fast", "ultra-fast"]
    """Provider relevance and latency tier.

    Some tiers cannot be combined with native safe search; conflicts are described
    in warnings.
    """

    topic: Literal["general", "news", "finance"]
    """Provider corpus selector. Publication metadata depends on the selected topic."""


class SearchTavilyTarget(TypedDict, total=False):
    provider: Required[Literal["tavily"]]

    options: SearchTavilyTargetOptions


class SearchSerpAPITargetOptions(TypedDict, total=False):
    engine: Required[str]
    """SerpApi engine identifier.

    The Kernel integration currently supports google only.
    """

    device: Literal["desktop", "mobile", "tablet"]
    """Device profile used for the search."""

    filter: Literal[0, 1]
    """Google duplicate-content filter."""

    gl: str
    """Two-letter Google country code."""

    google_domain: str
    """Google domain to search when using the google engine."""

    hl: str
    """Interface language code."""

    location: str
    """Free-form geographic location used for localized results."""

    nfpr: Literal[0, 1]
    """Google auto-correction filter."""

    no_cache: bool
    """When true, bypass SerpApi cached results when supported."""

    num: int
    """Number of results requested from the search engine."""

    safe: Literal["active", "off"]
    """Safe-search setting for engines that support it."""

    start: int
    """Zero-based result offset for pagination."""

    tbm: str
    """Google vertical search selector, such as images, video, news, or shopping."""

    tbs: str
    """Google time and search modifiers, including freshness filters."""


class SearchSerpAPITarget(TypedDict, total=False):
    provider: Required[Literal["serpapi"]]

    options: SearchSerpAPITargetOptions


ProviderTargetParam: TypeAlias = Union[
    SearchBraveTarget,
    SearchExaTarget,
    SearchPerplexityTarget,
    SearchContextTarget,
    SearchParallelTarget,
    SearchValyuTarget,
    SearchOctenTarget,
    SearchYouTarget,
    SearchTavilyTarget,
    SearchSerpAPITarget,
]
