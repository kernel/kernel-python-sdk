# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    VaultProviderConfig,
)
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVaultProviderConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Kernel) -> None:
        vault_provider_config = client.vault_provider_configs.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="link",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Kernel) -> None:
        response = client.vault_provider_configs.with_raw_response.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="link",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = response.parse()
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Kernel) -> None:
        with client.vault_provider_configs.with_streaming_response.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="link",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = response.parse()
            assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Kernel) -> None:
        vault_provider_config = client.vault_provider_configs.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="agentcard",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Kernel) -> None:
        response = client.vault_provider_configs.with_raw_response.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="agentcard",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = response.parse()
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Kernel) -> None:
        with client.vault_provider_configs.with_streaming_response.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="agentcard",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = response.parse()
            assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        vault_provider_config = client.vault_provider_configs.retrieve(
            "id_or_name",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.vault_provider_configs.with_raw_response.retrieve(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = response.parse()
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.vault_provider_configs.with_streaming_response.retrieve(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = response.parse()
            assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vault_provider_configs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        vault_provider_config = client.vault_provider_configs.update(
            id_or_name="id_or_name",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        vault_provider_config = client.vault_provider_configs.update(
            id_or_name="id_or_name",
            credentials={"client_secret": "x"},
            name="renamed-link-client",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.vault_provider_configs.with_raw_response.update(
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = response.parse()
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.vault_provider_configs.with_streaming_response.update(
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = response.parse()
            assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vault_provider_configs.with_raw_response.update(
                id_or_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        vault_provider_config = client.vault_provider_configs.list()
        assert_matches_type(SyncOffsetPagination[VaultProviderConfig], vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        vault_provider_config = client.vault_provider_configs.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPagination[VaultProviderConfig], vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.vault_provider_configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = response.parse()
        assert_matches_type(SyncOffsetPagination[VaultProviderConfig], vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.vault_provider_configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = response.parse()
            assert_matches_type(SyncOffsetPagination[VaultProviderConfig], vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        vault_provider_config = client.vault_provider_configs.delete(
            "id_or_name",
        )
        assert vault_provider_config is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.vault_provider_configs.with_raw_response.delete(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = response.parse()
        assert vault_provider_config is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.vault_provider_configs.with_streaming_response.delete(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = response.parse()
            assert vault_provider_config is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            client.vault_provider_configs.with_raw_response.delete(
                "",
            )


class TestAsyncVaultProviderConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncKernel) -> None:
        vault_provider_config = await async_client.vault_provider_configs.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="link",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncKernel) -> None:
        response = await async_client.vault_provider_configs.with_raw_response.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="link",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = await response.parse()
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncKernel) -> None:
        async with async_client.vault_provider_configs.with_streaming_response.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="link",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = await response.parse()
            assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncKernel) -> None:
        vault_provider_config = await async_client.vault_provider_configs.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="agentcard",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncKernel) -> None:
        response = await async_client.vault_provider_configs.with_raw_response.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="agentcard",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = await response.parse()
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncKernel) -> None:
        async with async_client.vault_provider_configs.with_streaming_response.create(
            credentials={
                "client_id": "x",
                "client_secret": "x",
            },
            name="name",
            provider="agentcard",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = await response.parse()
            assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        vault_provider_config = await async_client.vault_provider_configs.retrieve(
            "id_or_name",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.vault_provider_configs.with_raw_response.retrieve(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = await response.parse()
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.vault_provider_configs.with_streaming_response.retrieve(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = await response.parse()
            assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vault_provider_configs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        vault_provider_config = await async_client.vault_provider_configs.update(
            id_or_name="id_or_name",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        vault_provider_config = await async_client.vault_provider_configs.update(
            id_or_name="id_or_name",
            credentials={"client_secret": "x"},
            name="renamed-link-client",
        )
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.vault_provider_configs.with_raw_response.update(
            id_or_name="id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = await response.parse()
        assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.vault_provider_configs.with_streaming_response.update(
            id_or_name="id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = await response.parse()
            assert_matches_type(VaultProviderConfig, vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vault_provider_configs.with_raw_response.update(
                id_or_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        vault_provider_config = await async_client.vault_provider_configs.list()
        assert_matches_type(AsyncOffsetPagination[VaultProviderConfig], vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        vault_provider_config = await async_client.vault_provider_configs.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPagination[VaultProviderConfig], vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.vault_provider_configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = await response.parse()
        assert_matches_type(AsyncOffsetPagination[VaultProviderConfig], vault_provider_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.vault_provider_configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = await response.parse()
            assert_matches_type(AsyncOffsetPagination[VaultProviderConfig], vault_provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        vault_provider_config = await async_client.vault_provider_configs.delete(
            "id_or_name",
        )
        assert vault_provider_config is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.vault_provider_configs.with_raw_response.delete(
            "id_or_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault_provider_config = await response.parse()
        assert vault_provider_config is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.vault_provider_configs.with_streaming_response.delete(
            "id_or_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault_provider_config = await response.parse()
            assert vault_provider_config is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_or_name` but received ''"):
            await async_client.vault_provider_configs.with_raw_response.delete(
                "",
            )
