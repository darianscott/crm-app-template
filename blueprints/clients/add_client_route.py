from flask import Blueprint, jsonify, request 
from backend.data_controllers.clients import add_client_service

bp = Blueprint("client", __name__, url_prefix="client")

@bp.route("/", methods=["POST"])
def create_client():
    """
    Handles the transport of the data to add a new client.

    Expects JSON data in the request body containing client information.
    Delegates client creation to the client_service and returns the created client as a JSON response.

    Returns:
        tuple: A JSON response containing the created client and HTTP status code 201.
    """
    data = request.json
    return 