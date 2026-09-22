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


class Content(TypedDict, total=False):
    """Defaults to source:auto when omitted."""

    browser: ContentBrowser
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
