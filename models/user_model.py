'''
The model for the User table. It holds everything that is
directly attatched to the user. It holds license, todo list
required trainging hours, completed training hours. user name
first name, last name, id(guid), role,   email, phone number. It is used 
across all models to tie everything together
'''


from flask_login import UserMixin
from extensions import db, uuid, datetime, timezone, GUID


class User(db.Model, UserMixin):
    """
    Represents a system user—typically a broker or agent who owns and operates the CRM.

    Identity and access:
    - First and last name
    - Username and password hash
    - Role (e.g. admin, agent)
    - Email for communication and authentication
    
    Includes:
    - License type (e.g. broker, agent)
    - Jurisdiction (e.g. state, region)
    - Expiration and renewal tracking
    - Relationship to user identity and role

    Design intent:
    - Ensure traceability of professional status
    - Support multi-jurisdictional workflows and scoped access
    - Enable future compliance features (e.g. alerts, audits)

    Relational scope:
    - Central node in the CRM—every other table relates to the user
    - Tracks appointments, interactions, notes, testimonials, and client records
    - Owns all data flows and reporting metrics

    Calculated fields (updated nightly):
    - Total invites sent, outstanding, and arrived
    - Testimonials received and average rating
    - Client counts: new, active, arrived

    Design intent:
    - Built for clarity, security, and traceability
    - Enables scoped access, personalized dashboards, and user-driven reporting
    - Serves as the anchor for multi-tenant architecture and data ownership

    This class defines the perspective from which all CRM activity is viewed and measured.
    """
    __tablename__ = 'users'

    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    todo_title = db.Column(db.String(40), nullable=False)
    todo_message = db.Column(db.Text, nullable=False)
    todo_date_created = db.Column(db.String(8), nullable=False)
    todo_is_active = db.Column(db.Boolean, default=True)
    todo_is_completed =db.Column(db.Boolean, default=False)
    todo_due_date = db.Column(db.String(8), nullable=False)

    invites_sent = db.Column(db.Integer, default=0)
    archived_invites = db.Column(db.Integer, default=0)
    outstanding_invites = db.Column(db.Integer, default=0)
    testimonials_received = db.Column(db.Integer, default=0)
    testimonial_rating = db.Column(db.Float, default=0.0,
        comment="Rating range is 1 to 5")

    new_clients = db.Column(db.Integer, default=0)
    active_clients = db.Column(db.Integer, default=0)
    archived_clients = db.Column(db.Integer, default=0)

    license_type = db.Column(db.String(255), nullable=False)
    license_number = db.Column(db.String(255), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    license_is_compliant = db.Column(db.Boolean, nullable=False, default=True)
    license_days_remaining = db.Column(db.Integer,nullable=False, default=365)
    reminder_days = db.Column(db.Integer, nullable=False, default=30)

    required_hours = db.Column(db.Float, nullable=False)
    training_date_due = db.Column(db.DateTime, nullable=False)
    training_is_compliant = db.Column(db.Boolean, nullable=False, default=True)
    training_authority = db.Column(db.String(100), nullable=False)
    training_type = db.Column(db.String(100), nullable=False)
    training_completed_hours = db.Column(db.Float, nullable=False)
    training_date_completed = db.Column(db.DateTime, nullable=False)
    training_certification_url = db.Column(db.String(255), nullable=True)
    training_days_remaining = db.Column(db.Integer,nullable=False, default=365)


    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    clients = db.relationship("Client", back_populates="user",
        cascade="all, delete-orphan")




    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

    def to_dict(self):
        """
        Returns a dictionary representation of the model instance.

        Purpose:
        - Used for frontend rendering, API responses, logging, and reporting
        - Ensures consistent, narratable snapshots of model state
        
        Represents a professional license held by a CRM user.

        Fields:
        - license_type: Type of credential (e.g. broker, agent)
        - license_number: Official registration or ID number
        - issued_on: Date the license was granted
        - expires_on: Date the license becomes invalid
        - is_compliant: Boolean flag indicating current validity
        - days_remaining: Calculated field showing time until expiration
        - reminder_30_day: Boolean or timestamp for 30-day-out alert

        Design intent:
        - Only includes fields relevant to user-facing flows or reporting
        - Omits sensitive or internal-only attributes (e.g. password hashes, system flags)
        - May include calculated or relational fields for richer context

        This method defines how the model introduces itself—what it reveals, what it protects,
        and how it fits into the broader story of the CRM.
        """

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            "email": self.email,
            "role": self.role,
            "is_active": self.is_active,
            "todo_title": self.todo_title,
            "todo_message": self.todo_message,
            "todo_date_created": self.todo_date_created,
            "todo_is_active": self.todo_is_active,
            "todo_is_completed": self.todo_is_completed,
            "todo_due_date": self.todo_due_date,
            "invites_sent": self.invites_sent,
            "archived_invites": self.archived_invites,
            "outstanding_invites": self.outstanding_invites,
            "testimonials_received": self.testimonials_received,
            "testimonial_rating": self.testimonial_rating,
            "new_clients": self.new_clients,
            "active_clients": self.active_clients,
            "archived_clients": self.archived_clients,
            "training_authority": self.training_authority,
            "training_type": self.training_type,
            "training_completed_hours": self.training_completed_hours,
            "required_hours": self.required_hours,
            "training_date_completed": self.training_date_completed.strftime
                ("%Y-%m-%d"),
            "training_date_due": self.training_date_due.strftime("%Y-%m-%d")
                if self.date_due else None,
            "training_is_compliant": self.training_days_remaining >= 0,
            "training_certification_url": self.training_certification_url,
            "license_type": self.license_type,
            "license_number": self.license_number,
            "issue_date": self.issue_date.strftime("%Y-%m-%d"),
            "expiration_date": self.expiration_date.strftime("%Y-%m-%d"),
            "license_days_remaining": self.license_days_remaining,
            "license_is_compliant": self.license_days_remaining > 0,
            "reminder_days": self.reminder_days,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
