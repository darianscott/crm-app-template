


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
    clients.send_testimonial_invite(data)
    return jsonify({"message": "Testimonial invitation sent successfully"}), 200


from flask import jsonify
from clients import client_service

@client_service.bp.route("/client/<uuid:client_id>", methods=["PUT"])
def update_client(client_id):
    """
    Handles the update of an existing client.

    Expects JSON data in the request body containing updated client information.
    Delegates client update to the client_service and returns the updated client as a JSON response.

    Args:
        client_id (uuid): The unique identifier of the client to be updated.

    Returns:
        tuple: A JSON response containing the updated client and HTTP status code 200.
    """
    data = request.json
    return jsonify(client_services.update_client(client_id, data)), 200
