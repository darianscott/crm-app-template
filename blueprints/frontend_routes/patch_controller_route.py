'''
Route for patching user or client data
'''
from flask import Blueprint, request, jsonify
from flask_login import login_required
from blueprints.users.patch_controller import update_resource


patch_bp = Blueprint('patch', __name__)

@patch_bp.route('/update', methods=['PATCH'])
@login_required
def update_existing_resource():
    '''
    Update an existing resource based on the provided data.
    '''
    # Implementation goes here
    payload = request.json
    result = update_resource(payload)
    return jsonify(result), 200
