from extensions import db, uuid, DateTime, Column, datetime, timezone, GUID


class TrainingHours(db.Model):
    __tablename__ = 'training_hours'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)
    authority = db.Column(db.String(100), nullable=False)
    training_type = db.Column(db.String(100), nullable=False)
    hours = db.Column(db.Float, nullable=False)
    date_completed = db.Column(db.DateTime, nullable=False)
    certification_url = db.Column(db.String(255), nullable=True)

    required_hours = db.Column(db.Float, nullable=False)
    date_due = db.Column(db.DateTime, nullable=False)

    is_compliant = db.Column(db.Boolean, nullable=False, default=True)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationship to User
    user = db.relationship("User", back_populates="training_hours")

    def __repr__(self):
        return f"<TrainingHours {self.id} - {self.authority} - {self.training_type}>"

    def to_dict(self):
        days_remaining = (self.date_due.date() - datetime.utcnow().date()).days if self.date_due else None
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "authority": self.authority,
            "training_type": self.training_type,
            "completed_hours": self.hours,
            "required_hours": self.required_hours,
            "date_completed": self.date_completed.strftime("%Y-%m-%d"),
            "date_due": self.date_due.strftime("%Y-%m-%d") if self.date_due else None,
            "days_remaining": days_remaining,
            "is_compliant": days_remaining is not None and days_remaining >= 0,
            "certification_url": self.certification_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
