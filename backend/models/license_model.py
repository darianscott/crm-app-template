"""
Defines the License model, representing professional
credentials and legal scope for CRM users.

Each license anchors a user's authority to operate
within a specific region or jurisdiction,
and may influence access, reporting, and compliance
flows across the system.

Includes:
- License type (e.g. broker, agent)
- Jurisdiction (e.g. state, region)
- Expiration and renewal tracking
- Relationship to user identity and role

Design intent:
- Ensure traceability of professional status
- Support multi-jurisdictional workflows and scoped access
- Enable future compliance features (e.g. alerts, audits)

This model defines the boundary between personal identity and professional legitimacy—
quietly shaping what users can do, where, and under what authority.
"""

from extensions import db, uuid, datetime, timezone, GUID

class License(db.Model):
    """
    Represents a professional license held by a CRM user.

    Fields:
    - license_type: Type of credential (e.g. broker, agent)
    - license_number: Official registration or ID number
    - issued_on: Date the license was granted
    - expires_on: Date the license becomes invalid
    - is_compliant: Boolean flag indicating current validity
    - days_remaining: Calculated field showing time until expiration
    - reminder_30_day: Boolean or timestamp for 30-day-out alert

    Relationships:
    - Linked to a single user (owner of the license)

    Design intent:
    - Track professional legitimacy and expiration risk
    - Support compliance workflows and proactive reminders
    - Enable scoped access and jurisdictional filtering

    This class defines the boundary between permission and expiration—
    a living credential that shapes what a user can do, and for how long.
    """

    __tablename__ = 'licenses'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)
    license_type = db.Column(db.String(255), nullable=False)
    license_number = db.Column(db.String(255), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    is_compliant = db.Column(db.Boolean, nullable=False, default=True)
    days_remaining = db.Column(db.Integer,nullable=False, default=365)
    reminder_days = db.Column(db.Integer, nullable=False, default=30)
    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    user = db.relationship("User", back_populates="licenses")

    def __repr__(self):
        return f"<License {self.id}>"

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
        days_remaining = (self.expiration_date.date() - datetime.utcnow().date()).days
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "license_type": self.license_type,
            "license_number": self.license_number,
            "issue_date": self.issue_date.strftime("%Y-%m-%d"),
            "expiration_date": self.expiration_date.strftime("%Y-%m-%d"),
            "days_remaining": days_remaining,
            "is_compliant": days_remaining > 0,
            "reminder_days": self.reminder_days,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }
