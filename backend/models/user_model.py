from extensions import db, uuid, datetime, timezone, GUID


class User(db.Model):
    """
    Represents a system user—typically a broker or agent who owns and operates the CRM.

    Identity and access:
    - First and last name
    - Username and password hash
    - Role (e.g. admin, agent)
    - Email for communication and authentication

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

    invites_sent = db.Column(db.Integer, default=0)
    archived_invites = db.Column(db.Integer, default=0)
    outstanding_invites = db.Column(db.Integer, default=0)
    testimonials_received = db.Column(db.Integer, default=0)
    testimonial_rating = db.Column(db.Float, default=0.0,
        comment="Rating range is 1 to 5")

    new_clients = db.Column(db.Integer, default=0)
    active_clients = db.Column(db.Integer, default=0)
    archived_clients = db.Column(db.Integer, default=0)

    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    licenses = db.relationship("License",
        back_populates="user", cascade="all, delete-orphan")
    reminders = db.relationship("Reminder",
        back_populates="user", cascade="all, delete-orphan")
    interactions = db.relationship("Interaction",
        back_populates="user", cascade="all, delete-orphan")
    training_hours = db.relationship("TrainingHours",
        back_populates="user", cascade="all, delete-orphan")
    clients = db.relationship("Client", back_populates="user",
        cascade="all, delete-orphan")
    appointments = db.relationship("Appointment",
        back_populates="user", cascade="all, delete-orphan")
    notes = db.relationship("Notes", back_populates="user",
        cascade="all, delete-orphan")
    testimonials = db.relationship("Testimonial",
        back_populates="user", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

    def to_dict(self):
        """
        Returns a dictionary representation of the model instance.

        Purpose:
        - Used for frontend rendering, API responses, logging, and reporting
        - Ensures consistent, narratable snapshots of model state

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
            "invites_sent": self.invites_sent,
            "archived_invites": self.archived_invites,
            "outstanding_invites": self.outstanding_invites,
            "testimonials_received": self.testimonials_received,
            "testimonial_rating": self.testimonial_rating,
            "new_clients": self.new_clients,
            "active_clients": self.active_clients,
            "archived_clients": self.archived_clients,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
