from extensions import db, uuid, datetime, timezone, GUID


class Reminder(db.Model):
    __tablename__ = 'reminders'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)

    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)

    title = db.Column(db.String(40), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.String(8), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_completed =db.Column(db.Boolean, default=False)
    due_date = db.Column(db.String(8), nullable=False)


    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    # Relationship
    user = db.relationship("User", back_populates="reminders")

    def __repr__(self):
        return f"<Reminder {self.id} - {self.message}>"

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
            "id": str(self.id),
            "user_id": str(self.user_id),
            "title": self.title,
            "message": self.message,
            "date_created": self.date_created,
            "due_date": self.due_date,
            "is_completed": self.is_completed,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
