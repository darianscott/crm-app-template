"""
Centralized model imports for the CRM.

This module exposes all core data models—user, client, license, and related entities—
so they can be imported cleanly from a single location.

Design intent:
- Eliminate repetitive import paths across the app
- Keep model access narratable and modular
- Support clean orchestration in app.py and beyond
"""

from .user_model import User
from .client_model import Client

__all__ = [
    "User",
    "Client",
]
