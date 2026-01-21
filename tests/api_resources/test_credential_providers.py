# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    CredentialProvider,
    CredentialProviderTestResult,
    CredentialProviderListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredentialProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        credential_provider = client.credential_providers.create(
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            provider_type="onepassword",
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        credential_provider = client.credential_providers.create(
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            provider_type="onepassword",
            cache_ttl_seconds=300,
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.credential_providers.with_raw_response.create(
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            provider_type="onepassword",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = response.parse()
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.credential_providers.with_streaming_response.create(
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            provider_type="onepassword",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = response.parse()
            assert_matches_type(CredentialProvider, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        credential_provider = client.credential_providers.retrieve(
            "id",
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.credential_providers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = response.parse()
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.credential_providers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = response.parse()
            assert_matches_type(CredentialProvider, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credential_providers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        credential_provider = client.credential_providers.update(
            id="id",
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        credential_provider = client.credential_providers.update(
            id="id",
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            cache_ttl_seconds=300,
            enabled=True,
            priority=0,
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.credential_providers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = response.parse()
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.credential_providers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = response.parse()
            assert_matches_type(CredentialProvider, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credential_providers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        credential_provider = client.credential_providers.list()
        assert_matches_type(CredentialProviderListResponse, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.credential_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = response.parse()
        assert_matches_type(CredentialProviderListResponse, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.credential_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = response.parse()
            assert_matches_type(CredentialProviderListResponse, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        credential_provider = client.credential_providers.delete(
            "id",
        )
        assert credential_provider is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.credential_providers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = response.parse()
        assert credential_provider is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.credential_providers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = response.parse()
            assert credential_provider is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credential_providers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test(self, client: Kernel) -> None:
        credential_provider = client.credential_providers.test(
            "id",
        )
        assert_matches_type(CredentialProviderTestResult, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Kernel) -> None:
        response = client.credential_providers.with_raw_response.test(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = response.parse()
        assert_matches_type(CredentialProviderTestResult, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Kernel) -> None:
        with client.credential_providers.with_streaming_response.test(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = response.parse()
            assert_matches_type(CredentialProviderTestResult, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credential_providers.with_raw_response.test(
                "",
            )


class TestAsyncCredentialProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        credential_provider = await async_client.credential_providers.create(
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            provider_type="onepassword",
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        credential_provider = await async_client.credential_providers.create(
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            provider_type="onepassword",
            cache_ttl_seconds=300,
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.credential_providers.with_raw_response.create(
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            provider_type="onepassword",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = await response.parse()
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.credential_providers.with_streaming_response.create(
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            provider_type="onepassword",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = await response.parse()
            assert_matches_type(CredentialProvider, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        credential_provider = await async_client.credential_providers.retrieve(
            "id",
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.credential_providers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = await response.parse()
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.credential_providers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = await response.parse()
            assert_matches_type(CredentialProvider, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credential_providers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        credential_provider = await async_client.credential_providers.update(
            id="id",
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        credential_provider = await async_client.credential_providers.update(
            id="id",
            token="ops_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
            cache_ttl_seconds=300,
            enabled=True,
            priority=0,
        )
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.credential_providers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = await response.parse()
        assert_matches_type(CredentialProvider, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.credential_providers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = await response.parse()
            assert_matches_type(CredentialProvider, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credential_providers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        credential_provider = await async_client.credential_providers.list()
        assert_matches_type(CredentialProviderListResponse, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.credential_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = await response.parse()
        assert_matches_type(CredentialProviderListResponse, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.credential_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = await response.parse()
            assert_matches_type(CredentialProviderListResponse, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        credential_provider = await async_client.credential_providers.delete(
            "id",
        )
        assert credential_provider is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.credential_providers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = await response.parse()
        assert credential_provider is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.credential_providers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = await response.parse()
            assert credential_provider is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credential_providers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncKernel) -> None:
        credential_provider = await async_client.credential_providers.test(
            "id",
        )
        assert_matches_type(CredentialProviderTestResult, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncKernel) -> None:
        response = await async_client.credential_providers.with_raw_response.test(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential_provider = await response.parse()
        assert_matches_type(CredentialProviderTestResult, credential_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncKernel) -> None:
        async with async_client.credential_providers.with_streaming_response.test(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential_provider = await response.parse()
            assert_matches_type(CredentialProviderTestResult, credential_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credential_providers.with_raw_response.test(
                "",
            )
