from ._cache import TokenCache as TokenCache
from ._chain import default_credentials as default_credentials
from ._types import (
    Principal as Principal,
    AccessToken as AccessToken,
    AccessTokenProvider as AccessTokenProvider,
    FederationAccessToken as FederationAccessToken,
    IdentityTokenProvider as IdentityTokenProvider,
    AsyncAccessTokenProvider as AsyncAccessTokenProvider,
    AsyncIdentityTokenProvider as AsyncIdentityTokenProvider,
)
from ._errors import WorkloadIdentityError as WorkloadIdentityError
from ._workload import (
    WorkloadIdentityCredentials as WorkloadIdentityCredentials,
    exchange_federation_assertion as exchange_federation_assertion,
    async_exchange_federation_assertion as async_exchange_federation_assertion,
)
from ._providers import (
    IdentityTokenFile as IdentityTokenFile,
    AWSSTSIdentityToken as AWSSTSIdentityToken,
    StaticIdentityToken as StaticIdentityToken,
    GCPMetadataIdentityToken as GCPMetadataIdentityToken,
    GitHubActionsIdentityToken as GitHubActionsIdentityToken,
)

__all__ = [
    "AccessToken",
    "FederationAccessToken",
    "Principal",
    "AccessTokenProvider",
    "AsyncAccessTokenProvider",
    "IdentityTokenProvider",
    "AsyncIdentityTokenProvider",
    "WorkloadIdentityCredentials",
    "WorkloadIdentityError",
    "exchange_federation_assertion",
    "async_exchange_federation_assertion",
    "IdentityTokenFile",
    "StaticIdentityToken",
    "GitHubActionsIdentityToken",
    "GCPMetadataIdentityToken",
    "AWSSTSIdentityToken",
    "TokenCache",
    "default_credentials",
]
