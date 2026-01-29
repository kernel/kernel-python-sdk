# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    browser_pool_create_params,
    browser_pool_delete_params,
    browser_pool_update_params,
    browser_pool_acquire_params,
    browser_pool_release_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.browser_pool import BrowserPool
from ..types.browser_pool_list_response import BrowserPoolListResponse
from ..types.browser_pool_acquire_response import BrowserPoolAcquireResponse
from ..types.shared_params.browser_profile import BrowserProfile
from ..types.shared_params.browser_viewport import BrowserViewport
from ..types.shared_params.browser_extension import BrowserExtension

__all__ = ["BrowserPoolsResource", "AsyncBrowserPoolsResource"]


class BrowserPoolsResource(SyncAPIResource):
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
        extensions: Iterable[BrowserExtension] | Omit = omit,
        fill_rate_per_minute: int | Omit = omit,
        headless: bool | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        name: str | Omit = omit,
        profile: BrowserProfile | Omit = omit,
        proxy_id: str | Omit = omit,
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
        """
        Create a new browser pool with the specified configuration and size.

        Args:
          size: Number of browsers to maintain in the pool. The maximum size is determined by
              your organization's pooled sessions limit (the sum of all pool sizes cannot
              exceed your limit).

          extensions: List of browser extensions to load into the session. Provide each by id or name.

          fill_rate_per_minute: Percentage of the pool to fill per minute. Defaults to 10%.

          headless: If true, launches the browser using a headless image. Defaults to false.

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          name: Optional name for the browser pool. Must be unique within the organization.

          profile: Profile selection for the browser session. Provide either id or name. If
              specified, the matching profile will be loaded into the browser session.
              Profiles must be created beforehand.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy
              belonging to the caller's org.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: Default idle timeout in seconds for browsers acquired from this pool before they
              are destroyed. Defaults to 600 seconds if not specified

          viewport: Initial browser window size in pixels with optional refresh rate. If omitted,
              image defaults apply (1920x1080@25). Only specific viewport configurations are
              supported. The server will reject unsupported combinations. Supported
              resolutions are: 2560x1440@10, 1920x1080@25, 1920x1200@25, 1440x900@25,
              1280x800@60, 1024x768@60, 1200x800@60 If refresh_rate is not provided, it will
              be automatically determined from the width and height if they match a supported
              configuration exactly. Note: Higher resolutions may affect the responsiveness of
              live view browser

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
                    "extensions": extensions,
                    "fill_rate_per_minute": fill_rate_per_minute,
                    "headless": headless,
                    "kiosk_mode": kiosk_mode,
                    "name": name,
                    "profile": profile,
                    "proxy_id": proxy_id,
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
            f"/browser_pools/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPool,
        )

    def update(
        self,
        id_or_name: str,
        *,
        size: int,
        discard_all_idle: bool | Omit = omit,
        extensions: Iterable[BrowserExtension] | Omit = omit,
        fill_rate_per_minute: int | Omit = omit,
        headless: bool | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        name: str | Omit = omit,
        profile: BrowserProfile | Omit = omit,
        proxy_id: str | Omit = omit,
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
        """
        Updates the configuration used to create browsers in the pool.

        Args:
          size: Number of browsers to maintain in the pool. The maximum size is determined by
              your organization's pooled sessions limit (the sum of all pool sizes cannot
              exceed your limit).

          discard_all_idle: Whether to discard all idle browsers and rebuild the pool immediately. Defaults
              to false.

          extensions: List of browser extensions to load into the session. Provide each by id or name.

          fill_rate_per_minute: Percentage of the pool to fill per minute. Defaults to 10%.

          headless: If true, launches the browser using a headless image. Defaults to false.

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          name: Optional name for the browser pool. Must be unique within the organization.

          profile: Profile selection for the browser session. Provide either id or name. If
              specified, the matching profile will be loaded into the browser session.
              Profiles must be created beforehand.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy
              belonging to the caller's org.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: Default idle timeout in seconds for browsers acquired from this pool before they
              are destroyed. Defaults to 600 seconds if not specified

          viewport: Initial browser window size in pixels with optional refresh rate. If omitted,
              image defaults apply (1920x1080@25). Only specific viewport configurations are
              supported. The server will reject unsupported combinations. Supported
              resolutions are: 2560x1440@10, 1920x1080@25, 1920x1200@25, 1440x900@25,
              1280x800@60, 1024x768@60, 1200x800@60 If refresh_rate is not provided, it will
              be automatically determined from the width and height if they match a supported
              configuration exactly. Note: Higher resolutions may affect the responsiveness of
              live view browser

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._patch(
            f"/browser_pools/{id_or_name}",
            body=maybe_transform(
                {
                    "size": size,
                    "discard_all_idle": discard_all_idle,
                    "extensions": extensions,
                    "fill_rate_per_minute": fill_rate_per_minute,
                    "headless": headless,
                    "kiosk_mode": kiosk_mode,
                    "name": name,
                    "profile": profile,
                    "proxy_id": proxy_id,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPoolListResponse:
        """List browser pools owned by the caller's organization."""
        return self._get(
            "/browser_pools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPoolListResponse,
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
            f"/browser_pools/{id_or_name}",
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return self._post(
            f"/browser_pools/{id_or_name}/acquire",
            body=maybe_transform(
                {"acquire_timeout_seconds": acquire_timeout_seconds},
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
            f"/browser_pools/{id_or_name}/flush",
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
            f"/browser_pools/{id_or_name}/release",
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
        extensions: Iterable[BrowserExtension] | Omit = omit,
        fill_rate_per_minute: int | Omit = omit,
        headless: bool | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        name: str | Omit = omit,
        profile: BrowserProfile | Omit = omit,
        proxy_id: str | Omit = omit,
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
        """
        Create a new browser pool with the specified configuration and size.

        Args:
          size: Number of browsers to maintain in the pool. The maximum size is determined by
              your organization's pooled sessions limit (the sum of all pool sizes cannot
              exceed your limit).

          extensions: List of browser extensions to load into the session. Provide each by id or name.

          fill_rate_per_minute: Percentage of the pool to fill per minute. Defaults to 10%.

          headless: If true, launches the browser using a headless image. Defaults to false.

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          name: Optional name for the browser pool. Must be unique within the organization.

          profile: Profile selection for the browser session. Provide either id or name. If
              specified, the matching profile will be loaded into the browser session.
              Profiles must be created beforehand.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy
              belonging to the caller's org.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: Default idle timeout in seconds for browsers acquired from this pool before they
              are destroyed. Defaults to 600 seconds if not specified

          viewport: Initial browser window size in pixels with optional refresh rate. If omitted,
              image defaults apply (1920x1080@25). Only specific viewport configurations are
              supported. The server will reject unsupported combinations. Supported
              resolutions are: 2560x1440@10, 1920x1080@25, 1920x1200@25, 1440x900@25,
              1280x800@60, 1024x768@60, 1200x800@60 If refresh_rate is not provided, it will
              be automatically determined from the width and height if they match a supported
              configuration exactly. Note: Higher resolutions may affect the responsiveness of
              live view browser

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
                    "extensions": extensions,
                    "fill_rate_per_minute": fill_rate_per_minute,
                    "headless": headless,
                    "kiosk_mode": kiosk_mode,
                    "name": name,
                    "profile": profile,
                    "proxy_id": proxy_id,
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
            f"/browser_pools/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPool,
        )

    async def update(
        self,
        id_or_name: str,
        *,
        size: int,
        discard_all_idle: bool | Omit = omit,
        extensions: Iterable[BrowserExtension] | Omit = omit,
        fill_rate_per_minute: int | Omit = omit,
        headless: bool | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        name: str | Omit = omit,
        profile: BrowserProfile | Omit = omit,
        proxy_id: str | Omit = omit,
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
        """
        Updates the configuration used to create browsers in the pool.

        Args:
          size: Number of browsers to maintain in the pool. The maximum size is determined by
              your organization's pooled sessions limit (the sum of all pool sizes cannot
              exceed your limit).

          discard_all_idle: Whether to discard all idle browsers and rebuild the pool immediately. Defaults
              to false.

          extensions: List of browser extensions to load into the session. Provide each by id or name.

          fill_rate_per_minute: Percentage of the pool to fill per minute. Defaults to 10%.

          headless: If true, launches the browser using a headless image. Defaults to false.

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          name: Optional name for the browser pool. Must be unique within the organization.

          profile: Profile selection for the browser session. Provide either id or name. If
              specified, the matching profile will be loaded into the browser session.
              Profiles must be created beforehand.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy
              belonging to the caller's org.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: Default idle timeout in seconds for browsers acquired from this pool before they
              are destroyed. Defaults to 600 seconds if not specified

          viewport: Initial browser window size in pixels with optional refresh rate. If omitted,
              image defaults apply (1920x1080@25). Only specific viewport configurations are
              supported. The server will reject unsupported combinations. Supported
              resolutions are: 2560x1440@10, 1920x1080@25, 1920x1200@25, 1440x900@25,
              1280x800@60, 1024x768@60, 1200x800@60 If refresh_rate is not provided, it will
              be automatically determined from the width and height if they match a supported
              configuration exactly. Note: Higher resolutions may affect the responsiveness of
              live view browser

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._patch(
            f"/browser_pools/{id_or_name}",
            body=await async_maybe_transform(
                {
                    "size": size,
                    "discard_all_idle": discard_all_idle,
                    "extensions": extensions,
                    "fill_rate_per_minute": fill_rate_per_minute,
                    "headless": headless,
                    "kiosk_mode": kiosk_mode,
                    "name": name,
                    "profile": profile,
                    "proxy_id": proxy_id,
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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserPoolListResponse:
        """List browser pools owned by the caller's organization."""
        return await self._get(
            "/browser_pools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserPoolListResponse,
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
            f"/browser_pools/{id_or_name}",
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        return await self._post(
            f"/browser_pools/{id_or_name}/acquire",
            body=await async_maybe_transform(
                {"acquire_timeout_seconds": acquire_timeout_seconds},
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
            f"/browser_pools/{id_or_name}/flush",
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
            f"/browser_pools/{id_or_name}/release",
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
