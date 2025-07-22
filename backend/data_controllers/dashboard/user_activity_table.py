from models.client_model import Client
from models.user_model import User
from models.interactions_model import Interaction
from models.testimonials_model import Testimonial
from app import db
from datetime import datetime

def get_user_activity_table():
    def get_user_information(user):
        return {
            "userName": user.name,
            "memberSince": user.created_at.strftime("%Y-%m-%d"),
            "lastLogin": user.last_login.strftime("%Y-%m-%d") if user.last_login else "Never"
        }

    def get_user_interaction_count(user):
        thirty_days_ago = datetime.now(db.timezone.utc) - db.timedelta(days=30)
        count = db.session.query(Interaction).filter(
            Interaction.user_id == user.id,
            Interaction.created_at >= thirty_days_ago
        ).count()
        return {"clientInteractionsLogged": count}

    def get_user_client_information(user):
        active = db.session.query(Client).filter_by(user_id=user.id, status='active').count()
        archived = db.session.query(Client).filter_by(user_id=user.id, status='archived').count()
        last_month_start = datetime.now(db.timezone.utc).replace(day=1) - db.timedelta(days=1)
        last_month_start = last_month_start.replace(day=1)
        onboarded = db.session.query(Client).filter(
            Client.user_id == user.id,
            Client.created_at >= last_month_start
        ).count()
        return {
            "numOfActiveClients": active,
            "numOfClientsArchived": archived,
            "clientOnboardedLastMonth": onboarded
        }

    def get_user_testimonial_count(user):
        testimonials = db.session.query(Testimonial).filter_by(user_id=user.id).all()
        count = len(testimonials)
        avg_rating = round(sum(t.rating for t in testimonials) / count, 2) if count else None
        return {
            "testimonialsReceived": count,
            "avgTestimonialRating": avg_rating
        }

    users = db.session.query(User).filter_by(role='agent').all()
    table_data = []

    for user in users:
        row = {}
        row.update(get_user_information(user))
        row.update(get_user_interaction_count(user))
        row.update(get_user_client_information(user))
        row.update(get_user_testimonial_count(user))
        table_data.append(row)

    return table_data

       