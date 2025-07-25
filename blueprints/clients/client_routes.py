from flask import Blueprint, jsonify, request 
from backend.data_controllers.clients import send_invite_service

bp = Blueprint("client", __name__, url_prefix="client")

@bp.route("/", methods=["POST"])

def invitation():
    """
    Handles the sending of a testimonial invitation to a client.

    Expects JSON data in the request body containing the client's email and other necessary details.
    Delegates the invitation sending to the client_service and returns a success message.

    Returns:
        tuple: A JSON response containing a success message and HTTP status code 200.
    """
    data = request.json
    send_invite_service(data)
    return jsonify({"message": "Testimonial invitation sent successfully"}), 200

 
