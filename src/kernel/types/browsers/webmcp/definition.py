# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .match import Match
from ...._models import BaseModel
from ..tool_metadata import ToolMetadata

__all__ = ["Definition"]


class Definition(BaseModel):
    id: str

    kind: str

    match: Match

    namespace: str

    tool: ToolMetadata
    """
    Tool metadata follows the
    [MCP Tool definition](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#tool)
    and the
    [WebMCP RegisteredTool definition](https://webmachinelearning.github.io/webmcp/#dictdef-registeredtool).
    outputSchema is optional for page and custom tools.
    """
