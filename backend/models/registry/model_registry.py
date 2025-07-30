"""
Model registry for dynamic reporting and user-scoped access.

Each entry defines:
- The model class
- Fields available for display or export
- Filters for querying
- Joins for relational context
- User scope for data ownership
- Labels and descriptions for UI or documentation

Used by backend reporting engines and dashboard builders to interpret model structure narratively.
"""

from models import User, Client, License, Reminder, Interaction, TrainingHours, Testimonial, Notes, Appointments

MODEL_REGISTRY = {
    "user": {
        "model": User,
        "fields": ["first_name", "last_name", "user_name",
                   "invites_sent", "archived_invites", "outstanding_invites",
                   "new_clients", "active_clients", "testimonials_recieved",
                   "testimonial_rating", "archived_clients",
                   "email", "role", "created_at"
        ],
        "filters": ["role", "created_at", "user_name",
                    "first_name", "last_name"
        ],
        "joins": ["clients", "licenses", "training_hours", "interactions", "reminders", "testimonials", "notes", "appointments"],
        "user_scope": "user_id",  # user owns themselves
        "label": "User",
        "description": "Represents the system user and the metrics related to them"
    },
    "client": {
        "model": Client,
        "fields": ["first_name", "last_name", "phone_number",
                   "street_address", "zip_code", "notes", "created_at",
                   "email", "status"
        ],
        "filters": ["status", "created_at"],
        "joins": ["users", "testimonials", "interactions", "notes", ],
        "user_scope": "user_id",
        "label": "Client",
        "description": "Represents a person or organization using the system"
    },
    "license": {
        "model": License,
        "fields": ["license_type", "license_number", "expiration_date",
                   "is_compliant", "days_remaining"
        ],
        "filters": ["expiration_date", "is_compliant", "days_remaining"],
        "joins": ["users"],
        "user_scope": "user_id",
        "label": "License",
        "description": (
            "Tracks compliance, expiration, and remaining"
            "days till expiration for user licenses"
        ),
    },
    "reminder": {
        "model": Reminder,
        "fields": ["title", "due_date", "is_completed", "date_created",
                   "is_active", "message"
        ],
        "filters": ["due_date", "is_completed", "is_active"],
        "joins": ["user_id"],
        "user_scope": "user_id",
        "label": "Reminder",
        "description": "User-created reminders for follow-up or tasks"
    },
    "interaction": {
        "model": Interaction,
        "fields": ["type", "created_at", "summary"],
        "filters": ["type", "created_at"],
        "joins": ["users", "clients"],
        "user_scope": "user_id",
        "label": "Interaction",
        "description": "Logs of user-client interactions"
    },
    "training_hours": {
        "model": TrainingHours,
        "fields": ["completed_hours", "date_completed", "authority",
                   "training_type", "required_hours", "date_due",
                   "is_compliant", "updated_at"
        ],
        "filters": ["date", "is_compliant", "updated_at", "completed_hours"],
        "joins": ["users"],
        "user_scope": "user_id",
        "label": "Training Hours",
        "description": (
            "Tracks training hours vs required training,"
            "hours for compliance and overall growth"
        ),
    },
    "testimonial": {
        "model": Testimonial,
        "fields": ["content", "type", "date_collected", "approved", "rating" ],
        "filters": ["date_collected", "type"],
        "joins": ["users", "clients"],
        "user_scope": "user_id",
        "label": "Testimonial",
        "description": (
            "Client feedback or endorsements. Can be"
            "in the form of written, voice, or video."
        ),
    },
    "notes": {
        "model": Notes,
        "fields": ["created_at", "client_name", "comments"],
        "filters": ["created_at", "client_name"],
        "joins": ["users", "client"],
        "user_scope": "user_id",
        "label": "Notes",
        "description": (
            "Instead of using other db rows to include notes I"
            "seperated them to their own tables"
        ),
    },
    "appointments": {
        "model": Appointments,
        "fields": ["title", "date", "is_completed", "appointment_with"
                   "is_active", "message"
        ],
        "filters": ["date", "is_completed", "is_active"],
        "joins": ["user_id"],
        "user_scope": "user_id",
        "label": "Appointments",
        "description": "User appointments with clients, or anyone they need to meet with"
    }
}
