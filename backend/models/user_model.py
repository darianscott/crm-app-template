import uuid
from flask_sqlalchemy import SQLAlchemy
from utils.guid_type import GUID

db = SQLAlchemy()  # Usually initialized in __init__.py and imported into this file

# ---- Sample User Model using UUID ----
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(GUID(), primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
