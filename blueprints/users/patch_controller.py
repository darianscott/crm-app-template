
'''
This is the route for any data to be patched to the db.
What it does:
-recieves json request from frontend and upackes it
-checks to make sure the resource to be deleted and id
    are in the package
-compares the resource against the registry
-if valid it executes the delete
-returns a reply
-the payload must include id
'''

import logging
from typing import TypedDict
from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from models.registry.model_registry import MODEL_REGISTRY
from extensions import db

class ReportPayload(TypedDict):
    '''
    Represents how the report payload should be structured.
    '''
    resource: str
    resource_id: str
    fields: list[str]


patch_bp = Blueprint('patch', __name__, url_prefix='/api/patch')

@patch_bp.route('/update', methods=['PATCH'])
@login_required
def update_resource(payload: ReportPayload) -> dict:
    """
    Update an existing resource by its ID or unique key.
    """
    try:
        resource = payload.get('resource')
        resource_id = payload.get('resourceid')  # UUID of the record
        payload_fields = payload.get('fields', {})

        if not resource_id:
            return jsonify({"error": "Missing 'id' for update"}), 400

        if resource not in MODEL_REGISTRY:
            return jsonify({"error": f"Invalid resource '{resource}'"}), 400

        resource = payload.get('resource')
        resource_id = payload.get('resource_id')  # UUID of the record
        payload_fields = payload.get('fields', {})

        if not resource_id:
            return jsonify({"error": "Missing 'id' for update"}), 400

        if resource not in MODEL_REGISTRY:
            return jsonify({"error": f"Invalid resource '{resource}'"}), 400

        config = MODEL_REGISTRY[resource]
        model = config["model"]
        allowed_fields = set(config["fields"])

        # Validate fields
        filtered_payload = {k: v for k, v in payload_fields.items() if k in allowed_fields}

        # Fetch record and enforce user ownership
        instance = model.query.filter_by(id=resource_id, user_id=current_user.id).first()
        if not instance:
            return jsonify({"error": "Resource not found or not owned by user"}), 404

        # Update
        for field, value in filtered_payload.items():
            setattr(instance, field, value)
        db.session.commit()

        return jsonify({
            "status": "updated",
            "resource": resource,
            "id": resource_id,
            "fields_updated": list(filtered_payload.keys())
        }), 200

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500
    except Exception as e:
        logging.exception("Unexpected error in update_resource")
        return jsonify({"error": str(e)}), 500
