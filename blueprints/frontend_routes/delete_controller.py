'''
This is the route for any data to be deleted from the db.
The delete option is administration only accessable.
What it does:
-recieves json request from frontend and upackes it
-checks to make sure the resource to be deleted and id
    are in the package
-compares the resource against the registry
-if valid it executes the delete
-returns a reply
the payload must include id
'''
import logging
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from models.registry.model_registry import MODEL_REGISTRY
from extensions import db

delete_bp = Blueprint('delete', __name__, url_prefix='/api/delete')

@delete_bp.route('/delete', methods=['DELETE'])
@login_required
def delete_resource():
    """
    Delete a resource by its ID (UUID).
    """
    try:
        request_data = request.get_json()
        resource = request_data.get('resource')
        resource_id = request_data.get('id')

        if not resource_id:
            return jsonify({"error": "Missing 'id' for deletion"}), 400

        if resource not in MODEL_REGISTRY:
            return jsonify({"error": f"Invalid resource '{resource}'"}), 400

        config = MODEL_REGISTRY[resource]
        model = config["model"]

        # Fetch and enforce user ownership
        instance = model.query.filter_by(id=resource_id, user_id=current_user.id).first()
        if not instance:
            return jsonify({"error": "Resource not found or not owned by user"}), 404

        db.session.delete(instance)
        db.session.commit()

        return jsonify({
            "status": "deleted",
            "resource": resource,
            "id": resource_id
        }), 200

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred"}), 500
    except Exception as e:
        logging.exception("Unexpected error in delete_resource")
        return jsonify({"error": str(e)}), 500
