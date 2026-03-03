# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
)

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def connections(self) -> ConnectionsResource:
        """Create and manage auth connections for automated credential capture and login."""
        return ConnectionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        """Create and manage auth connections for automated credential capture and login."""
        return AsyncConnectionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        """Create and manage auth connections for automated credential capture and login."""
        return ConnectionsResourceWithRawResponse(self._auth.connections)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        """Create and manage auth connections for automated credential capture and login."""
        return AsyncConnectionsResourceWithRawResponse(self._auth.connections)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        """Create and manage auth connections for automated credential capture and login."""
        return ConnectionsResourceWithStreamingResponse(self._auth.connections)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """Create and manage auth connections for automated credential capture and login."""
        return AsyncConnectionsResourceWithStreamingResponse(self._auth.connections)
