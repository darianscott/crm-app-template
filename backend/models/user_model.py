from extensions import db, uuid, DateTime, Column, datetime, timezone, GUID


class User(db.Model):
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
    testimonial_rating = db.Column(db.Float, default=0.0, comment="Rating range is 1 to 5")

    new_clients = db.Column(db.Integer, default=0)
    active_clients = db.Column(db.Integer, default=0)
    archived_clients = db.Column(db.Integer, default=0)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    licenses = db.relationship("License", back_populates="user", cascade="all, delete-orphan")
    reminders = db.relationship("Reminder", back_populates="user", cascade="all, delete-orphan")
    interactions = db.relationship("Interaction", back_populates="user", cascade="all, delete-orphan")
    training_hours = db.relationship("TrainingHours", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

    def to_dict(self):
        return {
            "id": str(self.id),
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

