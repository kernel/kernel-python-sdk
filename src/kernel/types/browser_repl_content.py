# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .browser_repl_text_content import BrowserReplTextContent
from .browser_repl_image_content import BrowserReplImageContent

__all__ = ["BrowserReplContent"]

BrowserReplContent: TypeAlias = Annotated[
    Union[BrowserReplTextContent, BrowserReplImageContent], PropertyInfo(discriminator="type")
]
