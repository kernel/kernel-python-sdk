# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import (
    browser_pool_list_params,
    browser_pool_create_params,
    browser_pool_delete_params,
    browser_pool_update_params,
    browser_pool_acquire_params,
    browser_pool_release_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.tags_param import TagsParam
from ..types.browser_pool import BrowserPool
from ..types.browser_pool_acquire_response import BrowserPoolAcquireResponse
from ..types.shared_params.browser_viewport import BrowserViewport
from ..types.shared_params.browser_extension import BrowserExtension

__all__ = ["BrowserPoolsResource", "AsyncBrowserPoolsResource"]


class BrowserPoolsResource(SyncAPIResource):
    """Create and manage browser pools for acquiring and releasing browsers."""

    @cached_property
    def with_raw_response(self) -> BrowserPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrowserPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return BrowserPoolsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        size: int,
        chrome_policy: Dict[str, object] | Omit = omit,
        extensions: Iterable[BrowserExtension] | Omit = omit,
        fill_rate_per_minute: int | Omit = omit,
        headless: bool | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        name: str | Omit = omit,
        profile: browser_pool_create_params.Profile | Omit = omit,
        proxy_id: str | Omit = omit,
        start_url: str | Omit = omit,
        stealth: bool | Omit = omit,
        timeout_seconds: int | Omit = omit,
        viewport: BrowserViewport | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPool:
        """Create a new browser pool with the specified configuration and size.

        Pooled
        browsers load their profile read-only: any save_changes on the profile is
        ignored (not rejected), so pooled browsers never persist changes back to the
        profile.

        Args:
          size: Number of browsers to maintain in the pool. The maximum size is determined by
              your organization's pooled sessions limit (the sum of all pool sizes cannot
              exceed your limit).

          chrome_policy: Custom Chrome enterprise policy overrides applied to all browsers in this pool.
              Keys are Chrome enterprise policy names; values must match their expected types.
              Blocked: kernel-managed policies (extensions, proxy, CDP/automation). See
              https://chromeenterprise.google/policies/

          extensions: List of browser extensions to load into the session. Provide each by id or name.

          fill_rate_per_minute: Percentage of the pool to fill per minute. Defaults to 10. The cap is 25 for
              most organizations but can be raised per-organization, so only the lower bound
              is enforced here.

          headless: If true, launches the browser using a headless image. Defaults to false.

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          name: Optional name for the browser pool. Must be unique within the project.

          profile: Profile selection for browsers in a pool. Provide either id or name. The
              matching profile is loaded into every browser in the pool. Profiles must be
              created beforehand. Unlike single browser sessions, pools load the profile
              read-only and never persist changes back to it, so save_changes is omitted here.
              Any save_changes value sent on a pool profile is silently ignored rather than
              rejected, so callers reusing a single-session profile object will not error.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy in
              the same project as the browser session.

          start_url: Optional URL to navigate to when a new browser is warmed into the pool.
              Best-effort: failures to navigate do not fail pool fill. Only applied to
              newly-warmed browsers; browsers reused via release/acquire keep whatever URL the
              previous lease left them on. Accepts any URL Chromium can resolve, including
              chrome:// pages.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: Default idle timeout in seconds for browsers acquired from this pool before they
              are destroyed. Defaults to 600 seconds. Minimum 10, maximum 259200 (72 hours).

          viewport: Initial browser window size in pixels with optional refresh rate. If omitted,
              image defaults apply (1920x1080@25). For GPU images, the default is
              1920x1080@60. Arbitrary viewport dimensions and refresh rates are accepted.
              Known-good presets include: 2560x1440@10, 1920x1080@25, 1920x1200@25,
              1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60, 768x1024@60, 390x844@60. For
              GPU images, recommended presets use one of these resolutions with refresh rates
              60, 30, 25, or 10: 800x600, 960x720, 1024x576, 1024x768, 1152x648, 1200x800,
              1280x720, 1368x768, 1440x900, 1600x900, 1920x1080, 1920x1200, 390x844, 360x250,
              768x1024, 800x1600. Viewports outside this list may exhibit unstable live view
              or recording behavior. If refresh_rate is not provided, it will be automatically
              determined based on the resolution (higher resolutions use lower refresh rates
              to keep bandwidth reasonable).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/browser_pools",
            body=maybe_transform(
                {
                    "size": size,
                    "chrome_policy": chrome_policy,
                    "extensions": extensions,
                    "fill_rate_per_minute": fill_rate_per_minute,
                    "headless": headless,
                    "kiosk_mode": kiosk_mode,
                    "name": name,
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "start_url": start_url,
                    "stealth": stealth,
                    "timeout_seconds": timeout_seconds,
                    "viewport": viewport,
                },
                browser_pool_create_params.BrowserPoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPool,
        )

    def retrieve(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPool:
        """
        Retrieve details for a single browser pool by its ID or name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._get(
            path_template("/browser_pools/{id_or_name}", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPool,
        )

    def update(
        self,
        id_or_name: str,
        *,
        chrome_policy: Dict[str, object] | Omit = omit,
        discard_all_idle: bool | Omit = omit,
        extensions: Iterable[BrowserExtension] | Omit = omit,
        fill_rate_per_minute: int | Omit = omit,
        headless: bool | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        name: str | Omit = omit,
        profile: browser_pool_update_params.Profile | Omit = omit,
        proxy_id: str | Omit = omit,
        size: int | Omit = omit,
        start_url: str | Omit = omit,
        stealth: bool | Omit = omit,
        timeout_seconds: int | Omit = omit,
        viewport: BrowserViewport | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPool:
        """Updates the configuration used to create browsers in the pool.

        As with creation,
        save_changes on the pool profile is ignored (not rejected); pooled browsers
        never persist changes back to the profile.

        Args:
          chrome_policy: Custom Chrome enterprise policy overrides applied to all browsers in this pool.
              Keys are Chrome enterprise policy names; values must match their expected types.
              Blocked: kernel-managed policies (extensions, proxy, CDP/automation). See
              https://chromeenterprise.google/policies/

          discard_all_idle: Whether to discard all idle browsers and rebuild the pool immediately. Defaults
              to false.

          extensions: List of browser extensions to load into the session. Provide each by id or name.

          fill_rate_per_minute: Percentage of the pool to fill per minute. Defaults to 10. The cap is 25 for
              most organizations but can be raised per-organization, so only the lower bound
              is enforced here.

          headless: If true, launches the browser using a headless image. Defaults to false.

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          name: Optional name for the browser pool. Must be unique within the project.

          profile: Profile selection for browsers in a pool. Provide either id or name. The
              matching profile is loaded into every browser in the pool. Profiles must be
              created beforehand. Unlike single browser sessions, pools load the profile
              read-only and never persist changes back to it, so save_changes is omitted here.
              Any save_changes value sent on a pool profile is silently ignored rather than
              rejected, so callers reusing a single-session profile object will not error.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy in
              the same project as the browser session.

          size: Number of browsers to maintain in the pool. The maximum size is determined by
              your organization's pooled sessions limit (the sum of all pool sizes cannot
              exceed your limit).

          start_url: Optional URL to navigate to when a new browser is warmed into the pool.
              Best-effort: failures to navigate do not fail pool fill. Only applied to
              newly-warmed browsers; browsers reused via release/acquire keep whatever URL the
              previous lease left them on. Accepts any URL Chromium can resolve, including
              chrome:// pages.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: Default idle timeout in seconds for browsers acquired from this pool before they
              are destroyed. Defaults to 600 seconds. Minimum 10, maximum 259200 (72 hours).

          viewport: Initial browser window size in pixels with optional refresh rate. If omitted,
              image defaults apply (1920x1080@25). For GPU images, the default is
              1920x1080@60. Arbitrary viewport dimensions and refresh rates are accepted.
              Known-good presets include: 2560x1440@10, 1920x1080@25, 1920x1200@25,
              1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60, 768x1024@60, 390x844@60. For
              GPU images, recommended presets use one of these resolutions with refresh rates
              60, 30, 25, or 10: 800x600, 960x720, 1024x576, 1024x768, 1152x648, 1200x800,
              1280x720, 1368x768, 1440x900, 1600x900, 1920x1080, 1920x1200, 390x844, 360x250,
              768x1024, 800x1600. Viewports outside this list may exhibit unstable live view
              or recording behavior. If refresh_rate is not provided, it will be automatically
              determined based on the resolution (higher resolutions use lower refresh rates
              to keep bandwidth reasonable).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._patch(
            path_template("/browser_pools/{id_or_name}", id_or_name=id_or_name),
            body=maybe_transform(
                {
                    "chrome_policy": chrome_policy,
                    "discard_all_idle": discard_all_idle,
                    "extensions": extensions,
                    "fill_rate_per_minute": fill_rate_per_minute,
                    "headless": headless,
                    "kiosk_mode": kiosk_mode,
                    "name": name,
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "size": size,
                    "start_url": start_url,
                    "stealth": stealth,
                    "timeout_seconds": timeout_seconds,
                    "viewport": viewport,
                },
                browser_pool_update_params.BrowserPoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPool,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[BrowserPool]:
        """
        List browser pools in the resolved project.

        Args:
          limit: Limit the number of browser pools to return.

          offset: Offset the number of browser pools to return.

          query: Search browser pools by name or ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/browser_pools",
            page=SyncOffsetPagination[BrowserPool],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                    },
                    browser_pool_list_params.BrowserPoolListParams,
                ),
            ),
            model=BrowserPool,
        )

    def delete(
        self,
        id_or_name: str,
        *,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a browser pool and all browsers in it.

        By default, deletion is blocked if
        browsers are currently leased. Use force=true to terminate leased browsers.

        Args:
          force: If true, force delete even if browsers are currently leased. Leased browsers
              will be terminated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/browser_pools/{id_or_name}", id_or_name=id_or_name),
            body=maybe_transform({"force": force}, browser_pool_delete_params.BrowserPoolDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def acquire(
        self,
        id_or_name: str,
        *,
        acquire_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        start_url: str | Omit = omit,
        tags: TagsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPoolAcquireResponse:
        """Long-polling endpoint to acquire a browser from the pool.

        Returns immediately
        when a browser is available, or returns 204 No Content when the poll times out.
        The client should retry the request to continue waiting for a browser. The
        acquired browser will use the pool's timeout_seconds for its idle timeout.

        Args:
          acquire_timeout_seconds: Maximum number of seconds to wait for a browser to be available. Defaults to the
              calculated time it would take to fill the pool at the currently configured fill
              rate.

          name: Optional human-readable name for the acquired browser session, used to find it
              later in the dashboard. Must be unique among active sessions within the pool's
              project. Applies to this lease only and is cleared when the browser is released
              back to the pool.

          start_url: Optional URL to navigate the acquired browser to. Overrides the pool's start_url
              for this acquire only. Best-effort: failures to navigate do not fail the
              acquire.

          tags: Optional user-defined key-value tags for the acquired browser session, used to
              find and group sessions later. Applies to this lease only and are cleared when
              the browser is released back to the pool. Up to 50 pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._post(
            path_template("/browser_pools/{id_or_name}/acquire", id_or_name=id_or_name),
            body=maybe_transform(
                {
                    "acquire_timeout_seconds": acquire_timeout_seconds,
                    "name": name,
                    "start_url": start_url,
                    "tags": tags,
                },
                browser_pool_acquire_params.BrowserPoolAcquireParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPoolAcquireResponse,
        )

    def flush(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Destroys all idle browsers in the pool; leased browsers are not affected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/browser_pools/{id_or_name}/flush", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def release(
        self,
        id_or_name: str,
        *,
        session_id: str,
        reuse: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Release a browser back to the pool, optionally recreating the browser instance.

        Args:
          session_id: Browser session ID to release back to the pool

          reuse: Whether to reuse the browser instance or destroy it and create a new one.
              Defaults to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/browser_pools/{id_or_name}/release", id_or_name=id_or_name),
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "reuse": reuse,
                },
                browser_pool_release_params.BrowserPoolReleaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBrowserPoolsResource(AsyncAPIResource):
    """Create and manage browser pools for acquiring and releasing browsers."""

    @cached_property
    def with_raw_response(self) -> AsyncBrowserPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncBrowserPoolsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        size: int,
        chrome_policy: Dict[str, object] | Omit = omit,
        extensions: Iterable[BrowserExtension] | Omit = omit,
        fill_rate_per_minute: int | Omit = omit,
        headless: bool | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        name: str | Omit = omit,
        profile: browser_pool_create_params.Profile | Omit = omit,
        proxy_id: str | Omit = omit,
        start_url: str | Omit = omit,
        stealth: bool | Omit = omit,
        timeout_seconds: int | Omit = omit,
        viewport: BrowserViewport | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPool:
        """Create a new browser pool with the specified configuration and size.

        Pooled
        browsers load their profile read-only: any save_changes on the profile is
        ignored (not rejected), so pooled browsers never persist changes back to the
        profile.

        Args:
          size: Number of browsers to maintain in the pool. The maximum size is determined by
              your organization's pooled sessions limit (the sum of all pool sizes cannot
              exceed your limit).

          chrome_policy: Custom Chrome enterprise policy overrides applied to all browsers in this pool.
              Keys are Chrome enterprise policy names; values must match their expected types.
              Blocked: kernel-managed policies (extensions, proxy, CDP/automation). See
              https://chromeenterprise.google/policies/

          extensions: List of browser extensions to load into the session. Provide each by id or name.

          fill_rate_per_minute: Percentage of the pool to fill per minute. Defaults to 10. The cap is 25 for
              most organizations but can be raised per-organization, so only the lower bound
              is enforced here.

          headless: If true, launches the browser using a headless image. Defaults to false.

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          name: Optional name for the browser pool. Must be unique within the project.

          profile: Profile selection for browsers in a pool. Provide either id or name. The
              matching profile is loaded into every browser in the pool. Profiles must be
              created beforehand. Unlike single browser sessions, pools load the profile
              read-only and never persist changes back to it, so save_changes is omitted here.
              Any save_changes value sent on a pool profile is silently ignored rather than
              rejected, so callers reusing a single-session profile object will not error.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy in
              the same project as the browser session.

          start_url: Optional URL to navigate to when a new browser is warmed into the pool.
              Best-effort: failures to navigate do not fail pool fill. Only applied to
              newly-warmed browsers; browsers reused via release/acquire keep whatever URL the
              previous lease left them on. Accepts any URL Chromium can resolve, including
              chrome:// pages.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: Default idle timeout in seconds for browsers acquired from this pool before they
              are destroyed. Defaults to 600 seconds. Minimum 10, maximum 259200 (72 hours).

          viewport: Initial browser window size in pixels with optional refresh rate. If omitted,
              image defaults apply (1920x1080@25). For GPU images, the default is
              1920x1080@60. Arbitrary viewport dimensions and refresh rates are accepted.
              Known-good presets include: 2560x1440@10, 1920x1080@25, 1920x1200@25,
              1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60, 768x1024@60, 390x844@60. For
              GPU images, recommended presets use one of these resolutions with refresh rates
              60, 30, 25, or 10: 800x600, 960x720, 1024x576, 1024x768, 1152x648, 1200x800,
              1280x720, 1368x768, 1440x900, 1600x900, 1920x1080, 1920x1200, 390x844, 360x250,
              768x1024, 800x1600. Viewports outside this list may exhibit unstable live view
              or recording behavior. If refresh_rate is not provided, it will be automatically
              determined based on the resolution (higher resolutions use lower refresh rates
              to keep bandwidth reasonable).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/browser_pools",
            body=await async_maybe_transform(
                {
                    "size": size,
                    "chrome_policy": chrome_policy,
                    "extensions": extensions,
                    "fill_rate_per_minute": fill_rate_per_minute,
                    "headless": headless,
                    "kiosk_mode": kiosk_mode,
                    "name": name,
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "start_url": start_url,
                    "stealth": stealth,
                    "timeout_seconds": timeout_seconds,
                    "viewport": viewport,
                },
                browser_pool_create_params.BrowserPoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPool,
        )

    async def retrieve(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPool:
        """
        Retrieve details for a single browser pool by its ID or name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._get(
            path_template("/browser_pools/{id_or_name}", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPool,
        )

    async def update(
        self,
        id_or_name: str,
        *,
        chrome_policy: Dict[str, object] | Omit = omit,
        discard_all_idle: bool | Omit = omit,
        extensions: Iterable[BrowserExtension] | Omit = omit,
        fill_rate_per_minute: int | Omit = omit,
        headless: bool | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        name: str | Omit = omit,
        profile: browser_pool_update_params.Profile | Omit = omit,
        proxy_id: str | Omit = omit,
        size: int | Omit = omit,
        start_url: str | Omit = omit,
        stealth: bool | Omit = omit,
        timeout_seconds: int | Omit = omit,
        viewport: BrowserViewport | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPool:
        """Updates the configuration used to create browsers in the pool.

        As with creation,
        save_changes on the pool profile is ignored (not rejected); pooled browsers
        never persist changes back to the profile.

        Args:
          chrome_policy: Custom Chrome enterprise policy overrides applied to all browsers in this pool.
              Keys are Chrome enterprise policy names; values must match their expected types.
              Blocked: kernel-managed policies (extensions, proxy, CDP/automation). See
              https://chromeenterprise.google/policies/

          discard_all_idle: Whether to discard all idle browsers and rebuild the pool immediately. Defaults
              to false.

          extensions: List of browser extensions to load into the session. Provide each by id or name.

          fill_rate_per_minute: Percentage of the pool to fill per minute. Defaults to 10. The cap is 25 for
              most organizations but can be raised per-organization, so only the lower bound
              is enforced here.

          headless: If true, launches the browser using a headless image. Defaults to false.

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          name: Optional name for the browser pool. Must be unique within the project.

          profile: Profile selection for browsers in a pool. Provide either id or name. The
              matching profile is loaded into every browser in the pool. Profiles must be
              created beforehand. Unlike single browser sessions, pools load the profile
              read-only and never persist changes back to it, so save_changes is omitted here.
              Any save_changes value sent on a pool profile is silently ignored rather than
              rejected, so callers reusing a single-session profile object will not error.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy in
              the same project as the browser session.

          size: Number of browsers to maintain in the pool. The maximum size is determined by
              your organization's pooled sessions limit (the sum of all pool sizes cannot
              exceed your limit).

          start_url: Optional URL to navigate to when a new browser is warmed into the pool.
              Best-effort: failures to navigate do not fail pool fill. Only applied to
              newly-warmed browsers; browsers reused via release/acquire keep whatever URL the
              previous lease left them on. Accepts any URL Chromium can resolve, including
              chrome:// pages.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: Default idle timeout in seconds for browsers acquired from this pool before they
              are destroyed. Defaults to 600 seconds. Minimum 10, maximum 259200 (72 hours).

          viewport: Initial browser window size in pixels with optional refresh rate. If omitted,
              image defaults apply (1920x1080@25). For GPU images, the default is
              1920x1080@60. Arbitrary viewport dimensions and refresh rates are accepted.
              Known-good presets include: 2560x1440@10, 1920x1080@25, 1920x1200@25,
              1440x900@25, 1280x800@60, 1024x768@60, 1200x800@60, 768x1024@60, 390x844@60. For
              GPU images, recommended presets use one of these resolutions with refresh rates
              60, 30, 25, or 10: 800x600, 960x720, 1024x576, 1024x768, 1152x648, 1200x800,
              1280x720, 1368x768, 1440x900, 1600x900, 1920x1080, 1920x1200, 390x844, 360x250,
              768x1024, 800x1600. Viewports outside this list may exhibit unstable live view
              or recording behavior. If refresh_rate is not provided, it will be automatically
              determined based on the resolution (higher resolutions use lower refresh rates
              to keep bandwidth reasonable).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._patch(
            path_template("/browser_pools/{id_or_name}", id_or_name=id_or_name),
            body=await async_maybe_transform(
                {
                    "chrome_policy": chrome_policy,
                    "discard_all_idle": discard_all_idle,
                    "extensions": extensions,
                    "fill_rate_per_minute": fill_rate_per_minute,
                    "headless": headless,
                    "kiosk_mode": kiosk_mode,
                    "name": name,
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "size": size,
                    "start_url": start_url,
                    "stealth": stealth,
                    "timeout_seconds": timeout_seconds,
                    "viewport": viewport,
                },
                browser_pool_update_params.BrowserPoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPool,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BrowserPool, AsyncOffsetPagination[BrowserPool]]:
        """
        List browser pools in the resolved project.

        Args:
          limit: Limit the number of browser pools to return.

          offset: Offset the number of browser pools to return.

          query: Search browser pools by name or ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/browser_pools",
            page=AsyncOffsetPagination[BrowserPool],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                    },
                    browser_pool_list_params.BrowserPoolListParams,
                ),
            ),
            model=BrowserPool,
        )

    async def delete(
        self,
        id_or_name: str,
        *,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a browser pool and all browsers in it.

        By default, deletion is blocked if
        browsers are currently leased. Use force=true to terminate leased browsers.

        Args:
          force: If true, force delete even if browsers are currently leased. Leased browsers
              will be terminated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/browser_pools/{id_or_name}", id_or_name=id_or_name),
            body=await async_maybe_transform({"force": force}, browser_pool_delete_params.BrowserPoolDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def acquire(
        self,
        id_or_name: str,
        *,
        acquire_timeout_seconds: int | Omit = omit,
        name: str | Omit = omit,
        start_url: str | Omit = omit,
        tags: TagsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPoolAcquireResponse:
        """Long-polling endpoint to acquire a browser from the pool.

        Returns immediately
        when a browser is available, or returns 204 No Content when the poll times out.
        The client should retry the request to continue waiting for a browser. The
        acquired browser will use the pool's timeout_seconds for its idle timeout.

        Args:
          acquire_timeout_seconds: Maximum number of seconds to wait for a browser to be available. Defaults to the
              calculated time it would take to fill the pool at the currently configured fill
              rate.

          name: Optional human-readable name for the acquired browser session, used to find it
              later in the dashboard. Must be unique among active sessions within the pool's
              project. Applies to this lease only and is cleared when the browser is released
              back to the pool.

          start_url: Optional URL to navigate the acquired browser to. Overrides the pool's start_url
              for this acquire only. Best-effort: failures to navigate do not fail the
              acquire.

          tags: Optional user-defined key-value tags for the acquired browser session, used to
              find and group sessions later. Applies to this lease only and are cleared when
              the browser is released back to the pool. Up to 50 pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._post(
            path_template("/browser_pools/{id_or_name}/acquire", id_or_name=id_or_name),
            body=await async_maybe_transform(
                {
                    "acquire_timeout_seconds": acquire_timeout_seconds,
                    "name": name,
                    "start_url": start_url,
                    "tags": tags,
                },
                browser_pool_acquire_params.BrowserPoolAcquireParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPoolAcquireResponse,
        )

    async def flush(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Destroys all idle browsers in the pool; leased browsers are not affected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/browser_pools/{id_or_name}/flush", id_or_name=id_or_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def release(
        self,
        id_or_name: str,
        *,
        session_id: str,
        reuse: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Release a browser back to the pool, optionally recreating the browser instance.

        Args:
          session_id: Browser session ID to release back to the pool

          reuse: Whether to reuse the browser instance or destroy it and create a new one.
              Defaults to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/browser_pools/{id_or_name}/release", id_or_name=id_or_name),
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "reuse": reuse,
                },
                browser_pool_release_params.BrowserPoolReleaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BrowserPoolsResourceWithRawResponse:
    def __init__(self, browser_pools: BrowserPoolsResource) -> None:
        self._browser_pools = browser_pools

        self.create = to_raw_response_wrapper(
            browser_pools.create,
        )
        self.retrieve = to_raw_response_wrapper(
            browser_pools.retrieve,
        )
        self.update = to_raw_response_wrapper(
            browser_pools.update,
        )
        self.list = to_raw_response_wrapper(
            browser_pools.list,
        )
        self.delete = to_raw_response_wrapper(
            browser_pools.delete,
        )
        self.acquire = to_raw_response_wrapper(
            browser_pools.acquire,
        )
        self.flush = to_raw_response_wrapper(
            browser_pools.flush,
        )
        self.release = to_raw_response_wrapper(
            browser_pools.release,
        )


class AsyncBrowserPoolsResourceWithRawResponse:
    def __init__(self, browser_pools: AsyncBrowserPoolsResource) -> None:
        self._browser_pools = browser_pools

        self.create = async_to_raw_response_wrapper(
            browser_pools.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            browser_pools.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            browser_pools.update,
        )
        self.list = async_to_raw_response_wrapper(
            browser_pools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            browser_pools.delete,
        )
        self.acquire = async_to_raw_response_wrapper(
            browser_pools.acquire,
        )
        self.flush = async_to_raw_response_wrapper(
            browser_pools.flush,
        )
        self.release = async_to_raw_response_wrapper(
            browser_pools.release,
        )


class BrowserPoolsResourceWithStreamingResponse:
    def __init__(self, browser_pools: BrowserPoolsResource) -> None:
        self._browser_pools = browser_pools

        self.create = to_streamed_response_wrapper(
            browser_pools.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            browser_pools.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            browser_pools.update,
        )
        self.list = to_streamed_response_wrapper(
            browser_pools.list,
        )
        self.delete = to_streamed_response_wrapper(
            browser_pools.delete,
        )
        self.acquire = to_streamed_response_wrapper(
            browser_pools.acquire,
        )
        self.flush = to_streamed_response_wrapper(
            browser_pools.flush,
        )
        self.release = to_streamed_response_wrapper(
            browser_pools.release,
        )


class AsyncBrowserPoolsResourceWithStreamingResponse:
    def __init__(self, browser_pools: AsyncBrowserPoolsResource) -> None:
        self._browser_pools = browser_pools

        self.create = async_to_streamed_response_wrapper(
            browser_pools.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            browser_pools.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            browser_pools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            browser_pools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            browser_pools.delete,
        )
        self.acquire = async_to_streamed_response_wrapper(
            browser_pools.acquire,
        )
        self.flush = async_to_streamed_response_wrapper(
            browser_pools.flush,
        )
        self.release = async_to_streamed_response_wrapper(
            browser_pools.release,
        )
