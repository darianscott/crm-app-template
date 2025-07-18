import uuid
from flask_sqlalchemy import SQLAlchemy
from utils.guid_type import GUID
from sqlalchemy.sql import func

db = SQLAlchemy()  # Usually initialized in __init__.py and imported into this file


# ---- Sample Interaction Model using UUID ----
class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    client_id = db.Column(GUID(), unique=True, nullable=False, default=uuid.uuid4, foreign_key=True)
    user_id = db.Column(GUID(), nullable=False, foreign_key=True)
    type = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text(300), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Interaction {self.id}>"
