"""
Model registry for dynamic reporting and user-scoped access.

Each entry defines:
- The model class
- Fields available for display or export
- Filters for querying
- Joins for relational context
- User scope for data ownership
- Labels and descriptions for UI or documentation

Used by backend reporting engines and dashboard builders
to interpret model structure narratively.
"""

from models import User, Client

MODEL_REGISTRY = {
    "user": {
        "model": User,
        "fields": [
            "first_name", "last_name", "user_name",
            "invites_sent", "archived_invites", "outstanding_invites",
            "new_clients", "active_clients", "testimonials_recieved",
            "testimonial_rating", "archived_clients",
            "email", "role", "created_at", "training_completed_hours",  
            "training_type", "required_hours", "training_date_due",
            "training_is_compliant", "training_certification_url",
            "training_date_completed", "training_authority",
            "license_days_remaining", "todo_title", "todo_due_date",
            "todo_is_completed", "todo_date_created",
            "todo_is_active", "todo_message", "training_days_remaining",
            "license_is_compliant", "license_expiration_date",
            "liense_number", "license_typ"
        ],
        "filters": [
            "role", "created_at", "user_name",
            "first_name","training_completed_hours", "last_name",
            "training_days_remaining", "license_expiration_date",
            "license_is_compliant", "license_days_remaining",
            "todo_is_completed", "todo_is_active", "training_date_due", "training_is_compliant" 
        ],
        "joins": ["clients" ],
        "user_scope": "user_id",  # user owns themselves
        "label": "User",
        "description": "Represents the system user and the"
            " using the system."
            "Tracks training hours vs required training,"
            "hours for compliance and overall growth"
            "Tracks compliance, expiration, and remaining"
            "days till expiration for user licenses"
            "User-created reminders for follow-up or tasks"
    },
    "client": {
        "model": Client,
        "fields": ["first_name", "last_name", "phone_number",
                   "street_address", "zip_code", "notes", "created_at",
                   "email", "status", "testimonial_content",
                   "testimonial_type", "date_collected",
                   "testimonial_approved", "testimonial_rating",
                   "interaction_type", "interaction_created_at",
                   "interaction_summary"
        ],
        "filters": ["status", "created_at", "testimonial_type",
                    "testimonial_rating", "interaction_created_at",
                    "interaction_type"
        ],
        "joins": ["users"],
        "user_scope": "user_id",
        "label": "Client",
        "description": "Represents a person or organization"
            "using the system.Client feedback or endorsements. Can be"
            "in the form of written, voice, or video."
            "Logs of user-client interactions"
    },
}
