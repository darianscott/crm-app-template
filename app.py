'''
This is a Flask application with APScheduler for background tasks,
with login management, and database integration, this is also 
where the flask application is configured and run.
'''

from flask import Flask
from flask_apscheduler import APScheduler
from flask import Blueprint, redirect, url_for
from models import User, Client
from extensions import db, LoginManager
from blueprints import (login_bp, register_bp, logout_bp, unauthorized_bp,
    reports_bp, post_bp, patch_bp, delete_bp, predefined_reports_bp)

def create_app():
    '''
    Creating the flask application. the db instance
    '''
    app = Flask(__name__)
    scheduler = APScheduler()
    login_manager = LoginManager()

    # Example config — replace with yours
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    login_manager.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Redirect here if not logged in
    login_manager.unauthorized_handler(lambda: redirect(url_for('auth.unauthorized')))

    scheduler.init_app(app)
    scheduler.start()




    with app.app_context():
        db.create_all()

    return app
