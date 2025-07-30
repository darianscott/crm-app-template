from extensions import db, uuid, datetime, timezone, GUID


class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)
    client_id = db.Column(GUID(), db.ForeignKey('client.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date_collected = db.Column(db.DateTime, nullable=False,
        server_default=db.func.now())
    approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Testimonial {self.id}>"


    # Relationships
    user = db.relationship("User", back_populates="testimonials", cascade="all, delete-orphan")
    client = db.relationship("Client", back_populates="testimonaial", cascade="all, delete-orphan")
