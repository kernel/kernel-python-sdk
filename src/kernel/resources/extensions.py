# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import extension_upload_params, extension_download_from_chrome_store_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.extension_list_response import ExtensionListResponse
from ..types.extension_upload_response import ExtensionUploadResponse

__all__ = ["ExtensionsResource", "AsyncExtensionsResource"]


class ExtensionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ExtensionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionListResponse:
        """List extensions owned by the caller's organization."""
        return self._get(
            "/extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionListResponse,
        )

    def delete(
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
        Delete an extension by its ID or by its name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/extensions/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def download(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download the extension as a ZIP archive by ID or name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/extensions/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def download_from_chrome_store(
        self,
        *,
        url: str,
        os: Literal["win", "mac", "linux"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Returns a ZIP archive containing the unpacked extension fetched from the Chrome
        Web Store.

        Args:
          url: Chrome Web Store URL for the extension.

          os: Target operating system for the extension package. Defaults to linux.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            "/extensions/from_chrome_store",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "os": os,
                    },
                    extension_download_from_chrome_store_params.ExtensionDownloadFromChromeStoreParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionUploadResponse:
        """Upload a zip file containing an unpacked browser extension.

        Optionally provide a
        unique name for later reference.

        Args:
          file: ZIP file containing the browser extension.

          name: Optional unique name within the organization to reference this extension.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "name": name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/extensions",
            body=maybe_transform(body, extension_upload_params.ExtensionUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionUploadResponse,
        )


class AsyncExtensionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncExtensionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionListResponse:
        """List extensions owned by the caller's organization."""
        return await self._get(
            "/extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionListResponse,
        )

    async def delete(
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
        Delete an extension by its ID or by its name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/extensions/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def download(
        self,
        id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download the extension as a ZIP archive by ID or name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_or_name:
            raise ValueError(f"Expected a non-empty value for `id_or_name` but received {id_or_name!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/extensions/{id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def download_from_chrome_store(
        self,
        *,
        url: str,
        os: Literal["win", "mac", "linux"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Returns a ZIP archive containing the unpacked extension fetched from the Chrome
        Web Store.

        Args:
          url: Chrome Web Store URL for the extension.

          os: Target operating system for the extension package. Defaults to linux.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            "/extensions/from_chrome_store",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "os": os,
                    },
                    extension_download_from_chrome_store_params.ExtensionDownloadFromChromeStoreParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionUploadResponse:
        """Upload a zip file containing an unpacked browser extension.

        Optionally provide a
        unique name for later reference.

        Args:
          file: ZIP file containing the browser extension.

          name: Optional unique name within the organization to reference this extension.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "name": name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/extensions",
            body=await async_maybe_transform(body, extension_upload_params.ExtensionUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionUploadResponse,
        )


class ExtensionsResourceWithRawResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

        self.list = to_raw_response_wrapper(
            extensions.list,
        )
        self.delete = to_raw_response_wrapper(
            extensions.delete,
        )
        self.download = to_custom_raw_response_wrapper(
            extensions.download,
            BinaryAPIResponse,
        )
        self.download_from_chrome_store = to_custom_raw_response_wrapper(
            extensions.download_from_chrome_store,
            BinaryAPIResponse,
        )
        self.upload = to_raw_response_wrapper(
            extensions.upload,
        )


class AsyncExtensionsResourceWithRawResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

        self.list = async_to_raw_response_wrapper(
            extensions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            extensions.delete,
        )
        self.download = async_to_custom_raw_response_wrapper(
            extensions.download,
            AsyncBinaryAPIResponse,
        )
        self.download_from_chrome_store = async_to_custom_raw_response_wrapper(
            extensions.download_from_chrome_store,
            AsyncBinaryAPIResponse,
        )
        self.upload = async_to_raw_response_wrapper(
            extensions.upload,
        )


class ExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

        self.list = to_streamed_response_wrapper(
            extensions.list,
        )
        self.delete = to_streamed_response_wrapper(
            extensions.delete,
        )
        self.download = to_custom_streamed_response_wrapper(
            extensions.download,
            StreamedBinaryAPIResponse,
        )
        self.download_from_chrome_store = to_custom_streamed_response_wrapper(
            extensions.download_from_chrome_store,
            StreamedBinaryAPIResponse,
        )
        self.upload = to_streamed_response_wrapper(
            extensions.upload,
        )


class AsyncExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

        self.list = async_to_streamed_response_wrapper(
            extensions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            extensions.delete,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            extensions.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.download_from_chrome_store = async_to_custom_streamed_response_wrapper(
            extensions.download_from_chrome_store,
            AsyncStreamedBinaryAPIResponse,
        )
        self.upload = async_to_streamed_response_wrapper(
            extensions.upload,
        )
