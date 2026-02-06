# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from kernel.types.browsers import (
    ComputerGetMousePositionResponse,
    ComputerSetCursorVisibilityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComputer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch(self, client: Kernel) -> None:
        computer = client.browsers.computer.batch(
            id="id",
            actions=[{"type": "click_mouse"}],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.batch(
            id="id",
            actions=[{"type": "click_mouse"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.batch(
            id="id",
            actions=[{"type": "click_mouse"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_batch(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.batch(
                id="",
                actions=[{"type": "click_mouse"}],
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_capture_screenshot(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.post("/browsers/id/computer/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        computer = client.browsers.computer.capture_screenshot(
            id="id",
        )
        assert computer.is_closed
        assert computer.json() == {"foo": "bar"}
        assert cast(Any, computer.is_closed) is True
        assert isinstance(computer, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_capture_screenshot_with_all_params(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.post("/browsers/id/computer/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        computer = client.browsers.computer.capture_screenshot(
            id="id",
            region={
                "height": 0,
                "width": 0,
                "x": 0,
                "y": 0,
            },
        )
        assert computer.is_closed
        assert computer.json() == {"foo": "bar"}
        assert cast(Any, computer.is_closed) is True
        assert isinstance(computer, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_capture_screenshot(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.post("/browsers/id/computer/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        computer = client.browsers.computer.with_raw_response.capture_screenshot(
            id="id",
        )

        assert computer.is_closed is True
        assert computer.http_request.headers.get("X-Stainless-Lang") == "python"
        assert computer.json() == {"foo": "bar"}
        assert isinstance(computer, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_capture_screenshot(self, client: Kernel, respx_mock: MockRouter) -> None:
        respx_mock.post("/browsers/id/computer/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.browsers.computer.with_streaming_response.capture_screenshot(
            id="id",
        ) as computer:
            assert not computer.is_closed
            assert computer.http_request.headers.get("X-Stainless-Lang") == "python"

            assert computer.json() == {"foo": "bar"}
            assert cast(Any, computer.is_closed) is True
            assert isinstance(computer, StreamedBinaryAPIResponse)

        assert cast(Any, computer.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_capture_screenshot(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.capture_screenshot(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_click_mouse(self, client: Kernel) -> None:
        computer = client.browsers.computer.click_mouse(
            id="id",
            x=0,
            y=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_click_mouse_with_all_params(self, client: Kernel) -> None:
        computer = client.browsers.computer.click_mouse(
            id="id",
            x=0,
            y=0,
            button="left",
            click_type="down",
            hold_keys=["string"],
            num_clicks=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_click_mouse(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.click_mouse(
            id="id",
            x=0,
            y=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_click_mouse(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.click_mouse(
            id="id",
            x=0,
            y=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_click_mouse(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.click_mouse(
                id="",
                x=0,
                y=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_drag_mouse(self, client: Kernel) -> None:
        computer = client.browsers.computer.drag_mouse(
            id="id",
            path=[[0, 0], [0, 0]],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_drag_mouse_with_all_params(self, client: Kernel) -> None:
        computer = client.browsers.computer.drag_mouse(
            id="id",
            path=[[0, 0], [0, 0]],
            button="left",
            delay=0,
            hold_keys=["string"],
            step_delay_ms=0,
            steps_per_segment=1,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_drag_mouse(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.drag_mouse(
            id="id",
            path=[[0, 0], [0, 0]],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_drag_mouse(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.drag_mouse(
            id="id",
            path=[[0, 0], [0, 0]],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_drag_mouse(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.drag_mouse(
                id="",
                path=[[0, 0], [0, 0]],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_mouse_position(self, client: Kernel) -> None:
        computer = client.browsers.computer.get_mouse_position(
            "id",
        )
        assert_matches_type(ComputerGetMousePositionResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_mouse_position(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.get_mouse_position(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerGetMousePositionResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_mouse_position(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.get_mouse_position(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerGetMousePositionResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_mouse_position(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.get_mouse_position(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move_mouse(self, client: Kernel) -> None:
        computer = client.browsers.computer.move_mouse(
            id="id",
            x=0,
            y=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move_mouse_with_all_params(self, client: Kernel) -> None:
        computer = client.browsers.computer.move_mouse(
            id="id",
            x=0,
            y=0,
            hold_keys=["string"],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_move_mouse(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.move_mouse(
            id="id",
            x=0,
            y=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_move_mouse(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.move_mouse(
            id="id",
            x=0,
            y=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_move_mouse(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.move_mouse(
                id="",
                x=0,
                y=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_press_key(self, client: Kernel) -> None:
        computer = client.browsers.computer.press_key(
            id="id",
            keys=["string"],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_press_key_with_all_params(self, client: Kernel) -> None:
        computer = client.browsers.computer.press_key(
            id="id",
            keys=["string"],
            duration=0,
            hold_keys=["string"],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_press_key(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.press_key(
            id="id",
            keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_press_key(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.press_key(
            id="id",
            keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_press_key(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.press_key(
                id="",
                keys=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_scroll(self, client: Kernel) -> None:
        computer = client.browsers.computer.scroll(
            id="id",
            x=0,
            y=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_scroll_with_all_params(self, client: Kernel) -> None:
        computer = client.browsers.computer.scroll(
            id="id",
            x=0,
            y=0,
            delta_x=0,
            delta_y=0,
            hold_keys=["string"],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_scroll(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.scroll(
            id="id",
            x=0,
            y=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_scroll(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.scroll(
            id="id",
            x=0,
            y=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_scroll(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.scroll(
                id="",
                x=0,
                y=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_cursor_visibility(self, client: Kernel) -> None:
        computer = client.browsers.computer.set_cursor_visibility(
            id="id",
            hidden=True,
        )
        assert_matches_type(ComputerSetCursorVisibilityResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_cursor_visibility(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.set_cursor_visibility(
            id="id",
            hidden=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert_matches_type(ComputerSetCursorVisibilityResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_cursor_visibility(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.set_cursor_visibility(
            id="id",
            hidden=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert_matches_type(ComputerSetCursorVisibilityResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_set_cursor_visibility(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.set_cursor_visibility(
                id="",
                hidden=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_type_text(self, client: Kernel) -> None:
        computer = client.browsers.computer.type_text(
            id="id",
            text="text",
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_type_text_with_all_params(self, client: Kernel) -> None:
        computer = client.browsers.computer.type_text(
            id="id",
            text="text",
            delay=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_type_text(self, client: Kernel) -> None:
        response = client.browsers.computer.with_raw_response.type_text(
            id="id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_type_text(self, client: Kernel) -> None:
        with client.browsers.computer.with_streaming_response.type_text(
            id="id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_type_text(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.computer.with_raw_response.type_text(
                id="",
                text="text",
            )


class TestAsyncComputer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.batch(
            id="id",
            actions=[{"type": "click_mouse"}],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.batch(
            id="id",
            actions=[{"type": "click_mouse"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.batch(
            id="id",
            actions=[{"type": "click_mouse"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_batch(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.batch(
                id="",
                actions=[{"type": "click_mouse"}],
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_capture_screenshot(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.post("/browsers/id/computer/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        computer = await async_client.browsers.computer.capture_screenshot(
            id="id",
        )
        assert computer.is_closed
        assert await computer.json() == {"foo": "bar"}
        assert cast(Any, computer.is_closed) is True
        assert isinstance(computer, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_capture_screenshot_with_all_params(
        self, async_client: AsyncKernel, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/browsers/id/computer/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        computer = await async_client.browsers.computer.capture_screenshot(
            id="id",
            region={
                "height": 0,
                "width": 0,
                "x": 0,
                "y": 0,
            },
        )
        assert computer.is_closed
        assert await computer.json() == {"foo": "bar"}
        assert cast(Any, computer.is_closed) is True
        assert isinstance(computer, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_capture_screenshot(self, async_client: AsyncKernel, respx_mock: MockRouter) -> None:
        respx_mock.post("/browsers/id/computer/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        computer = await async_client.browsers.computer.with_raw_response.capture_screenshot(
            id="id",
        )

        assert computer.is_closed is True
        assert computer.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await computer.json() == {"foo": "bar"}
        assert isinstance(computer, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_capture_screenshot(
        self, async_client: AsyncKernel, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/browsers/id/computer/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.browsers.computer.with_streaming_response.capture_screenshot(
            id="id",
        ) as computer:
            assert not computer.is_closed
            assert computer.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await computer.json() == {"foo": "bar"}
            assert cast(Any, computer.is_closed) is True
            assert isinstance(computer, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, computer.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_capture_screenshot(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.capture_screenshot(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_click_mouse(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.click_mouse(
            id="id",
            x=0,
            y=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_click_mouse_with_all_params(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.click_mouse(
            id="id",
            x=0,
            y=0,
            button="left",
            click_type="down",
            hold_keys=["string"],
            num_clicks=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_click_mouse(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.click_mouse(
            id="id",
            x=0,
            y=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_click_mouse(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.click_mouse(
            id="id",
            x=0,
            y=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_click_mouse(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.click_mouse(
                id="",
                x=0,
                y=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_drag_mouse(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.drag_mouse(
            id="id",
            path=[[0, 0], [0, 0]],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_drag_mouse_with_all_params(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.drag_mouse(
            id="id",
            path=[[0, 0], [0, 0]],
            button="left",
            delay=0,
            hold_keys=["string"],
            step_delay_ms=0,
            steps_per_segment=1,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_drag_mouse(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.drag_mouse(
            id="id",
            path=[[0, 0], [0, 0]],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_drag_mouse(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.drag_mouse(
            id="id",
            path=[[0, 0], [0, 0]],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_drag_mouse(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.drag_mouse(
                id="",
                path=[[0, 0], [0, 0]],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_mouse_position(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.get_mouse_position(
            "id",
        )
        assert_matches_type(ComputerGetMousePositionResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_mouse_position(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.get_mouse_position(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerGetMousePositionResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_mouse_position(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.get_mouse_position(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerGetMousePositionResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_mouse_position(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.get_mouse_position(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move_mouse(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.move_mouse(
            id="id",
            x=0,
            y=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move_mouse_with_all_params(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.move_mouse(
            id="id",
            x=0,
            y=0,
            hold_keys=["string"],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_move_mouse(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.move_mouse(
            id="id",
            x=0,
            y=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_move_mouse(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.move_mouse(
            id="id",
            x=0,
            y=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_move_mouse(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.move_mouse(
                id="",
                x=0,
                y=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_press_key(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.press_key(
            id="id",
            keys=["string"],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_press_key_with_all_params(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.press_key(
            id="id",
            keys=["string"],
            duration=0,
            hold_keys=["string"],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_press_key(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.press_key(
            id="id",
            keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_press_key(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.press_key(
            id="id",
            keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_press_key(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.press_key(
                id="",
                keys=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_scroll(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.scroll(
            id="id",
            x=0,
            y=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_scroll_with_all_params(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.scroll(
            id="id",
            x=0,
            y=0,
            delta_x=0,
            delta_y=0,
            hold_keys=["string"],
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_scroll(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.scroll(
            id="id",
            x=0,
            y=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_scroll(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.scroll(
            id="id",
            x=0,
            y=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_scroll(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.scroll(
                id="",
                x=0,
                y=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_cursor_visibility(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.set_cursor_visibility(
            id="id",
            hidden=True,
        )
        assert_matches_type(ComputerSetCursorVisibilityResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_cursor_visibility(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.set_cursor_visibility(
            id="id",
            hidden=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert_matches_type(ComputerSetCursorVisibilityResponse, computer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_cursor_visibility(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.set_cursor_visibility(
            id="id",
            hidden=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert_matches_type(ComputerSetCursorVisibilityResponse, computer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_set_cursor_visibility(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.set_cursor_visibility(
                id="",
                hidden=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_type_text(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.type_text(
            id="id",
            text="text",
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_type_text_with_all_params(self, async_client: AsyncKernel) -> None:
        computer = await async_client.browsers.computer.type_text(
            id="id",
            text="text",
            delay=0,
        )
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_type_text(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.computer.with_raw_response.type_text(
            id="id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        computer = await response.parse()
        assert computer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_type_text(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.computer.with_streaming_response.type_text(
            id="id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            computer = await response.parse()
            assert computer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_type_text(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.computer.with_raw_response.type_text(
                id="",
                text="text",
            )
