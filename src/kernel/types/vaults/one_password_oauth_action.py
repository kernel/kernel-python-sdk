# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OnePasswordOAuthAction"]


class OnePasswordOAuthAction(BaseModel):
    name: Literal["1password_oauth"]

    url: str
    """1Password-hosted OAuth authorization URL for the human to open."""

    connect_url: Optional[str] = None
    """
    1Password connect link for the same authorization, for the person to open on
    their own device. In 1Password for iOS or Android it opens the app to approve
    the connection. Anywhere else it opens 1Password in the browser, where someone
    without 1Password can sign up; if the account is still pending afterwards, they
    connect with url. Also offer url to people who already use 1Password on a
    computer. Whichever link the person answers first settles the authorization and
    the other stops working. Expires with the account's expires_at; repeat the
    upsert for fresh links. Absent on a recovery link.
    """
