import uuid
from flask_sqlalchemy import SQLAlchemy
from utils.guid_type import GUID
from sqlalchemy.sql import func
from sqlalchemy import DateTime, Column
from datetime import datetime, timezone

db = SQLAlchemy()  # Usually initialized in __init__.py and imported into this file
 
# ---- Sample Reminder Model using UUID ----
class Reminder(db.Model):
    __tablename__ = 'reminders'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), nullable=False, foreign_key=True)
    message = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    date_reminded = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)  # Whether the reminder is still active
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Reminder {self.id} - {self.message}>"
