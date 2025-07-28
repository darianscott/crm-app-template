# extensions.py
import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column, func
from datetime import datetime, timezone
from utils.guid_type import GUID

db = SQLAlchemy()

