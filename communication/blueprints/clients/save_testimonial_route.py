from flask import Blueprint, jsonify, request 
from backend.services.clients import client_services





bp = Blueprint("client", __name__, url_prefix="client")

@bp.route("/client", methods=["POST"])
def save_testimonial():
    """
    Handles the saving of a testimonial by extracting JSON data from the request,
    adding a new user via the user_service, and returning the result as a JSON response.

    Returns:
        tuple: A JSON response containing the result of adding a user and the HTTP status code 201.
    """
    data = request.json
    return jsonify(client_services.save_testimonial(data)), 201