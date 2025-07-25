from extensions import db, uuid, DateTime, Column, datetime, timezone, GUID



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
    
    def to_dict(self):
        return {
            "client_id": str(self.client_id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "street_address": self.street_address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "notes": self.notes,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
    }

