'''
Route for fetching custom user defined reports
'''
from flask import Blueprint, request, jsonify
from flask_login import login_required
from blueprints.users.predefined_report_controller import predefined_reports

predefined_reports_bp = Blueprint('predefined_reports', __name__)

@predefined_reports_bp.route('/custom', methods=['POST'])
@login_required
def create_predefined_report():
    '''
    The route for creating and returning a predefined report.
    '''
    payload = request.json
    result = predefined_reports(payload)
    return jsonify(result), 200
