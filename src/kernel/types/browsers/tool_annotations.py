# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ToolAnnotations"]


class ToolAnnotations(BaseModel):
    """
    Tool-provided behavioral hints from the [MCP tool specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#tool)
    and the [WebMCP ToolAnnotations definition](https://webmachinelearning.github.io/webmcp/#dictdef-toolannotations).
    These hints are untrusted and are not enforced by Kernel.
    """

    autosubmit: Optional[bool] = None

    consequential_hint: Optional[bool] = FieldInfo(alias="consequentialHint", default=None)

    destructive_hint: Optional[bool] = FieldInfo(alias="destructiveHint", default=None)

    idempotent_hint: Optional[bool] = FieldInfo(alias="idempotentHint", default=None)

    open_world_hint: Optional[bool] = FieldInfo(alias="openWorldHint", default=None)

    read_only_hint: Optional[bool] = FieldInfo(alias="readOnlyHint", default=None)

    untrusted_content_hint: Optional[bool] = FieldInfo(alias="untrustedContentHint", default=None)
