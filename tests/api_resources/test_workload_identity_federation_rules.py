# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    WorkloadIdentityFederationRule,
)
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkloadIdentityFederationRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        workload_identity_federation_rule = client.workload_identity_federation_rules.create(
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
            },
            expected_audience="x",
            issuer_id="x",
            match={"type": "github_actions"},
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        workload_identity_federation_rule = client.workload_identity_federation_rules.create(
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                            "condition": {
                                "key": "source_ip",
                                "operator": "in",
                                "values": ["203.0.113.0/24"],
                            },
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
                "max_token_ttl_seconds": 1,
            },
            expected_audience="x",
            issuer_id="x",
            match={
                "type": "github_actions",
                "claims": {"foo": "x"},
                "environment": "environment",
                "event_names": ["x"],
                "job_workflow_ref": "job_workflow_ref",
                "namespace": "namespace",
                "ref": "ref",
                "repository": "repository",
                "repository_id": "269125115713",
                "repository_owner_id": "269125115713",
                "service_account": "service_account",
                "subject": "x",
                "subject_prefix": "x",
                "workflow": "workflow",
                "workflow_ref": "workflow_ref",
            },
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
            description="description",
            enabled=True,
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.workload_identity_federation_rules.with_raw_response.create(
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
            },
            expected_audience="x",
            issuer_id="x",
            match={"type": "github_actions"},
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = response.parse()
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.workload_identity_federation_rules.with_streaming_response.create(
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
            },
            expected_audience="x",
            issuer_id="x",
            match={"type": "github_actions"},
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = response.parse()
            assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        workload_identity_federation_rule = client.workload_identity_federation_rules.retrieve(
            "id",
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.workload_identity_federation_rules.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = response.parse()
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.workload_identity_federation_rules.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = response.parse()
            assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workload_identity_federation_rules.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        workload_identity_federation_rule = client.workload_identity_federation_rules.update(
            id="id",
            expected_version=1,
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        workload_identity_federation_rule = client.workload_identity_federation_rules.update(
            id="id",
            expected_version=1,
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                            "condition": {
                                "key": "source_ip",
                                "operator": "in",
                                "values": ["203.0.113.0/24"],
                            },
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
                "max_token_ttl_seconds": 1,
            },
            description="description",
            enabled=True,
            expected_audience="x",
            issuer_id="x",
            match={
                "type": "github_actions",
                "claims": {"foo": "x"},
                "environment": "environment",
                "event_names": ["x"],
                "job_workflow_ref": "job_workflow_ref",
                "namespace": "namespace",
                "ref": "ref",
                "repository": "repository",
                "repository_id": "269125115713",
                "repository_owner_id": "269125115713",
                "service_account": "service_account",
                "subject": "x",
                "subject_prefix": "x",
                "workflow": "workflow",
                "workflow_ref": "workflow_ref",
            },
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.workload_identity_federation_rules.with_raw_response.update(
            id="id",
            expected_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = response.parse()
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.workload_identity_federation_rules.with_streaming_response.update(
            id="id",
            expected_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = response.parse()
            assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workload_identity_federation_rules.with_raw_response.update(
                id="",
                expected_version=1,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        workload_identity_federation_rule = client.workload_identity_federation_rules.list()
        assert_matches_type(
            SyncOffsetPagination[WorkloadIdentityFederationRule], workload_identity_federation_rule, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        workload_identity_federation_rule = client.workload_identity_federation_rules.list(
            issuer_id="issuer_id",
            limit=1,
            offset=0,
            project_id="project_id",
            query="query",
            service_account_id="service_account_id",
            status="active",
        )
        assert_matches_type(
            SyncOffsetPagination[WorkloadIdentityFederationRule], workload_identity_federation_rule, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.workload_identity_federation_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = response.parse()
        assert_matches_type(
            SyncOffsetPagination[WorkloadIdentityFederationRule], workload_identity_federation_rule, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.workload_identity_federation_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = response.parse()
            assert_matches_type(
                SyncOffsetPagination[WorkloadIdentityFederationRule],
                workload_identity_federation_rule,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        workload_identity_federation_rule = client.workload_identity_federation_rules.delete(
            "id",
        )
        assert workload_identity_federation_rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.workload_identity_federation_rules.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = response.parse()
        assert workload_identity_federation_rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.workload_identity_federation_rules.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = response.parse()
            assert workload_identity_federation_rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workload_identity_federation_rules.with_raw_response.delete(
                "",
            )


class TestAsyncWorkloadIdentityFederationRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        workload_identity_federation_rule = await async_client.workload_identity_federation_rules.create(
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
            },
            expected_audience="x",
            issuer_id="x",
            match={"type": "github_actions"},
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        workload_identity_federation_rule = await async_client.workload_identity_federation_rules.create(
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                            "condition": {
                                "key": "source_ip",
                                "operator": "in",
                                "values": ["203.0.113.0/24"],
                            },
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
                "max_token_ttl_seconds": 1,
            },
            expected_audience="x",
            issuer_id="x",
            match={
                "type": "github_actions",
                "claims": {"foo": "x"},
                "environment": "environment",
                "event_names": ["x"],
                "job_workflow_ref": "job_workflow_ref",
                "namespace": "namespace",
                "ref": "ref",
                "repository": "repository",
                "repository_id": "269125115713",
                "repository_owner_id": "269125115713",
                "service_account": "service_account",
                "subject": "x",
                "subject_prefix": "x",
                "workflow": "workflow",
                "workflow_ref": "workflow_ref",
            },
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
            description="description",
            enabled=True,
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_federation_rules.with_raw_response.create(
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
            },
            expected_audience="x",
            issuer_id="x",
            match={"type": "github_actions"},
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = await response.parse()
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_federation_rules.with_streaming_response.create(
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
            },
            expected_audience="x",
            issuer_id="x",
            match={"type": "github_actions"},
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = await response.parse()
            assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        workload_identity_federation_rule = await async_client.workload_identity_federation_rules.retrieve(
            "id",
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_federation_rules.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = await response.parse()
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_federation_rules.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = await response.parse()
            assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workload_identity_federation_rules.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        workload_identity_federation_rule = await async_client.workload_identity_federation_rules.update(
            id="id",
            expected_version=1,
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        workload_identity_federation_rule = await async_client.workload_identity_federation_rules.update(
            id="id",
            expected_version=1,
            authorization={
                "policy": {
                    "statements": [
                        {
                            "action": "browsers:use",
                            "resource": "projects/proj_abc123/browsers/br_abc123",
                            "condition": {
                                "key": "source_ip",
                                "operator": "in",
                                "values": ["203.0.113.0/24"],
                            },
                        }
                    ]
                },
                "project_id": "x",
                "token_audience": "x",
                "max_token_ttl_seconds": 1,
            },
            description="description",
            enabled=True,
            expected_audience="x",
            issuer_id="x",
            match={
                "type": "github_actions",
                "claims": {"foo": "x"},
                "environment": "environment",
                "event_names": ["x"],
                "job_workflow_ref": "job_workflow_ref",
                "namespace": "namespace",
                "ref": "ref",
                "repository": "repository",
                "repository_id": "269125115713",
                "repository_owner_id": "269125115713",
                "service_account": "service_account",
                "subject": "x",
                "subject_prefix": "x",
                "workflow": "workflow",
                "workflow_ref": "workflow_ref",
            },
            name="name",
            target={
                "service_account_id": "x",
                "type": "service_account",
            },
        )
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_federation_rules.with_raw_response.update(
            id="id",
            expected_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = await response.parse()
        assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_federation_rules.with_streaming_response.update(
            id="id",
            expected_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = await response.parse()
            assert_matches_type(WorkloadIdentityFederationRule, workload_identity_federation_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workload_identity_federation_rules.with_raw_response.update(
                id="",
                expected_version=1,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        workload_identity_federation_rule = await async_client.workload_identity_federation_rules.list()
        assert_matches_type(
            AsyncOffsetPagination[WorkloadIdentityFederationRule], workload_identity_federation_rule, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        workload_identity_federation_rule = await async_client.workload_identity_federation_rules.list(
            issuer_id="issuer_id",
            limit=1,
            offset=0,
            project_id="project_id",
            query="query",
            service_account_id="service_account_id",
            status="active",
        )
        assert_matches_type(
            AsyncOffsetPagination[WorkloadIdentityFederationRule], workload_identity_federation_rule, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_federation_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = await response.parse()
        assert_matches_type(
            AsyncOffsetPagination[WorkloadIdentityFederationRule], workload_identity_federation_rule, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_federation_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = await response.parse()
            assert_matches_type(
                AsyncOffsetPagination[WorkloadIdentityFederationRule],
                workload_identity_federation_rule,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        workload_identity_federation_rule = await async_client.workload_identity_federation_rules.delete(
            "id",
        )
        assert workload_identity_federation_rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.workload_identity_federation_rules.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workload_identity_federation_rule = await response.parse()
        assert workload_identity_federation_rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.workload_identity_federation_rules.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workload_identity_federation_rule = await response.parse()
            assert workload_identity_federation_rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workload_identity_federation_rules.with_raw_response.delete(
                "",
            )
