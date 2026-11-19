# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AuthContextWorkloadIdentity"]


class AuthContextWorkloadIdentity(BaseModel):
    external_subject_digest: str
    """Digest of the verified external subject.

    Never the original assertion or arbitrary claims.
    """

    federation_rule_id: str

    issuer_id: str
