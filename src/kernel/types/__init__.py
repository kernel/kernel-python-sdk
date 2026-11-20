# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import browsers
from .. import _compat
from .tags import Tags as Tags
from .task import Task as Task
from .proxy import Proxy as Proxy
from .usage import Usage as Usage
from .vault import Vault as Vault
from .report import Report as Report
from .result import Result as Result
from .search import Search as Search
from .shared import (
    LogEvent as LogEvent,
    AppAction as AppAction,
    ErrorEvent as ErrorEvent,
    ErrorModel as ErrorModel,
    ErrorDetail as ErrorDetail,
    BrowserProfile as BrowserProfile,
    HeartbeatEvent as HeartbeatEvent,
    BrowserViewport as BrowserViewport,
    BrowserExtension as BrowserExtension,
)
from .target import Target as Target
from .api_key import APIKey as APIKey
from .attempt import Attempt as Attempt
from .browser import Browser as Browser
from .profile import Profile as Profile
from .project import Project as Project
from .warning import Warning as Warning
from .analysis import Analysis as Analysis
from .evidence import Evidence as Evidence
from .proxy_ip import ProxyIP as ProxyIP
from .credential import Credential as Credential
from .tags_param import TagsParam as TagsParam
from .report_type import ReportType as ReportType
from .browser_cost import BrowserCost as BrowserCost
from .browser_pool import BrowserPool as BrowserPool
from .browser_proxy import BrowserProxy as BrowserProxy
from .browser_usage import BrowserUsage as BrowserUsage
from .task_metadata import TaskMetadata as TaskMetadata
from .browser_memory import BrowserMemory as BrowserMemory
from .recommendation import Recommendation as Recommendation
from .strategy_param import StrategyParam as StrategyParam
from .app_list_params import AppListParams as AppListParams
from .audit_log_entry import AuditLogEntry as AuditLogEntry
from .created_api_key import CreatedAPIKey as CreatedAPIKey
from .lookup_response import LookupResponse as LookupResponse
from .proxy_ip_detail import ProxyIPDetail as ProxyIPDetail
from .service_account import ServiceAccount as ServiceAccount
from .vault_reference import VaultReference as VaultReference
from .analysis_summary import AnalysisSummary as AnalysisSummary
from .browser_location import BrowserLocation as BrowserLocation
from .browser_pool_ref import BrowserPoolRef as BrowserPoolRef
from .task_list_params import TaskListParams as TaskListParams
from .api_key_principal import APIKeyPrincipal as APIKeyPrincipal
from .app_list_response import AppListResponse as AppListResponse
from .no_recommendation import NoRecommendation as NoRecommendation
from .proxy_list_params import ProxyListParams as ProxyListParams
from .vault_list_params import VaultListParams as VaultListParams
from .browser_proxy_mode import BrowserProxyMode as BrowserProxyMode
from .proxy_check_params import ProxyCheckParams as ProxyCheckParams
from .report_list_params import ReportListParams as ReportListParams
from .task_create_params import TaskCreateParams as TaskCreateParams
from .api_key_list_params import APIKeyListParams as APIKeyListParams
from .browser_curl_params import BrowserCurlParams as BrowserCurlParams
from .browser_fingerprint import BrowserFingerprint as BrowserFingerprint
from .browser_list_params import BrowserListParams as BrowserListParams
from .browser_repl_params import BrowserReplParams as BrowserReplParams
from .browser_repl_result import BrowserReplResult as BrowserReplResult
from .credential_provider import CredentialProvider as CredentialProvider
from .profile_list_params import ProfileListParams as ProfileListParams
from .project_list_params import ProjectListParams as ProjectListParams
from .proxy_create_params import ProxyCreateParams as ProxyCreateParams
from .proxy_list_response import ProxyListResponse as ProxyListResponse
from .proxy_update_params import ProxyUpdateParams as ProxyUpdateParams
from .report_type_summary import ReportTypeSummary as ReportTypeSummary
from .task_metadata_param import TaskMetadataParam as TaskMetadataParam
from .vault_upsert_params import VaultUpsertParams as VaultUpsertParams
from .browser_proxy_config import BrowserProxyConfig as BrowserProxyConfig
from .browser_repl_content import BrowserReplContent as BrowserReplContent
from .browser_video_memory import BrowserVideoMemory as BrowserVideoMemory
from .proxy_check_response import ProxyCheckResponse as ProxyCheckResponse
from .proxy_ip_list_params import ProxyIPListParams as ProxyIPListParams
from .report_create_params import ReportCreateParams as ReportCreateParams
from .search_create_params import SearchCreateParams as SearchCreateParams
from .vault_encryption_key import VaultEncryptionKey as VaultEncryptionKey
from .api_key_create_params import APIKeyCreateParams as APIKeyCreateParams
from .api_key_rotate_params import APIKeyRotateParams as APIKeyRotateParams
from .api_key_update_params import APIKeyUpdateParams as APIKeyUpdateParams
from .audit_log_list_params import AuditLogListParams as AuditLogListParams
from .browser_create_params import BrowserCreateParams as BrowserCreateParams
from .browser_curl_response import BrowserCurlResponse as BrowserCurlResponse
from .browser_list_response import BrowserListResponse as BrowserListResponse
from .browser_update_params import BrowserUpdateParams as BrowserUpdateParams
from .extension_list_params import ExtensionListParams as ExtensionListParams
from .profile_create_params import ProfileCreateParams as ProfileCreateParams
from .profile_update_params import ProfileUpdateParams as ProfileUpdateParams
from .project_create_params import ProjectCreateParams as ProjectCreateParams
from .project_update_params import ProjectUpdateParams as ProjectUpdateParams
from .provider_target_param import ProviderTargetParam as ProviderTargetParam
from .proxy_create_response import ProxyCreateResponse as ProxyCreateResponse
from .proxy_update_response import ProxyUpdateResponse as ProxyUpdateResponse
from .recommendation_result import RecommendationResult as RecommendationResult
from .vault_provider_config import VaultProviderConfig as VaultProviderConfig
from .vault_reference_param import VaultReferenceParam as VaultReferenceParam
from .browser_captcha_solver import BrowserCaptchaSolver as BrowserCaptchaSolver
from .browser_memory_request import BrowserMemoryRequest as BrowserMemoryRequest
from .browser_network_config import BrowserNetworkConfig as BrowserNetworkConfig
from .credential_list_params import CredentialListParams as CredentialListParams
from .deployment_list_params import DeploymentListParams as DeploymentListParams
from .deployment_state_event import DeploymentStateEvent as DeploymentStateEvent
from .extension_get_response import ExtensionGetResponse as ExtensionGetResponse
from .invocation_list_params import InvocationListParams as InvocationListParams
from .invocation_state_event import InvocationStateEvent as InvocationStateEvent
from .recommendation_summary import RecommendationSummary as RecommendationSummary
from .api_key_retrieve_params import APIKeyRetrieveParams as APIKeyRetrieveParams
from .browser_allowlist_state import BrowserAllowlistState as BrowserAllowlistState
from .browser_create_response import BrowserCreateResponse as BrowserCreateResponse
from .browser_location_source import BrowserLocationSource as BrowserLocationSource
from .browser_retrieve_params import BrowserRetrieveParams as BrowserRetrieveParams
from .browser_update_response import BrowserUpdateResponse as BrowserUpdateResponse
from .extension_list_response import ExtensionListResponse as ExtensionListResponse
from .extension_upload_params import ExtensionUploadParams as ExtensionUploadParams
from .profile_download_params import ProfileDownloadParams as ProfileDownloadParams
from .proxy_retrieve_response import ProxyRetrieveResponse as ProxyRetrieveResponse
from .report_type_list_params import ReportTypeListParams as ReportTypeListParams
from .workload_identity_match import WorkloadIdentityMatch as WorkloadIdentityMatch
from .browser_pool_list_params import BrowserPoolListParams as BrowserPoolListParams
from .config_registry_response import ConfigRegistryResponse as ConfigRegistryResponse
from .credential_create_params import CredentialCreateParams as CredentialCreateParams
from .credential_provider_item import CredentialProviderItem as CredentialProviderItem
from .credential_update_params import CredentialUpdateParams as CredentialUpdateParams
from .deployment_create_params import DeploymentCreateParams as DeploymentCreateParams
from .deployment_follow_params import DeploymentFollowParams as DeploymentFollowParams
from .deployment_list_response import DeploymentListResponse as DeploymentListResponse
from .invocation_create_params import InvocationCreateParams as InvocationCreateParams
from .invocation_follow_params import InvocationFollowParams as InvocationFollowParams
from .invocation_list_response import InvocationListResponse as InvocationListResponse
from .invocation_update_params import InvocationUpdateParams as InvocationUpdateParams
from .workload_identity_issuer import WorkloadIdentityIssuer as WorkloadIdentityIssuer
from .workload_identity_target import WorkloadIdentityTarget as WorkloadIdentityTarget
from .browser_fingerprint_param import BrowserFingerprintParam as BrowserFingerprintParam
from .browser_repl_text_content import BrowserReplTextContent as BrowserReplTextContent
from .browser_retrieve_response import BrowserRetrieveResponse as BrowserRetrieveResponse
from .extension_upload_response import ExtensionUploadResponse as ExtensionUploadResponse
from .task_link_browsers_params import TaskLinkBrowsersParams as TaskLinkBrowsersParams
from .browser_pool_create_params import BrowserPoolCreateParams as BrowserPoolCreateParams
from .browser_pool_delete_params import BrowserPoolDeleteParams as BrowserPoolDeleteParams
from .browser_pool_update_params import BrowserPoolUpdateParams as BrowserPoolUpdateParams
from .browser_proxy_config_param import BrowserProxyConfigParam as BrowserProxyConfigParam
from .browser_repl_image_content import BrowserReplImageContent as BrowserReplImageContent
from .deployment_create_response import DeploymentCreateResponse as DeploymentCreateResponse
from .deployment_follow_response import DeploymentFollowResponse as DeploymentFollowResponse
from .invocation_create_response import InvocationCreateResponse as InvocationCreateResponse
from .invocation_follow_response import InvocationFollowResponse as InvocationFollowResponse
from .invocation_update_response import InvocationUpdateResponse as InvocationUpdateResponse
from .browser_pool_acquire_params import BrowserPoolAcquireParams as BrowserPoolAcquireParams
from .browser_pool_release_params import BrowserPoolReleaseParams as BrowserPoolReleaseParams
from .browser_save_profile_params import BrowserSaveProfileParams as BrowserSaveProfileParams
from .config_registry_list_params import ConfigRegistryListParams as ConfigRegistryListParams
from .report_type_version_summary import ReportTypeVersionSummary as ReportTypeVersionSummary
from .service_account_list_params import ServiceAccountListParams as ServiceAccountListParams
from .browser_captcha_solver_param import BrowserCaptchaSolverParam as BrowserCaptchaSolverParam
from .browser_network_config_param import BrowserNetworkConfigParam as BrowserNetworkConfigParam
from .browser_network_update_param import BrowserNetworkUpdateParam as BrowserNetworkUpdateParam
from .deployment_retrieve_response import DeploymentRetrieveResponse as DeploymentRetrieveResponse
from .invocation_retrieve_response import InvocationRetrieveResponse as InvocationRetrieveResponse
from .workload_identity_key_source import WorkloadIdentityKeySource as WorkloadIdentityKeySource
from .audit_log_export_chunk_params import AuditLogExportChunkParams as AuditLogExportChunkParams
from .browser_allowlist_state_param import BrowserAllowlistStateParam as BrowserAllowlistStateParam
from .browser_pool_acquire_response import BrowserPoolAcquireResponse as BrowserPoolAcquireResponse
from .config_registry_lookup_params import ConfigRegistryLookupParams as ConfigRegistryLookupParams
from .credential_totp_code_response import CredentialTotpCodeResponse as CredentialTotpCodeResponse
from .service_account_create_params import ServiceAccountCreateParams as ServiceAccountCreateParams
from .service_account_update_params import ServiceAccountUpdateParams as ServiceAccountUpdateParams
from .workload_identity_match_param import WorkloadIdentityMatchParam as WorkloadIdentityMatchParam
from .workload_identity_preset_type import WorkloadIdentityPresetType as WorkloadIdentityPresetType
from .browser_load_extensions_params import BrowserLoadExtensionsParams as BrowserLoadExtensionsParams
from .browser_location_request_param import BrowserLocationRequestParam as BrowserLocationRequestParam
from .config_registry_resolve_params import ConfigRegistryResolveParams as ConfigRegistryResolveParams
from .workload_identity_target_param import WorkloadIdentityTargetParam as WorkloadIdentityTargetParam
from .credential_provider_list_params import CredentialProviderListParams as CredentialProviderListParams
from .credential_provider_test_result import CredentialProviderTestResult as CredentialProviderTestResult
from .workload_identity_authorization import WorkloadIdentityAuthorization as WorkloadIdentityAuthorization
from .credential_provider_create_params import CredentialProviderCreateParams as CredentialProviderCreateParams
from .credential_provider_update_params import CredentialProviderUpdateParams as CredentialProviderUpdateParams
from .invocation_list_browsers_response import InvocationListBrowsersResponse as InvocationListBrowsersResponse
from .vault_provider_config_list_params import VaultProviderConfigListParams as VaultProviderConfigListParams
from .workload_identity_federation_rule import WorkloadIdentityFederationRule as WorkloadIdentityFederationRule
from .workload_identity_issuer_key_check import WorkloadIdentityIssuerKeyCheck as WorkloadIdentityIssuerKeyCheck
from .workload_identity_key_source_param import WorkloadIdentityKeySourceParam as WorkloadIdentityKeySourceParam
from .workload_identity_token_validation import WorkloadIdentityTokenValidation as WorkloadIdentityTokenValidation
from .vault_provider_config_create_params import VaultProviderConfigCreateParams as VaultProviderConfigCreateParams
from .vault_provider_config_update_params import VaultProviderConfigUpdateParams as VaultProviderConfigUpdateParams
from .workload_identity_issuer_list_params import WorkloadIdentityIssuerListParams as WorkloadIdentityIssuerListParams
from .browser_location_update_request_param import (
    BrowserLocationUpdateRequestParam as BrowserLocationUpdateRequestParam,
)
from .workload_identity_authorization_param import (
    WorkloadIdentityAuthorizationParam as WorkloadIdentityAuthorizationParam,
)
from .workload_identity_authentication_event import (
    WorkloadIdentityAuthenticationEvent as WorkloadIdentityAuthenticationEvent,
)
from .workload_identity_issuer_create_params import (
    WorkloadIdentityIssuerCreateParams as WorkloadIdentityIssuerCreateParams,
)
from .workload_identity_issuer_update_params import (
    WorkloadIdentityIssuerUpdateParams as WorkloadIdentityIssuerUpdateParams,
)
from .credential_provider_list_items_response import (
    CredentialProviderListItemsResponse as CredentialProviderListItemsResponse,
)
from .workload_identity_token_validation_param import (
    WorkloadIdentityTokenValidationParam as WorkloadIdentityTokenValidationParam,
)
from .extension_download_from_chrome_store_params import (
    ExtensionDownloadFromChromeStoreParams as ExtensionDownloadFromChromeStoreParams,
)
from .workload_identity_federation_rule_list_params import (
    WorkloadIdentityFederationRuleListParams as WorkloadIdentityFederationRuleListParams,
)
from .workload_identity_federation_rule_create_params import (
    WorkloadIdentityFederationRuleCreateParams as WorkloadIdentityFederationRuleCreateParams,
)
from .workload_identity_federation_rule_update_params import (
    WorkloadIdentityFederationRuleUpdateParams as WorkloadIdentityFederationRuleUpdateParams,
)
from .workload_identity_authentication_event_list_params import (
    WorkloadIdentityAuthenticationEventListParams as WorkloadIdentityAuthenticationEventListParams,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    browsers.browser_call_stack.BrowserCallStack.update_forward_refs()  # type: ignore
    browsers.browser_console_error_event.BrowserConsoleErrorEvent.update_forward_refs()  # type: ignore
    browsers.browser_console_log_event.BrowserConsoleLogEvent.update_forward_refs()  # type: ignore
    browsers.telemetry_events_response.TelemetryEventsResponse.update_forward_refs()  # type: ignore
    browsers.telemetry_stream_response.TelemetryStreamResponse.update_forward_refs()  # type: ignore
else:
    browsers.browser_call_stack.BrowserCallStack.model_rebuild(_parent_namespace_depth=0)
    browsers.browser_console_error_event.BrowserConsoleErrorEvent.model_rebuild(_parent_namespace_depth=0)
    browsers.browser_console_log_event.BrowserConsoleLogEvent.model_rebuild(_parent_namespace_depth=0)
    browsers.telemetry_events_response.TelemetryEventsResponse.model_rebuild(_parent_namespace_depth=0)
    browsers.telemetry_stream_response.TelemetryStreamResponse.model_rebuild(_parent_namespace_depth=0)
