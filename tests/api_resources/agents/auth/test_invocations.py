# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.agents import AgentAuthSubmitResponse, AgentAuthInvocationResponse, AuthAgentInvocationCreateResponse
from kernel.types.agents.auth import (
    InvocationExchangeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        invocation = client.agents.auth.invocations.create(
            auth_agent_id="abc123xyz",
        )
        assert_matches_type(AuthAgentInvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        invocation = client.agents.auth.invocations.create(
            auth_agent_id="abc123xyz",
            save_credential_as="my-netflix-login",
        )
        assert_matches_type(AuthAgentInvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.agents.auth.invocations.with_raw_response.create(
            auth_agent_id="abc123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(AuthAgentInvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.agents.auth.invocations.with_streaming_response.create(
            auth_agent_id="abc123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert_matches_type(AuthAgentInvocationCreateResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        invocation = client.agents.auth.invocations.retrieve(
            "invocation_id",
        )
        assert_matches_type(AgentAuthInvocationResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.agents.auth.invocations.with_raw_response.retrieve(
            "invocation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(AgentAuthInvocationResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.agents.auth.invocations.with_streaming_response.retrieve(
            "invocation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert_matches_type(AgentAuthInvocationResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invocation_id` but received ''"):
            client.agents.auth.invocations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_exchange(self, client: Kernel) -> None:
        invocation = client.agents.auth.invocations.exchange(
            invocation_id="invocation_id",
            code="abc123xyz",
        )
        assert_matches_type(InvocationExchangeResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_exchange(self, client: Kernel) -> None:
        response = client.agents.auth.invocations.with_raw_response.exchange(
            invocation_id="invocation_id",
            code="abc123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(InvocationExchangeResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_exchange(self, client: Kernel) -> None:
        with client.agents.auth.invocations.with_streaming_response.exchange(
            invocation_id="invocation_id",
            code="abc123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert_matches_type(InvocationExchangeResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_exchange(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invocation_id` but received ''"):
            client.agents.auth.invocations.with_raw_response.exchange(
                invocation_id="",
                code="abc123xyz",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_overload_1(self, client: Kernel) -> None:
        invocation = client.agents.auth.invocations.submit(
            invocation_id="invocation_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        )
        assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_overload_1(self, client: Kernel) -> None:
        response = client.agents.auth.invocations.with_raw_response.submit(
            invocation_id="invocation_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_overload_1(self, client: Kernel) -> None:
        with client.agents.auth.invocations.with_streaming_response.submit(
            invocation_id="invocation_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_overload_1(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invocation_id` but received ''"):
            client.agents.auth.invocations.with_raw_response.submit(
                invocation_id="",
                field_values={
                    "email": "user@example.com",
                    "password": "********",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_overload_2(self, client: Kernel) -> None:
        invocation = client.agents.auth.invocations.submit(
            invocation_id="invocation_id",
            sso_button="xpath=//button[contains(text(), 'Continue with Google')]",
        )
        assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_overload_2(self, client: Kernel) -> None:
        response = client.agents.auth.invocations.with_raw_response.submit(
            invocation_id="invocation_id",
            sso_button="xpath=//button[contains(text(), 'Continue with Google')]",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_overload_2(self, client: Kernel) -> None:
        with client.agents.auth.invocations.with_streaming_response.submit(
            invocation_id="invocation_id",
            sso_button="xpath=//button[contains(text(), 'Continue with Google')]",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_overload_2(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invocation_id` but received ''"):
            client.agents.auth.invocations.with_raw_response.submit(
                invocation_id="",
                sso_button="xpath=//button[contains(text(), 'Continue with Google')]",
            )


class TestAsyncInvocations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.agents.auth.invocations.create(
            auth_agent_id="abc123xyz",
        )
        assert_matches_type(AuthAgentInvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.agents.auth.invocations.create(
            auth_agent_id="abc123xyz",
            save_credential_as="my-netflix-login",
        )
        assert_matches_type(AuthAgentInvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.invocations.with_raw_response.create(
            auth_agent_id="abc123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(AuthAgentInvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.invocations.with_streaming_response.create(
            auth_agent_id="abc123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert_matches_type(AuthAgentInvocationCreateResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.agents.auth.invocations.retrieve(
            "invocation_id",
        )
        assert_matches_type(AgentAuthInvocationResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.invocations.with_raw_response.retrieve(
            "invocation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(AgentAuthInvocationResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.invocations.with_streaming_response.retrieve(
            "invocation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert_matches_type(AgentAuthInvocationResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invocation_id` but received ''"):
            await async_client.agents.auth.invocations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_exchange(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.agents.auth.invocations.exchange(
            invocation_id="invocation_id",
            code="abc123xyz",
        )
        assert_matches_type(InvocationExchangeResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_exchange(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.invocations.with_raw_response.exchange(
            invocation_id="invocation_id",
            code="abc123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(InvocationExchangeResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_exchange(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.invocations.with_streaming_response.exchange(
            invocation_id="invocation_id",
            code="abc123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert_matches_type(InvocationExchangeResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_exchange(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invocation_id` but received ''"):
            await async_client.agents.auth.invocations.with_raw_response.exchange(
                invocation_id="",
                code="abc123xyz",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_overload_1(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.agents.auth.invocations.submit(
            invocation_id="invocation_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        )
        assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_overload_1(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.invocations.with_raw_response.submit(
            invocation_id="invocation_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_overload_1(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.invocations.with_streaming_response.submit(
            invocation_id="invocation_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_overload_1(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invocation_id` but received ''"):
            await async_client.agents.auth.invocations.with_raw_response.submit(
                invocation_id="",
                field_values={
                    "email": "user@example.com",
                    "password": "********",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_overload_2(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.agents.auth.invocations.submit(
            invocation_id="invocation_id",
            sso_button="xpath=//button[contains(text(), 'Continue with Google')]",
        )
        assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_overload_2(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.invocations.with_raw_response.submit(
            invocation_id="invocation_id",
            sso_button="xpath=//button[contains(text(), 'Continue with Google')]",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_overload_2(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.invocations.with_streaming_response.submit(
            invocation_id="invocation_id",
            sso_button="xpath=//button[contains(text(), 'Continue with Google')]",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert_matches_type(AgentAuthSubmitResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_overload_2(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invocation_id` but received ''"):
            await async_client.agents.auth.invocations.with_raw_response.submit(
                invocation_id="",
                sso_button="xpath=//button[contains(text(), 'Continue with Google')]",
            )
