import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from utils.guid_type import GUID



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
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    def __repr__(self):
       
        return f"<TrainingHours {self.id} - {self.authority} - {self.training_type}>"
