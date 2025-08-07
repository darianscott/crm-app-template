'''
This module defines the authentication routes for the application.
'''

from .login_route import login_bp
from .register_route import register_bp
from .unauthorized import unauthorized_bp
from .logout_route import logout_bp
