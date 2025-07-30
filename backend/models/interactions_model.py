"""
Defines the Interaction model, which logs meaningful contact between users and clients.

This module supports:
- Tracking communication history
- Enabling follow-up workflows
- Enriching client profiles with narrative context

Interactions are relational anchors—each one adds depth to the client journey,
and helps users maintain clarity, continuity, and trust.
"""

from extensions import db, uuid, datetime, timezone, GUID


class Interaction(db.Model):
    """
    Represents a recorded moment of contact between a CRM user and a client.

    Fields:
    - interaction_type: Nature of the contact (e.g. call, email, meeting)
    - summary: Brief description of what occurred or was discussed

    Relationships:
    - Linked to a single user (who initiated or logged the interaction)
    - Linked to a single client (the recipient or subject of the interaction)

    Design intent:
    - Capture the evolving relationship between user and client
    - Provide context for follow-ups, reporting, and testimonial relevance
    - Serve as a chronological breadcrumb in the client journey

    Each interaction is a snapshot of connection—small, but essential to the larger story.
    """

    __tablename__ = 'interactions'
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)

    client_id = db.Column(GUID(), db.ForeignKey('clients.client_id'),
        nullable=False)
    user_id = db.Column(GUID(), db.ForeignKey('users.id'), nullable=False)

    type = db.Column(db.Text, nullable=False)
    summary = db.Column(db.String(300), nullable=False)

    created_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    client = db.relationship("Client", back_populates="interactions")
    user = db.relationship("User", back_populates="interactions")

    def __repr__(self):
        return f"<Interaction {self.id}>"

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
            "id": str(self.id),
            "client_id": str(self.client_id),
            "user_id": str(self.user_id),
            "type": self.type,
            "summary": self.summary,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
