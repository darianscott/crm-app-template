from utils.guid_type import GUID
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import uuid
from sqlalchemy import DateTime, Column
from datetime import datetime, timezone

db = SQLAlchemy()  # Usually initialized in __init__.py and imported into this file

# ---- Sample Client Model using UUID ----
class Client(db.Model):
    __tablename__ = 'clients'
    client_id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    street_address = db.Column(db.Text, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=True) 
    email = db.Column(db.Text, unique=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Client {self.first_name} {self.last_name}>"
