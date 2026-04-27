"""
API package for state_stacker.

Architecture:
    Three-layer data flow: Entities → Coordinator → API Client.
    Only the coordinator should call the API client. Entities must never
    import or call the API client directly.

Exception hierarchy:
    StateStackerApiClientError (base)
    ├── StateStackerApiClientCommunicationError (network/timeout)
    └── StateStackerApiClientAuthenticationError (401/403)

Coordinator exception mapping:
    ApiClientAuthenticationError → ConfigEntryAuthFailed (triggers reauth)
    ApiClientCommunicationError → UpdateFailed (auto-retry)
    ApiClientError             → UpdateFailed (auto-retry)
"""

from .client import (
    StateStackerApiClient,
    StateStackerApiClientAuthenticationError,
    StateStackerApiClientCommunicationError,
    StateStackerApiClientError,
)

__all__ = [
    "StateStackerApiClient",
    "StateStackerApiClientAuthenticationError",
    "StateStackerApiClientCommunicationError",
    "StateStackerApiClientError",
]
