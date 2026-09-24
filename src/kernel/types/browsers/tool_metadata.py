# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tool_annotations import ToolAnnotations

__all__ = ["ToolMetadata"]


class ToolMetadata(BaseModel):
    """
    Tool metadata follows the [MCP Tool definition](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#tool)
    and the [WebMCP RegisteredTool definition](https://webmachinelearning.github.io/webmcp/#dictdef-registeredtool).
    outputSchema is optional for page and custom tools.
    """

    description: str

    input_schema: Dict[str, object] = FieldInfo(alias="inputSchema")

    name: str

    annotations: Optional[ToolAnnotations] = None
    """
    Tool-provided behavioral hints from the
    [MCP tool specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#tool)
    and the
    [WebMCP ToolAnnotations definition](https://webmachinelearning.github.io/webmcp/#dictdef-toolannotations).
    These hints are untrusted and are not enforced by Kernel.
    """

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    title: Optional[str] = None
