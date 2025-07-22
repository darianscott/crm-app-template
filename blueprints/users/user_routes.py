from flask import request, jsonify
from backend.services.users import user_services

@bp.route("/user", methods=["POST"])
def add_user():
    """
    Handles the addition of a new user.

    Expects JSON data in the request body containing user information.
    Delegates user creation to the user_service and returns the created user as a JSON response.

    Returns:
        tuple: A JSON response containing the created user and HTTP status code 201.
    """
    data = request.json
    return jsonify(user_services.add_user(data)), 201