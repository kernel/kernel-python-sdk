# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .strategy_param import StrategyParam

__all__ = ["SearchCreateParams", "Content", "ContentSearchContentOptions", "ContentSearchContentOptionsBrowser"]


class SearchCreateParams(TypedDict, total=False):
    query: Required[str]
    """Primary search query.

    A provider-native multi-query option applies only to that provider; other
    providers in a fallback chain receive this query.
    """

    content: Content
    """Optional portable content retrieval.

    Pass true for defaults or an options object. Omission never starts Kernel
    browser work; provider-supplied content is still returned when available,
    including when requested through native options. Both inline and deferred
    retrieval use the same options schema.
    """

    country: str
    """ISO 3166-1 alpha-2 search locale preference."""

    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Inclusive publication-date upper bound; must not precede start_date.

    If recency is also supplied, recency takes precedence with a warning.
    Unsupported or approximated filtering is reported, or rejected under
    strict_params.
    """

    exclude_domains: SequenceNotStr[str]
    """
    Hostname exclusions, with the same best-effort/strict behavior as
    include_domains. Provider-specific combinations that cannot be represented are
    reported via warnings or rejected in strict mode.
    """

    include_domains: SequenceNotStr[str]
    """Hostname inclusion preference, matching a hostname and its subdomains.

    Empty means unrestricted. Translated, emulated, or dropped with a warning
    according to provider capability unless strict_params is true. Native boost
    modes remain advisory and are identified in warnings.
    """

    include_raw: bool
    """
    Include untouched per-result payloads and the full serving-provider response in
    raw fields. Off by default; native top-level outputs such as answer remain
    available without it.
    """

    language: str
    """BCP 47 search language preference."""

    max_results: int
    """Requested result count from 1 through 100.

    The effective count is clamped to the serving provider's cap with a warning.
    Effective native counts are the lower of this limit and supplied provider-native
    count aliases. Strict mode rejects unsupported counts.
    """

    recency: Literal["hour", "day", "week", "month", "year"]
    """Relative search window.

    Takes precedence over start_date/end_date with a warning if both are set.
    Provider-native recency behavior is retained, including documented hour-to-day
    widening. Unsupported filters are rejected only in strict mode.
    """

    safe_search: Literal["off", "moderate", "strict"]
    """Optional safety preference.

    Omit to use provider defaults. Unsupported values are dropped with a warning
    unless strict_params is true. A search filter is not an authorization boundary.
    """

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Inclusive publication-date lower bound.

    If recency is also supplied, recency takes precedence with a warning. Provider
    date semantics, precision, and unsupported filters are reported; unknown source
    dates are not fabricated or universally post-filtered.
    """

    strategy: StrategyParam
    """Omitted strategy defaults to auto."""

    strict_params: bool
    """
    When false, unsupported portable parameters are omitted and approximations are
    described in warnings. When true, every supplied portable parameter must be
    honored exactly. Requests that cannot be served with those parameters are
    rejected. This does not guarantee identical rankings or document timestamps
    across indexes. Authentication and project isolation are always enforced.
    """

    timeout_ms: int
    """
    Overall deadline across search attempts and inline retrieval. No new attempt
    starts after the deadline. Completed search results survive inline retrieval
    timeouts.
    """


class ContentSearchContentOptionsBrowser(TypedDict, total=False):
    """Requires source=auto or source=browser in deferred retrieval."""

    browser_id: str
    """Existing browser session ID authorized for the caller and selected project.

    Reuses its cookies, proxy, and browser configuration; requests follow that
    browser's existing network access behavior, with no additional destination
    allowlist in this endpoint. Kernel does not delete a caller-supplied browser.
    Render mode uses a temporary tab; website activity may still change shared
    cookies and storage. When omitted and any result needs browser retrieval, Kernel
    creates one temporary browser for the request using the dashboard launch
    defaults (headful, stealth, default proxy), tags it with search_id, and deletes
    it when the request finishes. It is billed and counts toward browser concurrency
    like any other browser. A concurrency rejection returns 429 for source=browser;
    for source=auto, results with retained content are still returned and the rest
    report the rejection.
    """

    mode: Literal["curl", "render"]
    """Curl uses the browser HTTP stack without navigation or JavaScript execution.

    Render navigates a temporary page and extracts from its DOM. The selected mode
    is used for the retrieval.
    """


class ContentSearchContentOptions(TypedDict, total=False):
    browser: ContentSearchContentOptionsBrowser
    """Requires source=auto or source=browser in deferred retrieval."""

    format: Literal["markdown", "text"]

    max_age_hours: int
    """
    For source=auto, maximum acceptable age of retained provider content, measured
    from when the search received it from the provider. A value of 0 disables reuse
    of retained content, so every result is fetched through a browser.
    source=provider reuses retained provider content without freshness validation.
    source=browser always fetches through a browser and does not use this age limit.
    """

    max_chars: int
    """Per-result Unicode character limit after extraction.

    Retained provider content cannot exceed what was stored at search time; such
    results report truncated when the stored text was already truncated.
    """

    source: Literal["auto", "provider", "browser"]
    """
    auto uses retained provider content within max_age_hours; for deferred retrieval
    it falls back to a Kernel browser (caller-supplied or temporary) for results
    without it. Inline retrieval never uses a browser. provider reuses retained
    provider content when available, without freshness validation, and never
    provisions a browser. browser fetches each URL through a Kernel browser, either
    caller-supplied or temporary. No option makes a new provider request. Defaults
    to auto for both inline and deferred retrieval. Missing documents produce
    per-result unavailable outcomes, not request failures.
    """

    timeout_ms: int
    """Per-result deadline including capacity acquisition, retrieval, and extraction.

    Also bounded by the overall request deadline.
    """


Content: TypeAlias = Union[Literal[True], ContentSearchContentOptions]
