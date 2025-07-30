from extensions import db, uuid, datetime, timezone, GUID



# ---- Sample Client Model using UUID ----
class Notes(db.Model):
    '''
    -This is the table that will hold the notes for the clients
    - Reason to not clutter up the client table
    '''

    __tablename__ = 'note'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), db.ForeignKey('users.id'),
        nullable=False)
    client_id = db.Column(GUID(), db.ForeignKey('client.id'),
        nullable=False)
    note_content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    clients = db.relationship("Clients", back_populates="notes",
        cascade="all, delete-orphan")
    user = db.relationship("User", back_populates="notes",
        cascade="all, delete-orphan")



    def __repr__(self):
        return f"<Notes {self.note_content}>"

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
            "note_content": self.note_content,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
    }
