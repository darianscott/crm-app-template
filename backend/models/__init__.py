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
from .license_model import License
from .reminders_model import Reminder
from .interactions_model import Interaction
from .training_hours_model import TrainingHours
from .testimonials_model import Testimonial
from .notes_model import Notes
from .appointments_model import Appointments

__all__ = [
    "User",
    "Client",
    "License",
    "Reminder",
    "Interaction",
    "TrainingHours",
    "Testimonial",
    "Notes",
    "Appointments",
]
