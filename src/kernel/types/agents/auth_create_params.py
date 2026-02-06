# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AuthCreateParams", "Proxy"]


class AuthCreateParams(TypedDict, total=False):
    domain: Required[str]
    """Domain for authentication"""

    profile_name: Required[str]
    """Name of the profile to use for this auth agent"""

    allowed_domains: SequenceNotStr[str]
    """
    Additional domains that are valid for this auth agent's authentication flow
    (besides the primary domain). Useful when login pages redirect to different
    domains.

    The following SSO/OAuth provider domains are automatically allowed by default
    and do not need to be specified:

    - Google: accounts.google.com
    - Microsoft/Azure AD: login.microsoftonline.com, login.live.com
    - Okta: _.okta.com, _.oktapreview.com
    - Auth0: _.auth0.com, _.us.auth0.com, _.eu.auth0.com, _.au.auth0.com
    - Apple: appleid.apple.com
    - GitHub: github.com
    - Facebook/Meta: www.facebook.com
    - LinkedIn: www.linkedin.com
    - Amazon Cognito: \\**.amazoncognito.com
    - OneLogin: \\**.onelogin.com
    - Ping Identity: _.pingone.com, _.pingidentity.com
    """

    credential_name: str
    """Optional name of an existing credential to use for this auth agent.

    If provided, the credential will be linked to the agent and its values will be
    used to auto-fill the login form on invocation.
    """

    login_url: str
    """Optional login page URL.

    If provided, will be stored on the agent and used to skip discovery in future
    invocations.
    """

    proxy: Proxy
    """Optional proxy configuration"""


class Proxy(TypedDict, total=False):
    """Optional proxy configuration"""

    proxy_id: str
    """ID of the proxy to use"""
