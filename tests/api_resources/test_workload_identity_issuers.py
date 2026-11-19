# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    WorkloadIdentityIssuer,
    WorkloadIdentityIssuerKeyCheck,
)
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkloadIdentityIssuers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.create(
            name="name",
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.create(
            name="name",
            description="description",
            enabled=True,
            issuer_url="https://example.com",
            jwks={
                "type": "discovery",
                "ca_cert_pem": "ca_cert_pem",
                "discovery_base_url": "https://example.com",
                "keys": [{"foo": "bar"}],
                "url": "https://example.com",
            },
            preset_type="github_actions",
            token_validation={
                "max_lifetime_seconds": 1,
                "replay_protection": "single_use",
            },
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.workload_identity_issuers.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = response.parse()
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.workload_identity_issuers.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = response.parse()
            assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.retrieve(
            "id",
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.workload_identity_issuers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = response.parse()
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.workload_identity_issuers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = response.parse()
            assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workload_identity_issuers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.update(
            id="id",
            expected_version=1,
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.update(
            id="id",
            expected_version=1,
            description="description",
            enabled=True,
            issuer_url="https://example.com",
            jwks={
                "type": "discovery",
                "ca_cert_pem": "ca_cert_pem",
                "discovery_base_url": "https://example.com",
                "keys": [{"foo": "bar"}],
                "url": "https://example.com",
            },
            name="name",
            preset_type="github_actions",
            token_validation={
                "max_lifetime_seconds": 1,
                "replay_protection": "single_use",
            },
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.workload_identity_issuers.with_raw_response.update(
            id="id",
            expected_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = response.parse()
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.workload_identity_issuers.with_streaming_response.update(
            id="id",
            expected_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = response.parse()
            assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workload_identity_issuers.with_raw_response.update(
                id="",
                expected_version=1,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.list()
        assert_matches_type(SyncOffsetPagination[WorkloadIdentityIssuer], workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.list(
            enabled=True,
            limit=1,
            offset=0,
            query="query",
            status="active",
        )
        assert_matches_type(SyncOffsetPagination[WorkloadIdentityIssuer], workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.workload_identity_issuers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = response.parse()
        assert_matches_type(SyncOffsetPagination[WorkloadIdentityIssuer], workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.workload_identity_issuers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = response.parse()
            assert_matches_type(
                SyncOffsetPagination[WorkloadIdentityIssuer], workload_identity_issuer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.delete(
            "id",
        )
        assert workload_identity_issuer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.workload_identity_issuers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = response.parse()
        assert workload_identity_issuer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.workload_identity_issuers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = response.parse()
            assert workload_identity_issuer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workload_identity_issuers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: Kernel) -> None:
        workload_identity_issuer = client.workload_identity_issuers.verify(
            "id",
        )
        assert_matches_type(WorkloadIdentityIssuerKeyCheck, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Kernel) -> None:
        response = client.workload_identity_issuers.with_raw_response.verify(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = response.parse()
        assert_matches_type(WorkloadIdentityIssuerKeyCheck, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Kernel) -> None:
        with client.workload_identity_issuers.with_streaming_response.verify(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = response.parse()
            assert_matches_type(WorkloadIdentityIssuerKeyCheck, workload_identity_issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_verify(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workload_identity_issuers.with_raw_response.verify(
                "",
            )


class TestAsyncWorkloadIdentityIssuers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.create(
            name="name",
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.create(
            name="name",
            description="description",
            enabled=True,
            issuer_url="https://example.com",
            jwks={
                "type": "discovery",
                "ca_cert_pem": "ca_cert_pem",
                "discovery_base_url": "https://example.com",
                "keys": [{"foo": "bar"}],
                "url": "https://example.com",
            },
            preset_type="github_actions",
            token_validation={
                "max_lifetime_seconds": 1,
                "replay_protection": "single_use",
            },
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_issuers.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = await response.parse()
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_issuers.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = await response.parse()
            assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.retrieve(
            "id",
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_issuers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = await response.parse()
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_issuers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = await response.parse()
            assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workload_identity_issuers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.update(
            id="id",
            expected_version=1,
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.update(
            id="id",
            expected_version=1,
            description="description",
            enabled=True,
            issuer_url="https://example.com",
            jwks={
                "type": "discovery",
                "ca_cert_pem": "ca_cert_pem",
                "discovery_base_url": "https://example.com",
                "keys": [{"foo": "bar"}],
                "url": "https://example.com",
            },
            name="name",
            preset_type="github_actions",
            token_validation={
                "max_lifetime_seconds": 1,
                "replay_protection": "single_use",
            },
        )
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_issuers.with_raw_response.update(
            id="id",
            expected_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = await response.parse()
        assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_issuers.with_streaming_response.update(
            id="id",
            expected_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = await response.parse()
            assert_matches_type(WorkloadIdentityIssuer, workload_identity_issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workload_identity_issuers.with_raw_response.update(
                id="",
                expected_version=1,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.list()
        assert_matches_type(AsyncOffsetPagination[WorkloadIdentityIssuer], workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.list(
            enabled=True,
            limit=1,
            offset=0,
            query="query",
            status="active",
        )
        assert_matches_type(AsyncOffsetPagination[WorkloadIdentityIssuer], workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_issuers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = await response.parse()
        assert_matches_type(AsyncOffsetPagination[WorkloadIdentityIssuer], workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_issuers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = await response.parse()
            assert_matches_type(
                AsyncOffsetPagination[WorkloadIdentityIssuer], workload_identity_issuer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.delete(
            "id",
        )
        assert workload_identity_issuer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_issuers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = await response.parse()
        assert workload_identity_issuer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_issuers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = await response.parse()
            assert workload_identity_issuer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workload_identity_issuers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncKernel) -> None:
        workload_identity_issuer = await async_client.workload_identity_issuers.verify(
            "id",
        )
        assert_matches_type(WorkloadIdentityIssuerKeyCheck, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_issuers.with_raw_response.verify(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_issuer = await response.parse()
        assert_matches_type(WorkloadIdentityIssuerKeyCheck, workload_identity_issuer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_issuers.with_streaming_response.verify(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_issuer = await response.parse()
            assert_matches_type(WorkloadIdentityIssuerKeyCheck, workload_identity_issuer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_verify(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workload_identity_issuers.with_raw_response.verify(
                "",
            )
