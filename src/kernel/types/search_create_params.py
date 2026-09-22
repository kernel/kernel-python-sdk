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
    """Invalid with source=provider.

    Supplying browser_id requires
    source=browser so the chosen identity is not bypassed.
    """

    browser_id: str
    """Existing browser session ID authorized for the caller and selected project.

    Reuses its cookies, proxy, and browser configuration. Kernel does not delete a
    caller-supplied browser. Render mode uses a temporary tab; website activity may
    still change shared cookies and storage. When omitted, Kernel obtains isolated
    browser capacity in the caller's account and releases it after retrieval. That
    capacity is not retained for later interaction. Existing browser quotas apply.
    """

    mode: Literal["curl", "render"]
    """Curl uses the browser HTTP stack without navigation or JavaScript execution.

    Render navigates a temporary page and extracts from its DOM. The selected mode
    is used for the retrieval.
    """


class ContentSearchContentOptions(TypedDict, total=False):
    browser: ContentSearchContentOptionsBrowser
    """Invalid with source=provider.

    Supplying browser_id requires source=browser so the chosen identity is not
    bypassed.
    """

    format: Literal["markdown", "text"]

    max_age_hours: int
    """Maximum acceptable age of cached page content, measured from origin retrieval.

    0 forces a live fetch. Governs the Kernel content cache, which is scoped to the
    caller organization and project and separated by retrieval context; fetches
    through a caller-supplied browser_id bypass that cache. Mapped to the provider
    freshness control when source is provider and the provider supports one;
    otherwise provider content age is reported as unknown via fetched_at.
    """

    max_chars: int
    """Per-result Unicode character limit after extraction."""

    source: Literal["auto", "provider", "browser"]
    """
    provider uses the search provider's native content retrieval; browser fetches
    each URL through a Kernel browser; auto prefers Kernel browser retrieval and
    falls back to provider-native content when browser retrieval is unavailable or
    unsuitable. Defaults to auto for both inline and deferred retrieval. Deferred
    provider retrieval requires post_hoc capability; an explicit provider source
    without it is a 400. Missing documents produce per-result unavailable outcomes,
    not request failures.
    """

    timeout_ms: int
    """Per-result deadline including capacity acquisition, retrieval, and extraction.

    Also bounded by the overall request deadline.
    """


Content: TypeAlias = Union[Literal[True], ContentSearchContentOptions]
