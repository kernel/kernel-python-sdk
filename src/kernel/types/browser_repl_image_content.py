# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrowserReplImageContent"]


class BrowserReplImageContent(BaseModel):
    data_b64: str

    mime_type: str

    type: Literal["image"]
