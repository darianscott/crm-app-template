from extensions import db, uuid, datetime, timezone, GUID

class Appointments(db.Model):
    """
    Represents a scheduled meeting or event in the system.

    This model tracks:
    - Title: What the appointment is about
    - With whom: The person or party involved
    - Location: Where it's happening
    - Date and time: When it's scheduled
    - Notes: Any additional context or reminders

    Designed to be simple, readable, and narratable.
    Used in dashboards, reminders, and reporting flows.
    """
    __tablename__ = 'appointments'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)

    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)
    client_id = db.Column(GUID(), db.ForeignKey('client.id'), nullable=False)


    title = db.Column(db.String(40), nullable=False)
    appointment_with = db.Column(db.String(40), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(8), nullable=False)
    time = db.Column(db.String(10), nullable=False)
    place = db.Column(db.String(20), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_completed =db.Column(db.Boolean, default=False)


    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    # Relationship
    user = db.relationship("User", back_populates="appointments")
    client = db.relationship("Client", back_populates="appointments")


    def __repr__(self):
        return f"<Appointments {self.id} - {self.message}>"

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
            "title": self.title,
            "appointment_with": self.appointment_with,
            "message": self.message,
            "date": self.date_created,
            "is_completed": self.is_completed,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
