import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from utils.guid_type import GUID
from sqlalchemy import DateTime, Column
from datetime import datetime, timezone



db = SQLAlchemy()  # Usually initialized in __init__.py and imported into this file

# ---- Sample Training Hours Model using UUID ----
class TrainingHours(db.Model):
    __tablename__ = 'training_hours'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), nullable=False, foreign_key=True)
    authority = db.Column(db.String(100), nullable=False)  # Authority providing the training
    training_type = db.Column(db.String(100), nullable=False)  # Type of training (e.g., online, in-person)
    hours = db.Column(db.Float, nullable=False)  # Number of training hours
    date_completed = db.Column(db.DateTime, nullable=False)  # Date when the training was completed
    certification_url = db.Column(db.String(255), nullable=True)  # URL to the certification or proof of training))
    required_hours = db.Column(db.Float, nullable=False)
    date_due = db.Column(db.strftime("%m-%d-%Y"))
    days_remaining = db.Column(db.number, (db.expiration_date - (db.Datetime.utcnow().date()).days))
    is_compliant = db.Column(db.Text(50), nullable=False, default='active')
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):   
        return f"<TrainingHours {self.id} - {self.authority} - {self.training_type}>"
