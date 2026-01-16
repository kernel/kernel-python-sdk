# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import KernelError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        apps,
        agents,
        proxies,
        browsers,
        profiles,
        extensions,
        credentials,
        deployments,
        invocations,
        browser_pools,
    )
    from .resources.apps import AppsResource, AsyncAppsResource
    from .resources.proxies import ProxiesResource, AsyncProxiesResource
    from .resources.profiles import ProfilesResource, AsyncProfilesResource
    from .resources.extensions import ExtensionsResource, AsyncExtensionsResource
    from .resources.credentials import CredentialsResource, AsyncCredentialsResource
    from .resources.deployments import DeploymentsResource, AsyncDeploymentsResource
    from .resources.invocations import InvocationsResource, AsyncInvocationsResource
    from .resources.agents.agents import AgentsResource, AsyncAgentsResource
    from .resources.browser_pools import BrowserPoolsResource, AsyncBrowserPoolsResource
    from .resources.browsers.browsers import BrowsersResource, AsyncBrowsersResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Kernel",
    "AsyncKernel",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.onkernel.com/",
    "development": "https://localhost:3001/",
}


class Kernel(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "development"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Kernel client instance.

        This automatically infers the `api_key` argument from the `KERNEL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("KERNEL_API_KEY")
        if api_key is None:
            raise KernelError(
                "The api_key client option must be set either by passing api_key to the client or by setting the KERNEL_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("KERNEL_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `KERNEL_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def deployments(self) -> DeploymentsResource:
        from .resources.deployments import DeploymentsResource

        return DeploymentsResource(self)

    @cached_property
    def apps(self) -> AppsResource:
        from .resources.apps import AppsResource

        return AppsResource(self)

    @cached_property
    def invocations(self) -> InvocationsResource:
        from .resources.invocations import InvocationsResource

        return InvocationsResource(self)

    @cached_property
    def browsers(self) -> BrowsersResource:
        from .resources.browsers import BrowsersResource

        return BrowsersResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        from .resources.profiles import ProfilesResource

        return ProfilesResource(self)

    @cached_property
    def proxies(self) -> ProxiesResource:
        from .resources.proxies import ProxiesResource

        return ProxiesResource(self)

    @cached_property
    def extensions(self) -> ExtensionsResource:
        from .resources.extensions import ExtensionsResource

        return ExtensionsResource(self)

    @cached_property
    def browser_pools(self) -> BrowserPoolsResource:
        from .resources.browser_pools import BrowserPoolsResource

        return BrowserPoolsResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def credentials(self) -> CredentialsResource:
        from .resources.credentials import CredentialsResource

        return CredentialsResource(self)

    @cached_property
    def with_raw_response(self) -> KernelWithRawResponse:
        return KernelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KernelWithStreamedResponse:
        return KernelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncKernel(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "development"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncKernel client instance.

        This automatically infers the `api_key` argument from the `KERNEL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("KERNEL_API_KEY")
        if api_key is None:
            raise KernelError(
                "The api_key client option must be set either by passing api_key to the client or by setting the KERNEL_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("KERNEL_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `KERNEL_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        from .resources.deployments import AsyncDeploymentsResource

        return AsyncDeploymentsResource(self)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        from .resources.apps import AsyncAppsResource

        return AsyncAppsResource(self)

    @cached_property
    def invocations(self) -> AsyncInvocationsResource:
        from .resources.invocations import AsyncInvocationsResource

        return AsyncInvocationsResource(self)

    @cached_property
    def browsers(self) -> AsyncBrowsersResource:
        from .resources.browsers import AsyncBrowsersResource

        return AsyncBrowsersResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        from .resources.profiles import AsyncProfilesResource

        return AsyncProfilesResource(self)

    @cached_property
    def proxies(self) -> AsyncProxiesResource:
        from .resources.proxies import AsyncProxiesResource

        return AsyncProxiesResource(self)

    @cached_property
    def extensions(self) -> AsyncExtensionsResource:
        from .resources.extensions import AsyncExtensionsResource

        return AsyncExtensionsResource(self)

    @cached_property
    def browser_pools(self) -> AsyncBrowserPoolsResource:
        from .resources.browser_pools import AsyncBrowserPoolsResource

        return AsyncBrowserPoolsResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        from .resources.credentials import AsyncCredentialsResource

        return AsyncCredentialsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncKernelWithRawResponse:
        return AsyncKernelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKernelWithStreamedResponse:
        return AsyncKernelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class KernelWithRawResponse:
    _client: Kernel

    def __init__(self, client: Kernel) -> None:
        self._client = client

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithRawResponse:
        from .resources.deployments import DeploymentsResourceWithRawResponse

        return DeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def apps(self) -> apps.AppsResourceWithRawResponse:
        from .resources.apps import AppsResourceWithRawResponse

        return AppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def invocations(self) -> invocations.InvocationsResourceWithRawResponse:
        from .resources.invocations import InvocationsResourceWithRawResponse

        return InvocationsResourceWithRawResponse(self._client.invocations)

    @cached_property
    def browsers(self) -> browsers.BrowsersResourceWithRawResponse:
        from .resources.browsers import BrowsersResourceWithRawResponse

        return BrowsersResourceWithRawResponse(self._client.browsers)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        from .resources.profiles import ProfilesResourceWithRawResponse

        return ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def proxies(self) -> proxies.ProxiesResourceWithRawResponse:
        from .resources.proxies import ProxiesResourceWithRawResponse

        return ProxiesResourceWithRawResponse(self._client.proxies)

    @cached_property
    def extensions(self) -> extensions.ExtensionsResourceWithRawResponse:
        from .resources.extensions import ExtensionsResourceWithRawResponse

        return ExtensionsResourceWithRawResponse(self._client.extensions)

    @cached_property
    def browser_pools(self) -> browser_pools.BrowserPoolsResourceWithRawResponse:
        from .resources.browser_pools import BrowserPoolsResourceWithRawResponse

        return BrowserPoolsResourceWithRawResponse(self._client.browser_pools)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def credentials(self) -> credentials.CredentialsResourceWithRawResponse:
        from .resources.credentials import CredentialsResourceWithRawResponse

        return CredentialsResourceWithRawResponse(self._client.credentials)


class AsyncKernelWithRawResponse:
    _client: AsyncKernel

    def __init__(self, client: AsyncKernel) -> None:
        self._client = client

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithRawResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithRawResponse

        return AsyncDeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithRawResponse:
        from .resources.apps import AsyncAppsResourceWithRawResponse

        return AsyncAppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def invocations(self) -> invocations.AsyncInvocationsResourceWithRawResponse:
        from .resources.invocations import AsyncInvocationsResourceWithRawResponse

        return AsyncInvocationsResourceWithRawResponse(self._client.invocations)

    @cached_property
    def browsers(self) -> browsers.AsyncBrowsersResourceWithRawResponse:
        from .resources.browsers import AsyncBrowsersResourceWithRawResponse

        return AsyncBrowsersResourceWithRawResponse(self._client.browsers)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        from .resources.profiles import AsyncProfilesResourceWithRawResponse

        return AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def proxies(self) -> proxies.AsyncProxiesResourceWithRawResponse:
        from .resources.proxies import AsyncProxiesResourceWithRawResponse

        return AsyncProxiesResourceWithRawResponse(self._client.proxies)

    @cached_property
    def extensions(self) -> extensions.AsyncExtensionsResourceWithRawResponse:
        from .resources.extensions import AsyncExtensionsResourceWithRawResponse

        return AsyncExtensionsResourceWithRawResponse(self._client.extensions)

    @cached_property
    def browser_pools(self) -> browser_pools.AsyncBrowserPoolsResourceWithRawResponse:
        from .resources.browser_pools import AsyncBrowserPoolsResourceWithRawResponse

        return AsyncBrowserPoolsResourceWithRawResponse(self._client.browser_pools)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def credentials(self) -> credentials.AsyncCredentialsResourceWithRawResponse:
        from .resources.credentials import AsyncCredentialsResourceWithRawResponse

        return AsyncCredentialsResourceWithRawResponse(self._client.credentials)


class KernelWithStreamedResponse:
    _client: Kernel

    def __init__(self, client: Kernel) -> None:
        self._client = client

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithStreamingResponse:
        from .resources.deployments import DeploymentsResourceWithStreamingResponse

        return DeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def apps(self) -> apps.AppsResourceWithStreamingResponse:
        from .resources.apps import AppsResourceWithStreamingResponse

        return AppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def invocations(self) -> invocations.InvocationsResourceWithStreamingResponse:
        from .resources.invocations import InvocationsResourceWithStreamingResponse

        return InvocationsResourceWithStreamingResponse(self._client.invocations)

    @cached_property
    def browsers(self) -> browsers.BrowsersResourceWithStreamingResponse:
        from .resources.browsers import BrowsersResourceWithStreamingResponse

        return BrowsersResourceWithStreamingResponse(self._client.browsers)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        from .resources.profiles import ProfilesResourceWithStreamingResponse

        return ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def proxies(self) -> proxies.ProxiesResourceWithStreamingResponse:
        from .resources.proxies import ProxiesResourceWithStreamingResponse

        return ProxiesResourceWithStreamingResponse(self._client.proxies)

    @cached_property
    def extensions(self) -> extensions.ExtensionsResourceWithStreamingResponse:
        from .resources.extensions import ExtensionsResourceWithStreamingResponse

        return ExtensionsResourceWithStreamingResponse(self._client.extensions)

    @cached_property
    def browser_pools(self) -> browser_pools.BrowserPoolsResourceWithStreamingResponse:
        from .resources.browser_pools import BrowserPoolsResourceWithStreamingResponse

        return BrowserPoolsResourceWithStreamingResponse(self._client.browser_pools)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def credentials(self) -> credentials.CredentialsResourceWithStreamingResponse:
        from .resources.credentials import CredentialsResourceWithStreamingResponse

        return CredentialsResourceWithStreamingResponse(self._client.credentials)


class AsyncKernelWithStreamedResponse:
    _client: AsyncKernel

    def __init__(self, client: AsyncKernel) -> None:
        self._client = client

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithStreamingResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithStreamingResponse

        return AsyncDeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithStreamingResponse:
        from .resources.apps import AsyncAppsResourceWithStreamingResponse

        return AsyncAppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def invocations(self) -> invocations.AsyncInvocationsResourceWithStreamingResponse:
        from .resources.invocations import AsyncInvocationsResourceWithStreamingResponse

        return AsyncInvocationsResourceWithStreamingResponse(self._client.invocations)

    @cached_property
    def browsers(self) -> browsers.AsyncBrowsersResourceWithStreamingResponse:
        from .resources.browsers import AsyncBrowsersResourceWithStreamingResponse

        return AsyncBrowsersResourceWithStreamingResponse(self._client.browsers)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        from .resources.profiles import AsyncProfilesResourceWithStreamingResponse

        return AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def proxies(self) -> proxies.AsyncProxiesResourceWithStreamingResponse:
        from .resources.proxies import AsyncProxiesResourceWithStreamingResponse

        return AsyncProxiesResourceWithStreamingResponse(self._client.proxies)

    @cached_property
    def extensions(self) -> extensions.AsyncExtensionsResourceWithStreamingResponse:
        from .resources.extensions import AsyncExtensionsResourceWithStreamingResponse

        return AsyncExtensionsResourceWithStreamingResponse(self._client.extensions)

    @cached_property
    def browser_pools(self) -> browser_pools.AsyncBrowserPoolsResourceWithStreamingResponse:
        from .resources.browser_pools import AsyncBrowserPoolsResourceWithStreamingResponse

        return AsyncBrowserPoolsResourceWithStreamingResponse(self._client.browser_pools)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def credentials(self) -> credentials.AsyncCredentialsResourceWithStreamingResponse:
        from .resources.credentials import AsyncCredentialsResourceWithStreamingResponse

        return AsyncCredentialsResourceWithStreamingResponse(self._client.credentials)


Client = Kernel

AsyncClient = AsyncKernel
