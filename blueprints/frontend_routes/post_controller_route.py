'''
Route for fetching custom user defined reports
'''
from flask import Blueprint, request, jsonify
from flask_login import login_required
from blueprints.users.post_controller import create_resource


post_bp = Blueprint('post', __name__)

@post_bp.route('/create', methods=['POST'])
@login_required
def create_post():
    '''
    Create a new post based on the provided data.
    '''
    # Implementation goes here
    payload = request.json
    result = create_resource(payload)
    return jsonify(result), 200
