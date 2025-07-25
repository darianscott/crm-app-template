import uuid
from sqlalchemy.dialects.postgresql import UUID  # Only used if PostgreSQL is in use
from sqlalchemy.types import TypeDecorator, CHAR

class GUID(TypeDecorator):
    """Platform-independent GUID type for SQLite and PostgreSQL."""
    impl = CHAR
    cache_ok = True  # Recommended for SQLAlchemy 1.4+ to avoid warnings

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID(as_uuid=True))
        else:
            return dialect.type_descriptor(CHAR(36))

    def process_bind_param(self, value, dialect):
        if value is None:
            return str(uuid.uuid4())
        if not isinstance(value, str):
            return str(value)
        return value

    def process_result_value(self, value, dialect):
        # If you want UUID objects in Python, uncomment:
        # return uuid.UUID(value) if value else None
        return value if value else None
