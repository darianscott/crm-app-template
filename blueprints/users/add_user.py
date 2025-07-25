from flask import Blueprint, jsonify, request 
from backend.data_controllers.users import user_services

bp = Blueprint("user", __name__, url_prefix="user")

@bp.route("/", methods=["POST"])
def create_user():
    """
    Handles the transport of the data to add a new client.

    Expects JSON data in the request body containing client information.
    Delegates client creation to the client_service and returns the created client as a JSON response.

    Returns:
        tuple: A JSON response containing the created client and HTTP status code 201.
    """
    data = request.json
    return jsonify(user_services.add_user(data)), 201