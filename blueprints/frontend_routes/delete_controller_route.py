'''
Route for patching user or client data
'''
from flask import Blueprint, request, jsonify
from flask_login import login_required
from blueprints.users.delete_controller import delete_resource


delete_bp = Blueprint('delete', __name__)

@delete_bp.route('/delete', methods=['DELETE'])
@login_required
def delete_existing_resource():
    '''
    Delete an existing resource based on the provided data.
    '''
    # Implementation goes here
    payload = request.json
    result = delete_resource(payload)
    return jsonify(result), 200
