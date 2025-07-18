import uuid
from sqlalchemy.dialects.postgresql import UUID  # used only if deploying to Postgres
from sqlalchemy.types import TypeDecorator, CHAR

# ---- GUID TypeDecorator Definition ----
class GUID(TypeDecorator):
    """Platform-independent GUID type for SQLite and PostgreSQL."""
    impl = CHAR

    def load_dialect_impl(self, dialect):
        """
        Loads the appropriate SQLAlchemy type implementation for the given database dialect.

        If the dialect is PostgreSQL, returns a UUID type with `as_uuid=True`.
        For all other dialects, returns a CHAR(36) type.

        Args:
            dialect: The SQLAlchemy dialect in use.

        Returns:
            A SQLAlchemy type descriptor suitable for the specified dialect.
        """
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID(as_uuid=True))
        else:
            return dialect.type_descriptor(CHAR(36))

    def process_bind_param(self, value, dialect):
        """
        Processes the value before it is bound to a database parameter.

        If the value is None, generates and returns a new UUID string.
        If the value is not a string, converts it to a string.
        Otherwise, returns the value as is.

        Args:
            value: The value to be processed and bound to the parameter.
            dialect: The database dialect in use (not used in this implementation).

        Returns:
            str: The processed value as a string, or a new UUID string if value is None.
        """
        if value is None:
            return str(uuid.uuid4())
        if not isinstance(value, str):
            return str(value)
        return value

    def process_result_value(self, value, dialect):
        return value if value else None