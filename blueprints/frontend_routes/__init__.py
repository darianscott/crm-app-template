'''
This module defines the frontend routes for the application.
It will be imported into the parent folder blueprints.
Which in turn will be used to register the routes.
'''

from .delete_controller_route import delete_bp
from .patch_controller_route import patch_bp
from .post_controller_route import post_bp
from .predefined_report_controller_route import predefined_reports_bp
from .reports_bp_route import reports_bp
