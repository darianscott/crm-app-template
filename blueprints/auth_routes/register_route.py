'''
This blueprint handles user registration.
'''

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import User
from extensions import db


register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    '''
    This route handles user registration.
    '''
    data = request.get_json()
    hashed_pw = generate_password_hash(data['password'])
    new_user = User(username=data['username'], password_hash=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user_id": new_user.id})
