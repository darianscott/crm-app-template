# app.py
from flask import Flask
from extensions import db
from backend.models import *

def create_app():
    app = Flask(__name__)

    # Example config — replace with yours
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
