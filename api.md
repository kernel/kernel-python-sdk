# Shared Types

```python
from kernel.types import (
    AppAction,
    BrowserExtension,
    BrowserProfile,
    BrowserViewport,
    ErrorDetail,
    ErrorEvent,
    ErrorModel,
    HeartbeatEvent,
    LogEvent,
)
```

# Deployments

Types:

```python
from kernel.types import (
    DeploymentStateEvent,
    DeploymentCreateResponse,
    DeploymentRetrieveResponse,
    DeploymentListResponse,
    DeploymentFollowResponse,
)
```

Methods:

- <code title="post /deployments">client.deployments.<a href="./src/kernel/resources/deployments.py">create</a>(\*\*<a href="src/kernel/types/deployment_create_params.py">params</a>) -> <a href="./src/kernel/types/deployment_create_response.py">DeploymentCreateResponse</a></code>
- <code title="get /deployments/{id}">client.deployments.<a href="./src/kernel/resources/deployments.py">retrieve</a>(id) -> <a href="./src/kernel/types/deployment_retrieve_response.py">DeploymentRetrieveResponse</a></code>
- <code title="get /deployments">client.deployments.<a href="./src/kernel/resources/deployments.py">list</a>(\*\*<a href="src/kernel/types/deployment_list_params.py">params</a>) -> <a href="./src/kernel/types/deployment_list_response.py">SyncOffsetPagination[DeploymentListResponse]</a></code>
- <code title="get /deployments/{id}/events">client.deployments.<a href="./src/kernel/resources/deployments.py">follow</a>(id, \*\*<a href="src/kernel/types/deployment_follow_params.py">params</a>) -> <a href="./src/kernel/types/deployment_follow_response.py">DeploymentFollowResponse</a></code>

# Apps

Types:

```python
from kernel.types import AppListResponse
```

Methods:

- <code title="get /apps">client.apps.<a href="./src/kernel/resources/apps.py">list</a>(\*\*<a href="src/kernel/types/app_list_params.py">params</a>) -> <a href="./src/kernel/types/app_list_response.py">SyncOffsetPagination[AppListResponse]</a></code>

# Invocations

Types:

```python
from kernel.types import (
    InvocationStateEvent,
    InvocationCreateResponse,
    InvocationRetrieveResponse,
    InvocationUpdateResponse,
    InvocationListResponse,
    InvocationFollowResponse,
)
```

Methods:

- <code title="post /invocations">client.invocations.<a href="./src/kernel/resources/invocations.py">create</a>(\*\*<a href="src/kernel/types/invocation_create_params.py">params</a>) -> <a href="./src/kernel/types/invocation_create_response.py">InvocationCreateResponse</a></code>
- <code title="get /invocations/{id}">client.invocations.<a href="./src/kernel/resources/invocations.py">retrieve</a>(id) -> <a href="./src/kernel/types/invocation_retrieve_response.py">InvocationRetrieveResponse</a></code>
- <code title="patch /invocations/{id}">client.invocations.<a href="./src/kernel/resources/invocations.py">update</a>(id, \*\*<a href="src/kernel/types/invocation_update_params.py">params</a>) -> <a href="./src/kernel/types/invocation_update_response.py">InvocationUpdateResponse</a></code>
- <code title="get /invocations">client.invocations.<a href="./src/kernel/resources/invocations.py">list</a>(\*\*<a href="src/kernel/types/invocation_list_params.py">params</a>) -> <a href="./src/kernel/types/invocation_list_response.py">SyncOffsetPagination[InvocationListResponse]</a></code>
- <code title="delete /invocations/{id}/browsers">client.invocations.<a href="./src/kernel/resources/invocations.py">delete_browsers</a>(id) -> None</code>
- <code title="get /invocations/{id}/events">client.invocations.<a href="./src/kernel/resources/invocations.py">follow</a>(id, \*\*<a href="src/kernel/types/invocation_follow_params.py">params</a>) -> <a href="./src/kernel/types/invocation_follow_response.py">InvocationFollowResponse</a></code>

# Browsers

Types:

```python
from kernel.types import (
    BrowserPersistence,
    Profile,
    BrowserCreateResponse,
    BrowserRetrieveResponse,
    BrowserListResponse,
)
```

Methods:

- <code title="post /browsers">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">create</a>(\*\*<a href="src/kernel/types/browser_create_params.py">params</a>) -> <a href="./src/kernel/types/browser_create_response.py">BrowserCreateResponse</a></code>
- <code title="get /browsers/{id}">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">retrieve</a>(id) -> <a href="./src/kernel/types/browser_retrieve_response.py">BrowserRetrieveResponse</a></code>
- <code title="get /browsers">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">list</a>(\*\*<a href="src/kernel/types/browser_list_params.py">params</a>) -> <a href="./src/kernel/types/browser_list_response.py">SyncOffsetPagination[BrowserListResponse]</a></code>
- <code title="delete /browsers">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">delete</a>(\*\*<a href="src/kernel/types/browser_delete_params.py">params</a>) -> None</code>
- <code title="delete /browsers/{id}">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">delete_by_id</a>(id) -> None</code>
- <code title="post /browsers/{id}/extensions">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">load_extensions</a>(id, \*\*<a href="src/kernel/types/browser_load_extensions_params.py">params</a>) -> None</code>

## Replays

Types:

```python
from kernel.types.browsers import ReplayListResponse, ReplayStartResponse
```

Methods:

- <code title="get /browsers/{id}/replays">client.browsers.replays.<a href="./src/kernel/resources/browsers/replays.py">list</a>(id) -> <a href="./src/kernel/types/browsers/replay_list_response.py">ReplayListResponse</a></code>
- <code title="get /browsers/{id}/replays/{replay_id}">client.browsers.replays.<a href="./src/kernel/resources/browsers/replays.py">download</a>(replay_id, \*, id) -> BinaryAPIResponse</code>
- <code title="post /browsers/{id}/replays">client.browsers.replays.<a href="./src/kernel/resources/browsers/replays.py">start</a>(id, \*\*<a href="src/kernel/types/browsers/replay_start_params.py">params</a>) -> <a href="./src/kernel/types/browsers/replay_start_response.py">ReplayStartResponse</a></code>
- <code title="post /browsers/{id}/replays/{replay_id}/stop">client.browsers.replays.<a href="./src/kernel/resources/browsers/replays.py">stop</a>(replay_id, \*, id) -> None</code>

## Fs

Types:

```python
from kernel.types.browsers import FFileInfoResponse, FListFilesResponse
```

Methods:

- <code title="put /browsers/{id}/fs/create_directory">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">create_directory</a>(id, \*\*<a href="src/kernel/types/browsers/f_create_directory_params.py">params</a>) -> None</code>
- <code title="put /browsers/{id}/fs/delete_directory">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">delete_directory</a>(id, \*\*<a href="src/kernel/types/browsers/f_delete_directory_params.py">params</a>) -> None</code>
- <code title="put /browsers/{id}/fs/delete_file">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">delete_file</a>(id, \*\*<a href="src/kernel/types/browsers/f_delete_file_params.py">params</a>) -> None</code>
- <code title="get /browsers/{id}/fs/download_dir_zip">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">download_dir_zip</a>(id, \*\*<a href="src/kernel/types/browsers/f_download_dir_zip_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /browsers/{id}/fs/file_info">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">file_info</a>(id, \*\*<a href="src/kernel/types/browsers/f_file_info_params.py">params</a>) -> <a href="./src/kernel/types/browsers/f_file_info_response.py">FFileInfoResponse</a></code>
- <code title="get /browsers/{id}/fs/list_files">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">list_files</a>(id, \*\*<a href="src/kernel/types/browsers/f_list_files_params.py">params</a>) -> <a href="./src/kernel/types/browsers/f_list_files_response.py">FListFilesResponse</a></code>
- <code title="put /browsers/{id}/fs/move">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">move</a>(id, \*\*<a href="src/kernel/types/browsers/f_move_params.py">params</a>) -> None</code>
- <code title="get /browsers/{id}/fs/read_file">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">read_file</a>(id, \*\*<a href="src/kernel/types/browsers/f_read_file_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /browsers/{id}/fs/set_file_permissions">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">set_file_permissions</a>(id, \*\*<a href="src/kernel/types/browsers/f_set_file_permissions_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/fs/upload">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">upload</a>(id, \*\*<a href="src/kernel/types/browsers/f_upload_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/fs/upload_zip">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">upload_zip</a>(id, \*\*<a href="src/kernel/types/browsers/f_upload_zip_params.py">params</a>) -> None</code>
- <code title="put /browsers/{id}/fs/write_file">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">write_file</a>(id, contents, \*\*<a href="src/kernel/types/browsers/f_write_file_params.py">params</a>) -> None</code>

### Watch

Types:

```python
from kernel.types.browsers.fs import WatchEventsResponse, WatchStartResponse
```

Methods:

- <code title="get /browsers/{id}/fs/watch/{watch_id}/events">client.browsers.fs.watch.<a href="./src/kernel/resources/browsers/fs/watch.py">events</a>(watch_id, \*, id) -> <a href="./src/kernel/types/browsers/fs/watch_events_response.py">WatchEventsResponse</a></code>
- <code title="post /browsers/{id}/fs/watch">client.browsers.fs.watch.<a href="./src/kernel/resources/browsers/fs/watch.py">start</a>(id, \*\*<a href="src/kernel/types/browsers/fs/watch_start_params.py">params</a>) -> <a href="./src/kernel/types/browsers/fs/watch_start_response.py">WatchStartResponse</a></code>
- <code title="delete /browsers/{id}/fs/watch/{watch_id}">client.browsers.fs.watch.<a href="./src/kernel/resources/browsers/fs/watch.py">stop</a>(watch_id, \*, id) -> None</code>

## Process

Types:

```python
from kernel.types.browsers import (
    ProcessExecResponse,
    ProcessKillResponse,
    ProcessSpawnResponse,
    ProcessStatusResponse,
    ProcessStdinResponse,
    ProcessStdoutStreamResponse,
)
```

Methods:

- <code title="post /browsers/{id}/process/exec">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">exec</a>(id, \*\*<a href="src/kernel/types/browsers/process_exec_params.py">params</a>) -> <a href="./src/kernel/types/browsers/process_exec_response.py">ProcessExecResponse</a></code>
- <code title="post /browsers/{id}/process/{process_id}/kill">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">kill</a>(process_id, \*, id, \*\*<a href="src/kernel/types/browsers/process_kill_params.py">params</a>) -> <a href="./src/kernel/types/browsers/process_kill_response.py">ProcessKillResponse</a></code>
- <code title="post /browsers/{id}/process/spawn">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">spawn</a>(id, \*\*<a href="src/kernel/types/browsers/process_spawn_params.py">params</a>) -> <a href="./src/kernel/types/browsers/process_spawn_response.py">ProcessSpawnResponse</a></code>
- <code title="get /browsers/{id}/process/{process_id}/status">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">status</a>(process_id, \*, id) -> <a href="./src/kernel/types/browsers/process_status_response.py">ProcessStatusResponse</a></code>
- <code title="post /browsers/{id}/process/{process_id}/stdin">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">stdin</a>(process_id, \*, id, \*\*<a href="src/kernel/types/browsers/process_stdin_params.py">params</a>) -> <a href="./src/kernel/types/browsers/process_stdin_response.py">ProcessStdinResponse</a></code>
- <code title="get /browsers/{id}/process/{process_id}/stdout/stream">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">stdout_stream</a>(process_id, \*, id) -> <a href="./src/kernel/types/browsers/process_stdout_stream_response.py">ProcessStdoutStreamResponse</a></code>

## Logs

Methods:

- <code title="get /browsers/{id}/logs/stream">client.browsers.logs.<a href="./src/kernel/resources/browsers/logs.py">stream</a>(id, \*\*<a href="src/kernel/types/browsers/log_stream_params.py">params</a>) -> <a href="./src/kernel/types/shared/log_event.py">LogEvent</a></code>

## Computer

Types:

```python
from kernel.types.browsers import ComputerSetCursorVisibilityResponse
```

Methods:

- <code title="post /browsers/{id}/computer/screenshot">client.browsers.computer.<a href="./src/kernel/resources/browsers/computer.py">capture_screenshot</a>(id, \*\*<a href="src/kernel/types/browsers/computer_capture_screenshot_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /browsers/{id}/computer/click_mouse">client.browsers.computer.<a href="./src/kernel/resources/browsers/computer.py">click_mouse</a>(id, \*\*<a href="src/kernel/types/browsers/computer_click_mouse_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/computer/drag_mouse">client.browsers.computer.<a href="./src/kernel/resources/browsers/computer.py">drag_mouse</a>(id, \*\*<a href="src/kernel/types/browsers/computer_drag_mouse_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/computer/move_mouse">client.browsers.computer.<a href="./src/kernel/resources/browsers/computer.py">move_mouse</a>(id, \*\*<a href="src/kernel/types/browsers/computer_move_mouse_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/computer/press_key">client.browsers.computer.<a href="./src/kernel/resources/browsers/computer.py">press_key</a>(id, \*\*<a href="src/kernel/types/browsers/computer_press_key_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/computer/scroll">client.browsers.computer.<a href="./src/kernel/resources/browsers/computer.py">scroll</a>(id, \*\*<a href="src/kernel/types/browsers/computer_scroll_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/computer/cursor">client.browsers.computer.<a href="./src/kernel/resources/browsers/computer.py">set_cursor_visibility</a>(id, \*\*<a href="src/kernel/types/browsers/computer_set_cursor_visibility_params.py">params</a>) -> <a href="./src/kernel/types/browsers/computer_set_cursor_visibility_response.py">ComputerSetCursorVisibilityResponse</a></code>
- <code title="post /browsers/{id}/computer/type">client.browsers.computer.<a href="./src/kernel/resources/browsers/computer.py">type_text</a>(id, \*\*<a href="src/kernel/types/browsers/computer_type_text_params.py">params</a>) -> None</code>

## Playwright

Types:

```python
from kernel.types.browsers import PlaywrightExecuteResponse
```

Methods:

- <code title="post /browsers/{id}/playwright/execute">client.browsers.playwright.<a href="./src/kernel/resources/browsers/playwright.py">execute</a>(id, \*\*<a href="src/kernel/types/browsers/playwright_execute_params.py">params</a>) -> <a href="./src/kernel/types/browsers/playwright_execute_response.py">PlaywrightExecuteResponse</a></code>

# Profiles

Types:

```python
from kernel.types import ProfileListResponse
```

Methods:

- <code title="post /profiles">client.profiles.<a href="./src/kernel/resources/profiles.py">create</a>(\*\*<a href="src/kernel/types/profile_create_params.py">params</a>) -> <a href="./src/kernel/types/profile.py">Profile</a></code>
- <code title="get /profiles/{id_or_name}">client.profiles.<a href="./src/kernel/resources/profiles.py">retrieve</a>(id_or_name) -> <a href="./src/kernel/types/profile.py">Profile</a></code>
- <code title="get /profiles">client.profiles.<a href="./src/kernel/resources/profiles.py">list</a>() -> <a href="./src/kernel/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /profiles/{id_or_name}">client.profiles.<a href="./src/kernel/resources/profiles.py">delete</a>(id_or_name) -> None</code>
- <code title="get /profiles/{id_or_name}/download">client.profiles.<a href="./src/kernel/resources/profiles.py">download</a>(id_or_name) -> BinaryAPIResponse</code>

# Proxies

Types:

```python
from kernel.types import (
    ProxyCreateResponse,
    ProxyRetrieveResponse,
    ProxyListResponse,
    ProxyCheckResponse,
)
```

Methods:

- <code title="post /proxies">client.proxies.<a href="./src/kernel/resources/proxies.py">create</a>(\*\*<a href="src/kernel/types/proxy_create_params.py">params</a>) -> <a href="./src/kernel/types/proxy_create_response.py">ProxyCreateResponse</a></code>
- <code title="get /proxies/{id}">client.proxies.<a href="./src/kernel/resources/proxies.py">retrieve</a>(id) -> <a href="./src/kernel/types/proxy_retrieve_response.py">ProxyRetrieveResponse</a></code>
- <code title="get /proxies">client.proxies.<a href="./src/kernel/resources/proxies.py">list</a>() -> <a href="./src/kernel/types/proxy_list_response.py">ProxyListResponse</a></code>
- <code title="delete /proxies/{id}">client.proxies.<a href="./src/kernel/resources/proxies.py">delete</a>(id) -> None</code>
- <code title="post /proxies/{id}/check">client.proxies.<a href="./src/kernel/resources/proxies.py">check</a>(id) -> <a href="./src/kernel/types/proxy_check_response.py">ProxyCheckResponse</a></code>

# Extensions

Types:

```python
from kernel.types import ExtensionListResponse, ExtensionUploadResponse
```

Methods:

- <code title="get /extensions">client.extensions.<a href="./src/kernel/resources/extensions.py">list</a>() -> <a href="./src/kernel/types/extension_list_response.py">ExtensionListResponse</a></code>
- <code title="delete /extensions/{id_or_name}">client.extensions.<a href="./src/kernel/resources/extensions.py">delete</a>(id_or_name) -> None</code>
- <code title="get /extensions/{id_or_name}">client.extensions.<a href="./src/kernel/resources/extensions.py">download</a>(id_or_name) -> BinaryAPIResponse</code>
- <code title="get /extensions/from_chrome_store">client.extensions.<a href="./src/kernel/resources/extensions.py">download_from_chrome_store</a>(\*\*<a href="src/kernel/types/extension_download_from_chrome_store_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /extensions">client.extensions.<a href="./src/kernel/resources/extensions.py">upload</a>(\*\*<a href="src/kernel/types/extension_upload_params.py">params</a>) -> <a href="./src/kernel/types/extension_upload_response.py">ExtensionUploadResponse</a></code>

# BrowserPools

Types:

```python
from kernel.types import BrowserPool, BrowserPoolListResponse, BrowserPoolAcquireResponse
```

Methods:

- <code title="post /browser_pools">client.browser_pools.<a href="./src/kernel/resources/browser_pools.py">create</a>(\*\*<a href="src/kernel/types/browser_pool_create_params.py">params</a>) -> <a href="./src/kernel/types/browser_pool.py">BrowserPool</a></code>
- <code title="get /browser_pools/{id_or_name}">client.browser_pools.<a href="./src/kernel/resources/browser_pools.py">retrieve</a>(id_or_name) -> <a href="./src/kernel/types/browser_pool.py">BrowserPool</a></code>
- <code title="patch /browser_pools/{id_or_name}">client.browser_pools.<a href="./src/kernel/resources/browser_pools.py">update</a>(id_or_name, \*\*<a href="src/kernel/types/browser_pool_update_params.py">params</a>) -> <a href="./src/kernel/types/browser_pool.py">BrowserPool</a></code>
- <code title="get /browser_pools">client.browser_pools.<a href="./src/kernel/resources/browser_pools.py">list</a>() -> <a href="./src/kernel/types/browser_pool_list_response.py">BrowserPoolListResponse</a></code>
- <code title="delete /browser_pools/{id_or_name}">client.browser_pools.<a href="./src/kernel/resources/browser_pools.py">delete</a>(id_or_name, \*\*<a href="src/kernel/types/browser_pool_delete_params.py">params</a>) -> None</code>
- <code title="post /browser_pools/{id_or_name}/acquire">client.browser_pools.<a href="./src/kernel/resources/browser_pools.py">acquire</a>(id_or_name, \*\*<a href="src/kernel/types/browser_pool_acquire_params.py">params</a>) -> <a href="./src/kernel/types/browser_pool_acquire_response.py">BrowserPoolAcquireResponse</a></code>
- <code title="post /browser_pools/{id_or_name}/flush">client.browser_pools.<a href="./src/kernel/resources/browser_pools.py">flush</a>(id_or_name) -> None</code>
- <code title="post /browser_pools/{id_or_name}/release">client.browser_pools.<a href="./src/kernel/resources/browser_pools.py">release</a>(id_or_name, \*\*<a href="src/kernel/types/browser_pool_release_params.py">params</a>) -> None</code>

# Agents

## Auth

Types:

```python
from kernel.types.agents import (
    AgentAuthInvocationResponse,
    AgentAuthSubmitResponse,
    AuthAgent,
    AuthAgentCreateRequest,
    AuthAgentInvocationCreateRequest,
    AuthAgentInvocationCreateResponse,
    DiscoveredField,
)
```

Methods:

- <code title="post /agents/auth">client.agents.auth.<a href="./src/kernel/resources/agents/auth/auth.py">create</a>(\*\*<a href="src/kernel/types/agents/auth_create_params.py">params</a>) -> <a href="./src/kernel/types/agents/auth_agent.py">AuthAgent</a></code>
- <code title="get /agents/auth/{id}">client.agents.auth.<a href="./src/kernel/resources/agents/auth/auth.py">retrieve</a>(id) -> <a href="./src/kernel/types/agents/auth_agent.py">AuthAgent</a></code>
- <code title="get /agents/auth">client.agents.auth.<a href="./src/kernel/resources/agents/auth/auth.py">list</a>(\*\*<a href="src/kernel/types/agents/auth_list_params.py">params</a>) -> <a href="./src/kernel/types/agents/auth_agent.py">SyncOffsetPagination[AuthAgent]</a></code>
- <code title="delete /agents/auth/{id}">client.agents.auth.<a href="./src/kernel/resources/agents/auth/auth.py">delete</a>(id) -> None</code>

### Invocations

Types:

```python
from kernel.types.agents.auth import InvocationExchangeResponse
```

Methods:

- <code title="post /agents/auth/invocations">client.agents.auth.invocations.<a href="./src/kernel/resources/agents/auth/invocations.py">create</a>(\*\*<a href="src/kernel/types/agents/auth/invocation_create_params.py">params</a>) -> <a href="./src/kernel/types/agents/auth_agent_invocation_create_response.py">AuthAgentInvocationCreateResponse</a></code>
- <code title="get /agents/auth/invocations/{invocation_id}">client.agents.auth.invocations.<a href="./src/kernel/resources/agents/auth/invocations.py">retrieve</a>(invocation_id) -> <a href="./src/kernel/types/agents/agent_auth_invocation_response.py">AgentAuthInvocationResponse</a></code>
- <code title="post /agents/auth/invocations/{invocation_id}/exchange">client.agents.auth.invocations.<a href="./src/kernel/resources/agents/auth/invocations.py">exchange</a>(invocation_id, \*\*<a href="src/kernel/types/agents/auth/invocation_exchange_params.py">params</a>) -> <a href="./src/kernel/types/agents/auth/invocation_exchange_response.py">InvocationExchangeResponse</a></code>
- <code title="post /agents/auth/invocations/{invocation_id}/submit">client.agents.auth.invocations.<a href="./src/kernel/resources/agents/auth/invocations.py">submit</a>(invocation_id, \*\*<a href="src/kernel/types/agents/auth/invocation_submit_params.py">params</a>) -> <a href="./src/kernel/types/agents/agent_auth_submit_response.py">AgentAuthSubmitResponse</a></code>

# Credentials

Types:

```python
from kernel.types import (
    CreateCredentialRequest,
    Credential,
    UpdateCredentialRequest,
    CredentialTotpCodeResponse,
)
```

Methods:

- <code title="post /credentials">client.credentials.<a href="./src/kernel/resources/credentials.py">create</a>(\*\*<a href="src/kernel/types/credential_create_params.py">params</a>) -> <a href="./src/kernel/types/credential.py">Credential</a></code>
- <code title="get /credentials/{id_or_name}">client.credentials.<a href="./src/kernel/resources/credentials.py">retrieve</a>(id_or_name) -> <a href="./src/kernel/types/credential.py">Credential</a></code>
- <code title="patch /credentials/{id_or_name}">client.credentials.<a href="./src/kernel/resources/credentials.py">update</a>(id_or_name, \*\*<a href="src/kernel/types/credential_update_params.py">params</a>) -> <a href="./src/kernel/types/credential.py">Credential</a></code>
- <code title="get /credentials">client.credentials.<a href="./src/kernel/resources/credentials.py">list</a>(\*\*<a href="src/kernel/types/credential_list_params.py">params</a>) -> <a href="./src/kernel/types/credential.py">SyncOffsetPagination[Credential]</a></code>
- <code title="delete /credentials/{id_or_name}">client.credentials.<a href="./src/kernel/resources/credentials.py">delete</a>(id_or_name) -> None</code>
- <code title="get /credentials/{id_or_name}/totp-code">client.credentials.<a href="./src/kernel/resources/credentials.py">totp_code</a>(id_or_name) -> <a href="./src/kernel/types/credential_totp_code_response.py">CredentialTotpCodeResponse</a></code>
