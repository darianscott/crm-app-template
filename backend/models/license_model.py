import uuid
from flask_sqlalchemy import SQLAlchemy
from utils.guid_type import GUID
from sqlalchemy.sql import func


db = SQLAlchemy()  # Usually initialized in __init__.py and imported into this file

# ---- Sample License Model using UUID ----
class License(db.Model):
    __tablename__ = 'licenses'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), nullable=False, foreign_key=True)
    license_type = db.Column(db.Text(255), unique=True, nullable=False)
    license_number = db.Column(db.Text, nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Text(50), nullable=False, default='active')  # e.g., active, expired, revoked
    reminder_days = db.Column(db.Integer, nullable=False, default=30)  # Days before expiration to send reminder    
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<License {self.id}>"
