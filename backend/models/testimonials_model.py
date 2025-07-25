from extensions import db, uuid, DateTime, Column, datetime, timezone, GUID



# ---- Sample Testimonials Model using UUID ----
class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), nullable=False, foreign_key=True)
    client_id = db.Column(GUID(), nullable=False, foreign_key=True)
    type = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Assuming a rating scale of 1-5
    date_collected = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    approved = db.Column(db.Boolean, default=False)  # Whether the testimonial has been approved for public display
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: db.datetime.now(db.timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: db.datetime.now(db.timezone.utc), onupdate=lambda: db.datetime.now(db.timezone.utc))
    
    def __repr__(self):
        return f"<Testimonial {self.id}>"
