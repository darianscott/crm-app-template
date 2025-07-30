'''
Parser Blueprint
-----------------
Provides an endpoint for generating post or patch request.
Features:
- Validates fields against MODEL_REGISTRY
- Searching models for existing row based on current user id
- If existing row - patches the fields
- If not existing creates a new row in the requied tabel
- Returns to the user what was done
- Logs errors
'''

import logging
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from extensions import db
from backend.models.registry.model_registry import MODEL_REGISTRY

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser_bp = Blueprint('parser', __name__, url_prefix='/api/parser')

@parser_bp.route('/custom', methods=['POST'])
@login_required
def end_point_parser():
    """
    Handles user-generated POST or PATCH requests all sent as POST.
    Validates input, dynamically builds SQLAlchemy queries, checks
    models for existing row matched with current user id, if finds 
    matching row patches in existing fields sent otherwise post
    new row, returns to user what was done, logs errors.
    """
    try:
        # --- Parse request ---
        request_data = request.get_json()
        resource = request_data.get('resource')
        payload_fields = request_data.get('fields', {})

        # --- Validate resource ---
        if resource not in MODEL_REGISTRY:
            return jsonify({"error": f"Invalid resource '{resource}'"}), 400

        config = MODEL_REGISTRY[resource]
        model = config["model"]
        allowed_fields = set(config["fields"])

        # --- Filter payload to allowed fields ---
        filtered_payload = {k: v for k, v in payload_fields.items() if k in allowed_fields}

        # --- Check for existing record ---
        existing = model.query.filter_by(user_id=current_user.id).first()

        if existing:
            # --- PATCH logic ---
            for field, value in filtered_payload.items():
                setattr(existing, field, value)
            db.session.commit()

            return jsonify({
                "method": "PATCH",
                "model": resource,
                "fields_updated": list(filtered_payload.keys()),
                "status": "updated"
            }), 200

        # --- POST logic ---
        new_instance = model(user_id=current_user.id, **filtered_payload)
        db.session.add(new_instance)
        db.session.commit()

        return jsonify({
            "method": "POST",
            "model": resource,
            "fields_created": list(filtered_payload.keys()),
            "status": "created"
        }), 201

    except Exception as e:
        # --- Error handling ---
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
