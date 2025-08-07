'''
This module defines the blueprints for the application.
I will be used to register all the routes for the app.
'''

from .frontend_routes import (delete_bp, patch_bp, post_bp, predefined_reports_bp, reports_bp)
from .auth_routes import (login_bp, register_bp, logout_bp, unauthorized_bp)
