'''
This function is for security. All rows in all models will have a
uuid created for the id of that record. In this function
the class GUID is created for SQLITE3 to be able to store 
the uuid.
'''

import uuid
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID

class GUID(TypeDecorator):
    """
    Platform-independent GUID type.

    - PostgreSQL: uses native UUID type
    - Other DBs (e.g., SQLite): stores as CHAR(36)
    - Always returns uuid.UUID in Python
    """
    impl = CHAR
    cache_ok = True  # Avoid warnings in SQLAlchemy 1.4+

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID(as_uuid=True))
        return dialect.type_descriptor(CHAR(36))

    def process_bind_param(self, value, dialect):
        if value is None:
            return (uuid.uuid4()) if dialect.name != 'postgresql' else uuid.uuid4()
        if isinstance(value, uuid.UUID):
            return (value) if dialect.name != 'postgresql' else value
        return (uuid.UUID(value)) if dialect.name != 'postgresql' else uuid.UUID(value)

    def process_result_value(self, value, dialect):
        return uuid.UUID((value)) if value else None

    @property
    def python_type(self):
        return uuid.UUID

    def process_literal_param(self, value, dialect):
        return f"'{value}'" if value else "NULL"
