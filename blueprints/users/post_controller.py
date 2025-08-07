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
    fields: list[str]



post_bp = Blueprint('post', __name__, url_prefix='/api/post')


@post_bp.route('/create', methods=['POST'])
@login_required
def create_resource(payload: ReportPayload) -> dict:
    '''
    This function accepts a payload containing the resource name and its
    corresponding fields.
    It performs the following operations:
        1. Validates that the specified resource exists in the model registry.
        2. Filters the provided fields to include only those allowed for the resource.
        3. Creates a new record associated with the current user.
        4. Persists the new record in the database.
        
        5. Handles and logs errors, returning appropriate JSON responses
        and HTTP status codes.
    Parameters:
        payload (ReportPayload): A dictionary-like object that must include:
            - "resource" (str): The key identifying the resource to create.
            - "fields" (dict, optional): A dictionary of field names and
            values to be used when creating the record.
    Returns:
        tuple: A tuple where the first element is a JSON-encoded response (dict)
        and the second element is the HTTP status code (int).
            - On success, returns a response with status 201 and details of
            the created resource.
            - If the resource is invalid or fields are missing, returns
            a response with status 400.
            - In case of database or unexpected errors, returns a
            response with status 500.
    Raises:
        SQLAlchemyError: If a database error occurs while committing
        the transaction.
        Exception: For any other unexpected errors.
    '''
    try:
        resource = payload.get('resource')
        fields = payload.get('fields', [])

        # Validate resource
        if resource not in MODEL_REGISTRY:
            return jsonify({"error": f"Invalid resource '{resource}'"}), 400

        config = MODEL_REGISTRY[resource]
        model = config["model"]
        allowed_fields = set(config["fields"])

        # Filter payload
        filtered_payload = {k: v for k, v in fields.items() if k in allowed_fields}
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
