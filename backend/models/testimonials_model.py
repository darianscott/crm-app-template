import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from utils.guid_type import GUID

db = SQLAlchemy()  # Usually initialized in __init__.py and imported into this file

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
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Testimonial {self.id}>"
