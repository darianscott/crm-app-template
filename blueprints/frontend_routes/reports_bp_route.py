'''
Route for fetching custom user defined reports
'''
from flask import Blueprint, request, jsonify
from flask_login import login_required
from blueprints.users.reports_service_controller import generate_custom_report


reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/custom', methods=['POST'])
@login_required
def custom_report():
    '''
    Generate a custom user-defined report based on the provided criteria.
    '''
    # Implementation goes here
    payload = request.json
    result = generate_custom_report(payload)
    return jsonify(result), 200
