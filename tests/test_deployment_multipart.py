from __future__ import annotations

import json
from email import policy
from email.parser import BytesParser
from email.message import EmailMessage

import httpx
import pytest
from respx import MockRouter

from kernel import Kernel, AsyncKernel
from kernel.types.deployment_create_params import Source, RuntimePolicy


@pytest.mark.parametrize("use_async", [False, True], ids=["sync", "async"])
async def test_deployment_json_parts(
    client: Kernel, async_client: AsyncKernel, respx_mock: MockRouter, use_async: bool
) -> None:
    route = respx_mock.post("/deployments").mock(return_value=httpx.Response(200, json={}))
    source: Source = {"type": "github", "url": "https://github.com/example/app", "ref": "main", "entrypoint": "app.py"}
    runtime_policy: RuntimePolicy = {"statements": [{"action": "invocations:write", "resource": "*"}]}
    if use_async:
        await async_client.deployments.with_raw_response.create(source=source, runtime_policy=runtime_policy)
    else:
        client.deployments.with_raw_response.create(source=source, runtime_policy=runtime_policy)

    request = route.calls.last.request
    message = BytesParser(EmailMessage, policy=policy.default).parsebytes(
        f"Content-Type: {request.headers['Content-Type']}\r\n\r\n".encode() + request.content
    )
    parts = list(message.iter_parts())
    assert len(parts) == 2
    assert all(part.get_content_type() == "application/json" and part.get_filename() is None for part in parts)
    assert {part.get_param("name", header="content-disposition"): json.loads(part.get_content()) for part in parts} == {
        "source": source,
        "runtime_policy": runtime_policy,
    }
