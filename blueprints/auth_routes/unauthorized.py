'''
This blueprint handles unauthorized access attempts.
'''
from flask import Blueprint


unauthorized_bp = Blueprint('unauthorized', __name__)

@unauthorized_bp.route('/unauthorized')
def unauthorized():
    '''
    This route is triggered when a user tries to access a resource
    that requires authentication but is not logged in.
    '''
    return "Unauthorized", 401
