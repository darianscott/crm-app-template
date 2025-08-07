"""
Extensions and external integrations used across the CRM.

This module initializes and configures third-party tools and internal helpers
that extend the system's capabilities without cluttering core logic.

Includes:
- Logging (e.g. Loguru setup with contextual traceability)
- Scheduling (e.g. nightly tasks, reminders)
- Mailers (e.g. invite dispatch, testimonial requests)
- Custom validators and formatters
- Any other reusable services that operate outside the main app flow

Design intent:
- Keep core modules clean and narratable
- Centralize setup for tools that operate behind the scenes
- Ensure traceability, modularity, and graceful failure handling

These extensions support the system’s rhythm—quietly powering the flows that users rely on.
"""
# extensions.py
import uuid
from datetime import datetime, timezone
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from utils.guid_type import GUID
from models import User

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'ath.login'



@login_manager.user_loader
def load_user(user_id):
    '''
    This function loads a user from the database by their user ID.
    '''
    return User.query.get(user_id)
