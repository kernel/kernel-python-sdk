# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.browsers import (
    ProcessExecResponse,
    ProcessKillResponse,
    ProcessSpawnResponse,
    ProcessStdinResponse,
    ProcessResizeResponse,
    ProcessStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProcess:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_exec(self, client: Kernel) -> None:
        process = client.browsers.process.exec(
            id="id",
            command="command",
        )
        assert_matches_type(ProcessExecResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_exec_with_all_params(self, client: Kernel) -> None:
        process = client.browsers.process.exec(
            id="id",
            command="command",
            args=["string"],
            as_root=True,
            as_user="as_user",
            cwd="/J!",
            env={"foo": "string"},
            timeout_sec=0,
        )
        assert_matches_type(ProcessExecResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_exec(self, client: Kernel) -> None:
        response = client.browsers.process.with_raw_response.exec(
            id="id",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(ProcessExecResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_exec(self, client: Kernel) -> None:
        with client.browsers.process.with_streaming_response.exec(
            id="id",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(ProcessExecResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_exec(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.process.with_raw_response.exec(
                id="",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_kill(self, client: Kernel) -> None:
        process = client.browsers.process.kill(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            signal="TERM",
        )
        assert_matches_type(ProcessKillResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_kill(self, client: Kernel) -> None:
        response = client.browsers.process.with_raw_response.kill(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            signal="TERM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(ProcessKillResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_kill(self, client: Kernel) -> None:
        with client.browsers.process.with_streaming_response.kill(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            signal="TERM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(ProcessKillResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_kill(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.process.with_raw_response.kill(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
                signal="TERM",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            client.browsers.process.with_raw_response.kill(
                process_id="",
                id="id",
                signal="TERM",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resize(self, client: Kernel) -> None:
        process = client.browsers.process.resize(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            cols=1,
            rows=1,
        )
        assert_matches_type(ProcessResizeResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resize(self, client: Kernel) -> None:
        response = client.browsers.process.with_raw_response.resize(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            cols=1,
            rows=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(ProcessResizeResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resize(self, client: Kernel) -> None:
        with client.browsers.process.with_streaming_response.resize(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            cols=1,
            rows=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(ProcessResizeResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resize(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.process.with_raw_response.resize(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
                cols=1,
                rows=1,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            client.browsers.process.with_raw_response.resize(
                process_id="",
                id="id",
                cols=1,
                rows=1,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_spawn(self, client: Kernel) -> None:
        process = client.browsers.process.spawn(
            id="id",
            command="command",
        )
        assert_matches_type(ProcessSpawnResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_spawn_with_all_params(self, client: Kernel) -> None:
        process = client.browsers.process.spawn(
            id="id",
            command="command",
            allocate_tty=True,
            args=["string"],
            as_root=True,
            as_user="as_user",
            cols=1,
            cwd="/J!",
            env={"foo": "string"},
            rows=1,
            timeout_sec=0,
        )
        assert_matches_type(ProcessSpawnResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_spawn(self, client: Kernel) -> None:
        response = client.browsers.process.with_raw_response.spawn(
            id="id",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(ProcessSpawnResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_spawn(self, client: Kernel) -> None:
        with client.browsers.process.with_streaming_response.spawn(
            id="id",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(ProcessSpawnResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_spawn(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.process.with_raw_response.spawn(
                id="",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_status(self, client: Kernel) -> None:
        process = client.browsers.process.status(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )
        assert_matches_type(ProcessStatusResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Kernel) -> None:
        response = client.browsers.process.with_raw_response.status(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(ProcessStatusResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Kernel) -> None:
        with client.browsers.process.with_streaming_response.status(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(ProcessStatusResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.process.with_raw_response.status(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            client.browsers.process.with_raw_response.status(
                process_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stdin(self, client: Kernel) -> None:
        process = client.browsers.process.stdin(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            data_b64="data_b64",
        )
        assert_matches_type(ProcessStdinResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stdin(self, client: Kernel) -> None:
        response = client.browsers.process.with_raw_response.stdin(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            data_b64="data_b64",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(ProcessStdinResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stdin(self, client: Kernel) -> None:
        with client.browsers.process.with_streaming_response.stdin(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            data_b64="data_b64",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(ProcessStdinResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stdin(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.process.with_raw_response.stdin(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
                data_b64="data_b64",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            client.browsers.process.with_raw_response.stdin(
                process_id="",
                id="id",
                data_b64="data_b64",
            )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_stdout_stream(self, client: Kernel) -> None:
        process_stream = client.browsers.process.stdout_stream(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )
        process_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_stdout_stream(self, client: Kernel) -> None:
        response = client.browsers.process.with_raw_response.stdout_stream(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_stdout_stream(self, client: Kernel) -> None:
        with client.browsers.process.with_streaming_response.stdout_stream(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_path_params_stdout_stream(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.process.with_raw_response.stdout_stream(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            client.browsers.process.with_raw_response.stdout_stream(
                process_id="",
                id="id",
            )


class TestAsyncProcess:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_exec(self, async_client: AsyncKernel) -> None:
        process = await async_client.browsers.process.exec(
            id="id",
            command="command",
        )
        assert_matches_type(ProcessExecResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_exec_with_all_params(self, async_client: AsyncKernel) -> None:
        process = await async_client.browsers.process.exec(
            id="id",
            command="command",
            args=["string"],
            as_root=True,
            as_user="as_user",
            cwd="/J!",
            env={"foo": "string"},
            timeout_sec=0,
        )
        assert_matches_type(ProcessExecResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_exec(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.process.with_raw_response.exec(
            id="id",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(ProcessExecResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_exec(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.process.with_streaming_response.exec(
            id="id",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(ProcessExecResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_exec(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.process.with_raw_response.exec(
                id="",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_kill(self, async_client: AsyncKernel) -> None:
        process = await async_client.browsers.process.kill(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            signal="TERM",
        )
        assert_matches_type(ProcessKillResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_kill(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.process.with_raw_response.kill(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            signal="TERM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(ProcessKillResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_kill(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.process.with_streaming_response.kill(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            signal="TERM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(ProcessKillResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_kill(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.process.with_raw_response.kill(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
                signal="TERM",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            await async_client.browsers.process.with_raw_response.kill(
                process_id="",
                id="id",
                signal="TERM",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resize(self, async_client: AsyncKernel) -> None:
        process = await async_client.browsers.process.resize(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            cols=1,
            rows=1,
        )
        assert_matches_type(ProcessResizeResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.process.with_raw_response.resize(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            cols=1,
            rows=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(ProcessResizeResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.process.with_streaming_response.resize(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            cols=1,
            rows=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(ProcessResizeResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resize(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.process.with_raw_response.resize(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
                cols=1,
                rows=1,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            await async_client.browsers.process.with_raw_response.resize(
                process_id="",
                id="id",
                cols=1,
                rows=1,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_spawn(self, async_client: AsyncKernel) -> None:
        process = await async_client.browsers.process.spawn(
            id="id",
            command="command",
        )
        assert_matches_type(ProcessSpawnResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_spawn_with_all_params(self, async_client: AsyncKernel) -> None:
        process = await async_client.browsers.process.spawn(
            id="id",
            command="command",
            allocate_tty=True,
            args=["string"],
            as_root=True,
            as_user="as_user",
            cols=1,
            cwd="/J!",
            env={"foo": "string"},
            rows=1,
            timeout_sec=0,
        )
        assert_matches_type(ProcessSpawnResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_spawn(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.process.with_raw_response.spawn(
            id="id",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(ProcessSpawnResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_spawn(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.process.with_streaming_response.spawn(
            id="id",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(ProcessSpawnResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_spawn(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.process.with_raw_response.spawn(
                id="",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncKernel) -> None:
        process = await async_client.browsers.process.status(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )
        assert_matches_type(ProcessStatusResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.process.with_raw_response.status(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(ProcessStatusResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.process.with_streaming_response.status(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(ProcessStatusResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.process.with_raw_response.status(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            await async_client.browsers.process.with_raw_response.status(
                process_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stdin(self, async_client: AsyncKernel) -> None:
        process = await async_client.browsers.process.stdin(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            data_b64="data_b64",
        )
        assert_matches_type(ProcessStdinResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stdin(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.process.with_raw_response.stdin(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            data_b64="data_b64",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(ProcessStdinResponse, process, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stdin(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.process.with_streaming_response.stdin(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            data_b64="data_b64",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(ProcessStdinResponse, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stdin(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.process.with_raw_response.stdin(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
                data_b64="data_b64",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            await async_client.browsers.process.with_raw_response.stdin(
                process_id="",
                id="id",
                data_b64="data_b64",
            )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_stdout_stream(self, async_client: AsyncKernel) -> None:
        process_stream = await async_client.browsers.process.stdout_stream(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )
        await process_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_stdout_stream(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.process.with_raw_response.stdout_stream(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_stdout_stream(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.process.with_streaming_response.stdout_stream(
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_path_params_stdout_stream(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.process.with_raw_response.stdout_stream(
                process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `process_id` but received ''"):
            await async_client.browsers.process.with_raw_response.stdout_stream(
                process_id="",
                id="id",
            )
