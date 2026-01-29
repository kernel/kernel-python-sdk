# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Mapping, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from .fs.fs import (
    FsResource,
    AsyncFsResource,
    FsResourceWithRawResponse,
    AsyncFsResourceWithRawResponse,
    FsResourceWithStreamingResponse,
    AsyncFsResourceWithStreamingResponse,
)
from ...types import (
    browser_list_params,
    browser_create_params,
    browser_delete_params,
    browser_update_params,
    browser_retrieve_params,
    browser_load_extensions_params,
)
from .process import (
    ProcessResource,
    AsyncProcessResource,
    ProcessResourceWithRawResponse,
    AsyncProcessResourceWithRawResponse,
    ProcessResourceWithStreamingResponse,
    AsyncProcessResourceWithStreamingResponse,
)
from .replays import (
    ReplaysResource,
    AsyncReplaysResource,
    ReplaysResourceWithRawResponse,
    AsyncReplaysResourceWithRawResponse,
    ReplaysResourceWithStreamingResponse,
    AsyncReplaysResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .computer import (
    ComputerResource,
    AsyncComputerResource,
    ComputerResourceWithRawResponse,
    AsyncComputerResourceWithRawResponse,
    ComputerResourceWithStreamingResponse,
    AsyncComputerResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .playwright import (
    PlaywrightResource,
    AsyncPlaywrightResource,
    PlaywrightResourceWithRawResponse,
    AsyncPlaywrightResourceWithRawResponse,
    PlaywrightResourceWithStreamingResponse,
    AsyncPlaywrightResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPagination, AsyncOffsetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.browser_list_response import BrowserListResponse
from ...types.browser_create_response import BrowserCreateResponse
from ...types.browser_update_response import BrowserUpdateResponse
from ...types.browser_persistence_param import BrowserPersistenceParam
from ...types.browser_retrieve_response import BrowserRetrieveResponse
from ...types.shared_params.browser_profile import BrowserProfile
from ...types.shared_params.browser_viewport import BrowserViewport
from ...types.shared_params.browser_extension import BrowserExtension

__all__ = ["BrowsersResource", "AsyncBrowsersResource"]


class BrowsersResource(SyncAPIResource):
    @cached_property
    def replays(self) -> ReplaysResource:
        return ReplaysResource(self._client)

    @cached_property
    def fs(self) -> FsResource:
        return FsResource(self._client)

    @cached_property
    def process(self) -> ProcessResource:
        return ProcessResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def computer(self) -> ComputerResource:
        return ComputerResource(self._client)

    @cached_property
    def playwright(self) -> PlaywrightResource:
        return PlaywrightResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrowsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return BrowsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        extensions: Iterable[BrowserExtension] | Omit = omit,
        headless: bool | Omit = omit,
        invocation_id: str | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        persistence: BrowserPersistenceParam | Omit = omit,
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
    ) -> BrowserCreateResponse:
        """
        Create a new browser session from within an action.

        Args:
          extensions: List of browser extensions to load into the session. Provide each by id or name.

          headless: If true, launches the browser using a headless image (no VNC/GUI). Defaults to
              false.

          invocation_id: action invocation ID

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          persistence: DEPRECATED: Use timeout_seconds (up to 72 hours) and Profiles instead.

          profile: Profile selection for the browser session. Provide either id or name. If
              specified, the matching profile will be loaded into the browser session.
              Profiles must be created beforehand.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy
              belonging to the caller's org.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: The number of seconds of inactivity before the browser session is terminated.
              Activity includes CDP connections and live view connections. Defaults to 60
              seconds. Minimum allowed is 10 seconds. Maximum allowed is 259200 (72 hours). We
              check for inactivity every 5 seconds, so the actual timeout behavior you will
              see is +/- 5 seconds around the specified value.

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
            "/browsers",
            body=maybe_transform(
                {
                    "extensions": extensions,
                    "headless": headless,
                    "invocation_id": invocation_id,
                    "kiosk_mode": kiosk_mode,
                    "persistence": persistence,
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "stealth": stealth,
                    "timeout_seconds": timeout_seconds,
                    "viewport": viewport,
                },
                browser_create_params.BrowserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserRetrieveResponse:
        """
        Get information about a browser session.

        Args:
          include_deleted: When true, includes soft-deleted browser sessions in the lookup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/browsers/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_deleted": include_deleted}, browser_retrieve_params.BrowserRetrieveParams
                ),
            ),
            cast_to=BrowserRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        profile: BrowserProfile | Omit = omit,
        proxy_id: Optional[str] | Omit = omit,
        viewport: BrowserViewport | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserUpdateResponse:
        """
        Update a browser session.

        Args:
          profile: Profile to load into the browser session. Only allowed if the session does not
              already have a profile loaded.

          proxy_id: ID of the proxy to use. Omit to leave unchanged, set to empty string to remove
              proxy.

          viewport: Viewport configuration to apply to the browser session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/browsers/{id}",
            body=maybe_transform(
                {
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "viewport": viewport,
                },
                browser_update_params.BrowserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserUpdateResponse,
        )

    def list(
        self,
        *,
        include_deleted: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["active", "deleted", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[BrowserListResponse]:
        """List all browser sessions with pagination support.

        Use status parameter to
        filter by session state.

        Args:
          include_deleted: Deprecated: Use status=all instead. When true, includes soft-deleted browser
              sessions in the results alongside active sessions.

          limit: Maximum number of results to return. Defaults to 20, maximum 100.

          offset: Number of results to skip. Defaults to 0.

          status: Filter sessions by status. "active" returns only active sessions (default),
              "deleted" returns only soft-deleted sessions, "all" returns both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/browsers",
            page=SyncOffsetPagination[BrowserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_deleted": include_deleted,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    browser_list_params.BrowserListParams,
                ),
            ),
            model=BrowserListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        *,
        persistent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """DEPRECATED: Use DELETE /browsers/{id} instead.

        Delete a persistent browser
        session by its persistent_id.

        Args:
          persistent_id: Persistent browser identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/browsers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"persistent_id": persistent_id}, browser_delete_params.BrowserDeleteParams),
            ),
            cast_to=NoneType,
        )

    def delete_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a browser session by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/browsers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def load_extensions(
        self,
        id: str,
        *,
        extensions: Iterable[browser_load_extensions_params.Extension],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Loads one or more unpacked extensions and restarts Chromium on the browser
        instance.

        Args:
          extensions: List of extensions to upload and activate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"extensions": extensions})
        files = extract_files(cast(Mapping[str, object], body), paths=[["extensions", "<array>", "zip_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            f"/browsers/{id}/extensions",
            body=maybe_transform(body, browser_load_extensions_params.BrowserLoadExtensionsParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBrowsersResource(AsyncAPIResource):
    @cached_property
    def replays(self) -> AsyncReplaysResource:
        return AsyncReplaysResource(self._client)

    @cached_property
    def fs(self) -> AsyncFsResource:
        return AsyncFsResource(self._client)

    @cached_property
    def process(self) -> AsyncProcessResource:
        return AsyncProcessResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def computer(self) -> AsyncComputerResource:
        return AsyncComputerResource(self._client)

    @cached_property
    def playwright(self) -> AsyncPlaywrightResource:
        return AsyncPlaywrightResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncBrowsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        extensions: Iterable[BrowserExtension] | Omit = omit,
        headless: bool | Omit = omit,
        invocation_id: str | Omit = omit,
        kiosk_mode: bool | Omit = omit,
        persistence: BrowserPersistenceParam | Omit = omit,
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
    ) -> BrowserCreateResponse:
        """
        Create a new browser session from within an action.

        Args:
          extensions: List of browser extensions to load into the session. Provide each by id or name.

          headless: If true, launches the browser using a headless image (no VNC/GUI). Defaults to
              false.

          invocation_id: action invocation ID

          kiosk_mode: If true, launches the browser in kiosk mode to hide address bar and tabs in live
              view.

          persistence: DEPRECATED: Use timeout_seconds (up to 72 hours) and Profiles instead.

          profile: Profile selection for the browser session. Provide either id or name. If
              specified, the matching profile will be loaded into the browser session.
              Profiles must be created beforehand.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy
              belonging to the caller's org.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: The number of seconds of inactivity before the browser session is terminated.
              Activity includes CDP connections and live view connections. Defaults to 60
              seconds. Minimum allowed is 10 seconds. Maximum allowed is 259200 (72 hours). We
              check for inactivity every 5 seconds, so the actual timeout behavior you will
              see is +/- 5 seconds around the specified value.

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
            "/browsers",
            body=await async_maybe_transform(
                {
                    "extensions": extensions,
                    "headless": headless,
                    "invocation_id": invocation_id,
                    "kiosk_mode": kiosk_mode,
                    "persistence": persistence,
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "stealth": stealth,
                    "timeout_seconds": timeout_seconds,
                    "viewport": viewport,
                },
                browser_create_params.BrowserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserRetrieveResponse:
        """
        Get information about a browser session.

        Args:
          include_deleted: When true, includes soft-deleted browser sessions in the lookup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/browsers/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_deleted": include_deleted}, browser_retrieve_params.BrowserRetrieveParams
                ),
            ),
            cast_to=BrowserRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        profile: BrowserProfile | Omit = omit,
        proxy_id: Optional[str] | Omit = omit,
        viewport: BrowserViewport | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserUpdateResponse:
        """
        Update a browser session.

        Args:
          profile: Profile to load into the browser session. Only allowed if the session does not
              already have a profile loaded.

          proxy_id: ID of the proxy to use. Omit to leave unchanged, set to empty string to remove
              proxy.

          viewport: Viewport configuration to apply to the browser session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/browsers/{id}",
            body=await async_maybe_transform(
                {
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "viewport": viewport,
                },
                browser_update_params.BrowserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserUpdateResponse,
        )

    def list(
        self,
        *,
        include_deleted: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["active", "deleted", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BrowserListResponse, AsyncOffsetPagination[BrowserListResponse]]:
        """List all browser sessions with pagination support.

        Use status parameter to
        filter by session state.

        Args:
          include_deleted: Deprecated: Use status=all instead. When true, includes soft-deleted browser
              sessions in the results alongside active sessions.

          limit: Maximum number of results to return. Defaults to 20, maximum 100.

          offset: Number of results to skip. Defaults to 0.

          status: Filter sessions by status. "active" returns only active sessions (default),
              "deleted" returns only soft-deleted sessions, "all" returns both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/browsers",
            page=AsyncOffsetPagination[BrowserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_deleted": include_deleted,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    browser_list_params.BrowserListParams,
                ),
            ),
            model=BrowserListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        *,
        persistent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """DEPRECATED: Use DELETE /browsers/{id} instead.

        Delete a persistent browser
        session by its persistent_id.

        Args:
          persistent_id: Persistent browser identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/browsers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"persistent_id": persistent_id}, browser_delete_params.BrowserDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def delete_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a browser session by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/browsers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def load_extensions(
        self,
        id: str,
        *,
        extensions: Iterable[browser_load_extensions_params.Extension],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Loads one or more unpacked extensions and restarts Chromium on the browser
        instance.

        Args:
          extensions: List of extensions to upload and activate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"extensions": extensions})
        files = extract_files(cast(Mapping[str, object], body), paths=[["extensions", "<array>", "zip_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            f"/browsers/{id}/extensions",
            body=await async_maybe_transform(body, browser_load_extensions_params.BrowserLoadExtensionsParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BrowsersResourceWithRawResponse:
    def __init__(self, browsers: BrowsersResource) -> None:
        self._browsers = browsers

        self.create = to_raw_response_wrapper(
            browsers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            browsers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            browsers.update,
        )
        self.list = to_raw_response_wrapper(
            browsers.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                browsers.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete_by_id = to_raw_response_wrapper(
            browsers.delete_by_id,
        )
        self.load_extensions = to_raw_response_wrapper(
            browsers.load_extensions,
        )

    @cached_property
    def replays(self) -> ReplaysResourceWithRawResponse:
        return ReplaysResourceWithRawResponse(self._browsers.replays)

    @cached_property
    def fs(self) -> FsResourceWithRawResponse:
        return FsResourceWithRawResponse(self._browsers.fs)

    @cached_property
    def process(self) -> ProcessResourceWithRawResponse:
        return ProcessResourceWithRawResponse(self._browsers.process)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._browsers.logs)

    @cached_property
    def computer(self) -> ComputerResourceWithRawResponse:
        return ComputerResourceWithRawResponse(self._browsers.computer)

    @cached_property
    def playwright(self) -> PlaywrightResourceWithRawResponse:
        return PlaywrightResourceWithRawResponse(self._browsers.playwright)


class AsyncBrowsersResourceWithRawResponse:
    def __init__(self, browsers: AsyncBrowsersResource) -> None:
        self._browsers = browsers

        self.create = async_to_raw_response_wrapper(
            browsers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            browsers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            browsers.update,
        )
        self.list = async_to_raw_response_wrapper(
            browsers.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                browsers.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete_by_id = async_to_raw_response_wrapper(
            browsers.delete_by_id,
        )
        self.load_extensions = async_to_raw_response_wrapper(
            browsers.load_extensions,
        )

    @cached_property
    def replays(self) -> AsyncReplaysResourceWithRawResponse:
        return AsyncReplaysResourceWithRawResponse(self._browsers.replays)

    @cached_property
    def fs(self) -> AsyncFsResourceWithRawResponse:
        return AsyncFsResourceWithRawResponse(self._browsers.fs)

    @cached_property
    def process(self) -> AsyncProcessResourceWithRawResponse:
        return AsyncProcessResourceWithRawResponse(self._browsers.process)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._browsers.logs)

    @cached_property
    def computer(self) -> AsyncComputerResourceWithRawResponse:
        return AsyncComputerResourceWithRawResponse(self._browsers.computer)

    @cached_property
    def playwright(self) -> AsyncPlaywrightResourceWithRawResponse:
        return AsyncPlaywrightResourceWithRawResponse(self._browsers.playwright)


class BrowsersResourceWithStreamingResponse:
    def __init__(self, browsers: BrowsersResource) -> None:
        self._browsers = browsers

        self.create = to_streamed_response_wrapper(
            browsers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            browsers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            browsers.update,
        )
        self.list = to_streamed_response_wrapper(
            browsers.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                browsers.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete_by_id = to_streamed_response_wrapper(
            browsers.delete_by_id,
        )
        self.load_extensions = to_streamed_response_wrapper(
            browsers.load_extensions,
        )

    @cached_property
    def replays(self) -> ReplaysResourceWithStreamingResponse:
        return ReplaysResourceWithStreamingResponse(self._browsers.replays)

    @cached_property
    def fs(self) -> FsResourceWithStreamingResponse:
        return FsResourceWithStreamingResponse(self._browsers.fs)

    @cached_property
    def process(self) -> ProcessResourceWithStreamingResponse:
        return ProcessResourceWithStreamingResponse(self._browsers.process)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._browsers.logs)

    @cached_property
    def computer(self) -> ComputerResourceWithStreamingResponse:
        return ComputerResourceWithStreamingResponse(self._browsers.computer)

    @cached_property
    def playwright(self) -> PlaywrightResourceWithStreamingResponse:
        return PlaywrightResourceWithStreamingResponse(self._browsers.playwright)


class AsyncBrowsersResourceWithStreamingResponse:
    def __init__(self, browsers: AsyncBrowsersResource) -> None:
        self._browsers = browsers

        self.create = async_to_streamed_response_wrapper(
            browsers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            browsers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            browsers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            browsers.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                browsers.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete_by_id = async_to_streamed_response_wrapper(
            browsers.delete_by_id,
        )
        self.load_extensions = async_to_streamed_response_wrapper(
            browsers.load_extensions,
        )

    @cached_property
    def replays(self) -> AsyncReplaysResourceWithStreamingResponse:
        return AsyncReplaysResourceWithStreamingResponse(self._browsers.replays)

    @cached_property
    def fs(self) -> AsyncFsResourceWithStreamingResponse:
        return AsyncFsResourceWithStreamingResponse(self._browsers.fs)

    @cached_property
    def process(self) -> AsyncProcessResourceWithStreamingResponse:
        return AsyncProcessResourceWithStreamingResponse(self._browsers.process)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._browsers.logs)

    @cached_property
    def computer(self) -> AsyncComputerResourceWithStreamingResponse:
        return AsyncComputerResourceWithStreamingResponse(self._browsers.computer)

    @cached_property
    def playwright(self) -> AsyncPlaywrightResourceWithStreamingResponse:
        return AsyncPlaywrightResourceWithStreamingResponse(self._browsers.playwright)
