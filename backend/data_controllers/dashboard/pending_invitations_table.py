from models.client_model import Client
from models.user_model import User
from models.interactions_model import Interaction
from models.testimonials_model import Testimonial
from app import db
from datetime import datetime


def pending_invitations_table():
    