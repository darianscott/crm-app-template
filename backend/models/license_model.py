import uuid
from flask_sqlalchemy import SQLAlchemy
from utils.guid_type import GUID
from sqlalchemy.sql import func


db = SQLAlchemy()  # Usually initialized in __init__.py and imported into this file

class License(db.Model):
    __tablename__ = 'licenses'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)
    license_type = db.Column(db.String(255), nullable=False)
    license_number = db.Column(db.String(255), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    is_compliant = db.Column(db.String(50), nullable=False, default='active')  # could also default to calculated in service
    reminder_days = db.Column(db.Integer, nullable=False, default=30)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<License {self.id}>"

    def to_dict(self):
        days_remaining = (self.expiration_date.date() - datetime.utcnow().date()).days
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "license_type": self.license_type,
            "license_number": self.license_number,
            "issue_date": self.issue_date.strftime("%Y-%m-%d"),
            "expiration_date": self.expiration_date.strftime("%Y-%m-%d"),
            "days_remaining": days_remaining,
            "is_compliant": days_remaining > 0,
            "reminder_days": self.reminder_days,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

