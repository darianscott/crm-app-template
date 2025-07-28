from flask import Blueprint, jsonify, request
from data_controllers.clients import update_client_service

bp = Blueprint("client", __name__, url_prefix="client")

@bp.route("/", methods=["PATCH"])
def update_client():
    """
    Handles the transport of the data to add a new client.

    Expects JSON data in the request body containing client information.
    Delegates client creation to the client_service and returns the created client as a JSON response.

    Returns:
        tuple: A JSON response containing the created client and HTTP status code 201.
    """
    data = request.json
    return jsonify(update_client_service.add_client(data)), 201
