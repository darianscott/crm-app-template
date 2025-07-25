from extensions import db, uuid, DateTime, Column, datetime, timezone, GUID


class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)

    client_id = db.Column(GUID(), db.ForeignKey('clients.client_id'), nullable=False)
    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)

    type = db.Column(db.Text, nullable=False)
    summary = db.Column(db.String(300), nullable=False)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    client = db.relationship("Client", back_populates="interactions")
    user = db.relationship("User", back_populates="interactions")

    def __repr__(self):
        return f"<Interaction {self.id}>"

    def to_dict(self):
        return {
            "id": str(self.id),
            "client_id": str(self.client_id),
            "user_id": str(self.user_id),
            "type": self.type,
            "summary": self.summary,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

