# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ComputerReadClipboardResponse"]


class ComputerReadClipboardResponse(BaseModel):
    text: str
    """Current clipboard text content"""
