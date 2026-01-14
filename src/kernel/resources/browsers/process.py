# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.browsers import (
    process_exec_params,
    process_kill_params,
    process_spawn_params,
    process_stdin_params,
    process_resize_params,
)
from ...types.browsers.process_exec_response import ProcessExecResponse
from ...types.browsers.process_kill_response import ProcessKillResponse
from ...types.browsers.process_spawn_response import ProcessSpawnResponse
from ...types.browsers.process_stdin_response import ProcessStdinResponse
from ...types.browsers.process_resize_response import ProcessResizeResponse
from ...types.browsers.process_status_response import ProcessStatusResponse
from ...types.browsers.process_stdout_stream_response import ProcessStdoutStreamResponse

__all__ = ["ProcessResource", "AsyncProcessResource"]


class ProcessResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProcessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProcessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProcessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return ProcessResourceWithStreamingResponse(self)

    def exec(
        self,
        id: str,
        *,
        command: str,
        args: SequenceNotStr[str] | Omit = omit,
        as_root: bool | Omit = omit,
        as_user: Optional[str] | Omit = omit,
        cwd: Optional[str] | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        timeout_sec: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessExecResponse:
        """
        Execute a command synchronously

        Args:
          command: Executable or shell command to run.

          args: Command arguments.

          as_root: Run the process with root privileges.

          as_user: Run the process as this user.

          cwd: Working directory (absolute path) to run the command in.

          env: Environment variables to set for the process.

          timeout_sec: Maximum execution time in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/browsers/{id}/process/exec",
            body=maybe_transform(
                {
                    "command": command,
                    "args": args,
                    "as_root": as_root,
                    "as_user": as_user,
                    "cwd": cwd,
                    "env": env,
                    "timeout_sec": timeout_sec,
                },
                process_exec_params.ProcessExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessExecResponse,
        )

    def kill(
        self,
        process_id: str,
        *,
        id: str,
        signal: Literal["TERM", "KILL", "INT", "HUP"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessKillResponse:
        """
        Send signal to process

        Args:
          signal: Signal to send.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        return self._post(
            f"/browsers/{id}/process/{process_id}/kill",
            body=maybe_transform({"signal": signal}, process_kill_params.ProcessKillParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessKillResponse,
        )

    def resize(
        self,
        process_id: str,
        *,
        id: str,
        cols: int,
        rows: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessResizeResponse:
        """
        Resize a PTY-backed process terminal

        Args:
          cols: New terminal columns.

          rows: New terminal rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        return self._post(
            f"/browsers/{id}/process/{process_id}/resize",
            body=maybe_transform(
                {
                    "cols": cols,
                    "rows": rows,
                },
                process_resize_params.ProcessResizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessResizeResponse,
        )

    def spawn(
        self,
        id: str,
        *,
        command: str,
        allocate_tty: bool | Omit = omit,
        args: SequenceNotStr[str] | Omit = omit,
        as_root: bool | Omit = omit,
        as_user: Optional[str] | Omit = omit,
        cols: int | Omit = omit,
        cwd: Optional[str] | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        rows: int | Omit = omit,
        timeout_sec: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessSpawnResponse:
        """
        Execute a command asynchronously

        Args:
          command: Executable or shell command to run.

          allocate_tty: Allocate a pseudo-terminal (PTY) for interactive shells.

          args: Command arguments.

          as_root: Run the process with root privileges.

          as_user: Run the process as this user.

          cols: Initial terminal columns. Only used when allocate_tty is true.

          cwd: Working directory (absolute path) to run the command in.

          env: Environment variables to set for the process.

          rows: Initial terminal rows. Only used when allocate_tty is true.

          timeout_sec: Maximum execution time in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/browsers/{id}/process/spawn",
            body=maybe_transform(
                {
                    "command": command,
                    "allocate_tty": allocate_tty,
                    "args": args,
                    "as_root": as_root,
                    "as_user": as_user,
                    "cols": cols,
                    "cwd": cwd,
                    "env": env,
                    "rows": rows,
                    "timeout_sec": timeout_sec,
                },
                process_spawn_params.ProcessSpawnParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessSpawnResponse,
        )

    def status(
        self,
        process_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessStatusResponse:
        """
        Get process status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        return self._get(
            f"/browsers/{id}/process/{process_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessStatusResponse,
        )

    def stdin(
        self,
        process_id: str,
        *,
        id: str,
        data_b64: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessStdinResponse:
        """
        Write to process stdin

        Args:
          data_b64: Base64-encoded data to write.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        return self._post(
            f"/browsers/{id}/process/{process_id}/stdin",
            body=maybe_transform({"data_b64": data_b64}, process_stdin_params.ProcessStdinParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessStdinResponse,
        )

    def stdout_stream(
        self,
        process_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ProcessStdoutStreamResponse]:
        """
        Stream process stdout via SSE

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            f"/browsers/{id}/process/{process_id}/stdout/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessStdoutStreamResponse,
            stream=True,
            stream_cls=Stream[ProcessStdoutStreamResponse],
        )


class AsyncProcessResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProcessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProcessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProcessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncProcessResourceWithStreamingResponse(self)

    async def exec(
        self,
        id: str,
        *,
        command: str,
        args: SequenceNotStr[str] | Omit = omit,
        as_root: bool | Omit = omit,
        as_user: Optional[str] | Omit = omit,
        cwd: Optional[str] | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        timeout_sec: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessExecResponse:
        """
        Execute a command synchronously

        Args:
          command: Executable or shell command to run.

          args: Command arguments.

          as_root: Run the process with root privileges.

          as_user: Run the process as this user.

          cwd: Working directory (absolute path) to run the command in.

          env: Environment variables to set for the process.

          timeout_sec: Maximum execution time in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/browsers/{id}/process/exec",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "args": args,
                    "as_root": as_root,
                    "as_user": as_user,
                    "cwd": cwd,
                    "env": env,
                    "timeout_sec": timeout_sec,
                },
                process_exec_params.ProcessExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessExecResponse,
        )

    async def kill(
        self,
        process_id: str,
        *,
        id: str,
        signal: Literal["TERM", "KILL", "INT", "HUP"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessKillResponse:
        """
        Send signal to process

        Args:
          signal: Signal to send.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        return await self._post(
            f"/browsers/{id}/process/{process_id}/kill",
            body=await async_maybe_transform({"signal": signal}, process_kill_params.ProcessKillParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessKillResponse,
        )

    async def resize(
        self,
        process_id: str,
        *,
        id: str,
        cols: int,
        rows: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessResizeResponse:
        """
        Resize a PTY-backed process terminal

        Args:
          cols: New terminal columns.

          rows: New terminal rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        return await self._post(
            f"/browsers/{id}/process/{process_id}/resize",
            body=await async_maybe_transform(
                {
                    "cols": cols,
                    "rows": rows,
                },
                process_resize_params.ProcessResizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessResizeResponse,
        )

    async def spawn(
        self,
        id: str,
        *,
        command: str,
        allocate_tty: bool | Omit = omit,
        args: SequenceNotStr[str] | Omit = omit,
        as_root: bool | Omit = omit,
        as_user: Optional[str] | Omit = omit,
        cols: int | Omit = omit,
        cwd: Optional[str] | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        rows: int | Omit = omit,
        timeout_sec: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessSpawnResponse:
        """
        Execute a command asynchronously

        Args:
          command: Executable or shell command to run.

          allocate_tty: Allocate a pseudo-terminal (PTY) for interactive shells.

          args: Command arguments.

          as_root: Run the process with root privileges.

          as_user: Run the process as this user.

          cols: Initial terminal columns. Only used when allocate_tty is true.

          cwd: Working directory (absolute path) to run the command in.

          env: Environment variables to set for the process.

          rows: Initial terminal rows. Only used when allocate_tty is true.

          timeout_sec: Maximum execution time in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/browsers/{id}/process/spawn",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "allocate_tty": allocate_tty,
                    "args": args,
                    "as_root": as_root,
                    "as_user": as_user,
                    "cols": cols,
                    "cwd": cwd,
                    "env": env,
                    "rows": rows,
                    "timeout_sec": timeout_sec,
                },
                process_spawn_params.ProcessSpawnParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessSpawnResponse,
        )

    async def status(
        self,
        process_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessStatusResponse:
        """
        Get process status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        return await self._get(
            f"/browsers/{id}/process/{process_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessStatusResponse,
        )

    async def stdin(
        self,
        process_id: str,
        *,
        id: str,
        data_b64: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcessStdinResponse:
        """
        Write to process stdin

        Args:
          data_b64: Base64-encoded data to write.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        return await self._post(
            f"/browsers/{id}/process/{process_id}/stdin",
            body=await async_maybe_transform({"data_b64": data_b64}, process_stdin_params.ProcessStdinParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessStdinResponse,
        )

    async def stdout_stream(
        self,
        process_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ProcessStdoutStreamResponse]:
        """
        Stream process stdout via SSE

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not process_id:
            raise ValueError(f"Expected a non-empty value for `process_id` but received {process_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            f"/browsers/{id}/process/{process_id}/stdout/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProcessStdoutStreamResponse,
            stream=True,
            stream_cls=AsyncStream[ProcessStdoutStreamResponse],
        )


class ProcessResourceWithRawResponse:
    def __init__(self, process: ProcessResource) -> None:
        self._process = process

        self.exec = to_raw_response_wrapper(
            process.exec,
        )
        self.kill = to_raw_response_wrapper(
            process.kill,
        )
        self.resize = to_raw_response_wrapper(
            process.resize,
        )
        self.spawn = to_raw_response_wrapper(
            process.spawn,
        )
        self.status = to_raw_response_wrapper(
            process.status,
        )
        self.stdin = to_raw_response_wrapper(
            process.stdin,
        )
        self.stdout_stream = to_raw_response_wrapper(
            process.stdout_stream,
        )


class AsyncProcessResourceWithRawResponse:
    def __init__(self, process: AsyncProcessResource) -> None:
        self._process = process

        self.exec = async_to_raw_response_wrapper(
            process.exec,
        )
        self.kill = async_to_raw_response_wrapper(
            process.kill,
        )
        self.resize = async_to_raw_response_wrapper(
            process.resize,
        )
        self.spawn = async_to_raw_response_wrapper(
            process.spawn,
        )
        self.status = async_to_raw_response_wrapper(
            process.status,
        )
        self.stdin = async_to_raw_response_wrapper(
            process.stdin,
        )
        self.stdout_stream = async_to_raw_response_wrapper(
            process.stdout_stream,
        )


class ProcessResourceWithStreamingResponse:
    def __init__(self, process: ProcessResource) -> None:
        self._process = process

        self.exec = to_streamed_response_wrapper(
            process.exec,
        )
        self.kill = to_streamed_response_wrapper(
            process.kill,
        )
        self.resize = to_streamed_response_wrapper(
            process.resize,
        )
        self.spawn = to_streamed_response_wrapper(
            process.spawn,
        )
        self.status = to_streamed_response_wrapper(
            process.status,
        )
        self.stdin = to_streamed_response_wrapper(
            process.stdin,
        )
        self.stdout_stream = to_streamed_response_wrapper(
            process.stdout_stream,
        )


class AsyncProcessResourceWithStreamingResponse:
    def __init__(self, process: AsyncProcessResource) -> None:
        self._process = process

        self.exec = async_to_streamed_response_wrapper(
            process.exec,
        )
        self.kill = async_to_streamed_response_wrapper(
            process.kill,
        )
        self.resize = async_to_streamed_response_wrapper(
            process.resize,
        )
        self.spawn = async_to_streamed_response_wrapper(
            process.spawn,
        )
        self.status = async_to_streamed_response_wrapper(
            process.status,
        )
        self.stdin = async_to_streamed_response_wrapper(
            process.stdin,
        )
        self.stdout_stream = async_to_streamed_response_wrapper(
            process.stdout_stream,
        )
