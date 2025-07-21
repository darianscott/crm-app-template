from models.client_model import Client
from models.user_model import User
from models.interactions
from app import db
from datetime import datetime


def get_user_activity_table():
    results = db.session.query(
        
        User.name.label("user_name")
    ).join(User, User.id == License.user_id).all()

    table_data = []
    for row in results:
        days_remaining = (row.expiration_date.date() - datetime.now().date()).days
        is_compliant = days_remaining > 0
        table_data.append({
            "userName": row.user_name,
            "memberSince": row.member_since,
            "lastLogin": row.last_login,
            "avgeragePerMnth": row.average_per_month,
            "clientOnboardedLastMonth": row.clients_onboarded_last_month,
            "numOfActiveClients": row.num_of_active_clients,
            "numOfClientsArchived": row.num_of_clients_archived,
            "clientInteractionsLogged": row.client_interactions_logged,
            "sentInvites": row.sent_invites,
            "testimonialsRecieved": row.testimonials_recieved,
            "avgTestimonialRating": row.avg_testimonial_rating,
        })

    return table_data

       