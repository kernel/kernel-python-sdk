# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ContentFetchParams", "Content", "ContentBrowser"]


class ContentFetchParams(TypedDict, total=False):
    content: Content
    """Defaults to source:auto when omitted."""

    limit: int
    """
    Maximum number of search results to fetch when result_ids is omitted, starting
    from rank 1. Mutually exclusive with result_ids.
    """

    result_ids: SequenceNotStr[str]
    """
    Kernel-generated IDs from the referenced retained search, in desired response
    order. They are not provider-standard IDs. Mutually exclusive with limit.
    """

    timeout_ms: int
    """Overall deadline across all selected results."""


class ContentBrowser(TypedDict, total=False):
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


class Content(TypedDict, total=False):
    """Defaults to source:auto when omitted."""

    browser: ContentBrowser
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
