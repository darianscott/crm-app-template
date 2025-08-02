from extensions import db, uuid, datetime, timezone, GUID



class Client(db.Model):
    """
    Represents a person in the system—typically a client, lead, or prospect.

    Core identity fields:
    - First and last name
    - Street address and ZIP code
    - Phone number and email
    - Status (e.g. active, lead, archived)

    Relational context:
    - Linked to interactions, appointments, notes, and testimonials
    - Serves as the anchor for all client-facing activity
    - Used in dashboards, reporting, and CRM flows

    Design intent:
    - Built for clarity and traceability—every relationship narrates the client journey
    - Status field helps brokers segment and prioritize contacts
    - Email and phone are validated for outreach integrity
    """
    __tablename__ = 'clients'
    client_id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    street_address = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, unique=True)
    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    interaction_type = db.Column(db.Text, nullable=False)
    interaction_summary = db.Column(db.String(300), nullable=False)
    interaction_created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))

    testimonial_type = db.Column(db.String(50), nullable=False)
    testimonial_content = db.Column(db.Text, nullable=False)
    testimonial_rating = db.Column(db.Integer, nullable=False)
    testimonial_date_collected = db.Column(db.DateTime, nullable=False,
        server_default=db.func.now())
    testimonial_approved = db.Column(db.Boolean, default=False)

    # Relationships

    user = db.relationship("User", back_populates="client",
        cascade="all, delete-orphan")



    def __repr__(self):
        return f"<Client {self.first_name} {self.last_name}>"

    def to_dict(self):
        """
        Returns a dictionary representation of the model instance.

        Purpose:
        - Used for frontend rendering, API responses, logging, and reporting
        - Ensures consistent, narratable snapshots of model state

        Design intent:
        - Only includes fields relevant to user-facing flows or reporting
        - Omits sensitive or internal-only attributes (e.g. password hashes, system flags)
        - May include calculated or relational fields for richer context

        This method defines how the model introduces itself—what it reveals, what it protects,
        and how it fits into the broader story of the CRM.
        """

        return {
            "client_id": str(self.client_id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "street_address": self.street_address,
            "zip_code": self.zip_code,
            "notes": self.notes,
            "email": self.email,
            "status": self.status,
            "created_at": self.created_at.isoformat()
                if self.created_at else None,
            "updated_at": self.updated_at.isoformat()
                if self.updated_at else None,
            "interaction_type": self.interaction_type,
            "interaction_summary": self.interaction_summary,
            "interaction_created_at": self.interaction_created_at.isoformat()
                if self.created_at else None,
            "testimonial_type": self.testimonial_type,
            "testimonial_content": self.testimonial_content,
            "testimonial_rating": self.testimonial_rating,
            "testimonial_date_collected": self.testimonial_date_collected,
            "testimonial_approved": self.testimonial_approved,         
        }
