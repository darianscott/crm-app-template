# extensions.py
import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column
from datetime import datetime, timezone
from backend.models.utils.guid_type import GUID

db = SQLAlchemy()

