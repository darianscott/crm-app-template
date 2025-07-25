from extensions import db, uuid, DateTime, Column, datetime, timezone, GUID

 
 
class Reminder(db.Model):
    __tablename__ = 'reminders'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)

    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)

    message = Column(db.Text, nullable=False)
    date_created = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    date_reminded = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(db.Boolean, default=True)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)), onupdate=lambda: datetime.now(timezone.utc)
    # Relationship
    user = db.relationship("User", back_populates="reminders")

    def __repr__(self):
        return f"<Reminder {self.id} - {self.message}>"

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "message": self.message,
            "date_created": self.date_created.isoformat() if self.date_created else None,
            "date_reminded": self.date_reminded.isoformat() if self.date_reminded else None,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

