'''
This is the route for any new data to be posted to  the db.
What it does:
-recieves json request from frontend and upackes it
-checks to make sure the resource to be deleted and id
    are in the package
-compares the resource against the registry
-if valid it executes the delete
-returns a reply
'''

import logging
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from models.registry.model_registry import MODEL_REGISTRY
from extensions import db


post_bp = Blueprint('post', __name__, url_prefix='/api/post')


@post_bp.route('/create', methods=['POST'])
@login_required
def create_resource():
    """
    Create a new resource (record) for the current user.
    """
    try:
        request_data = request.get_json()
        resource = request_data.get('resource')
        payload_fields = request_data.get('fields', {})

        # Validate resource
        if resource not in MODEL_REGISTRY:
            return jsonify({"error": f"Invalid resource '{resource}'"}), 400

        config = MODEL_REGISTRY[resource]
        model = config["model"]
        allowed_fields = set(config["fields"])

        # Filter payload
        filtered_payload = {k: v for k, v in payload_fields.items() if k in allowed_fields}
        if not filtered_payload:
            return jsonify({"error": "No valid fields provided"}), 400

        # Create new record
        new_instance = model(user_id=current_user.id, **filtered_payload)
        db.session.add(new_instance)
        db.session.commit()

        return jsonify({
            "status": "created",
            "resource": resource,
            "fields": filtered_payload
        }), 201

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500
    except Exception as e:
        logging.exception("Unexpected error in create_resource")
        return jsonify({"error": str(e)}), 500
