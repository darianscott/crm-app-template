import uuid
from flask_sqlalchemy import SQLAlchemy
from utils.guid_type import GUID
from sqlalchemy.sql import func

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
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


    def __repr__(self):
        return f"<Reminder {self.id} - {self.message}>"
