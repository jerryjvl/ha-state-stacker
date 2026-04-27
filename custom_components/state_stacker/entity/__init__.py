"""
Entity package for state_stacker.

Architecture:
    All platform entities inherit from (PlatformEntity, StateStackerEntity).
    MRO order matters — platform-specific class first, then the integration base.
    Entities read data from coordinator.data and NEVER call the API client directly.
    Unique IDs follow the pattern: {entry_id}_{description.key}

See entity/base.py for the StateStackerEntity base class.
"""

from .base import StateStackerEntity

__all__ = ["StateStackerEntity"]
