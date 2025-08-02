'''
Reports Blueprint
-----------------
Provides an endpoint for generating user-customized reports.
Features:
- Validates fields and filters against MODEL_REGISTRY
- Enforces user data scope
- Supports sorting, pagination
- Optional export to CSV
- Supports JOINs for related models
'''

import logging
import io
import csv
from flask import Blueprint, request, jsonify, Response
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from models.registry.model_registry import MODEL_REGISTRY
from extensions import db


# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

reports_bp = Blueprint('reports', __name__, url_prefix='/api/reports')

@reports_bp.route('/custom', methods=['POST'])
@login_required
def generate_custom_report():
    """
    Handles user-generated report requests.
    Validates input, dynamically builds SQLAlchemy queries, and returns
    results as JSON or CSV.
    """
    try:
        # --- Parse request ---
        request_data = request.get_json()
        resource = request_data.get('resource')
        fields = request_data.get('fields', [])
        filters = request_data.get('filters', {})
        sort_by = request_data.get('sort_by')
        export_format = request_data.get('format', 'json').lower()
        page = int(request_data.get('page', 1))
        per_page = int(request_data.get('per_page', 50))

        # --- Validate resource ---
        if resource not in MODEL_REGISTRY:
            return jsonify({"error": f"Invalid resource '{resource}'"}), 400

        config = MODEL_REGISTRY[resource]
        model = config["model"]
        allowed_fields = set(config["fields"])
        allowed_filters = set(config["filters"])
        allowed_joins = config.get("joins", [])
        user_scope = config.get("user_scope")

        # --- Validate and clean fields ---
        selected_fields = [f for f in fields if f in allowed_fields]
        if not selected_fields:
            selected_fields = list(allowed_fields)  # default: all allowed

        # --- Start query ---
        query = db.session.query(*[getattr(model, f) for f in selected_fields])

        # --- Apply JOINs if requested ---
        joins = request_data.get('joins', [])
        for join in joins:
            if join in allowed_joins and join in MODEL_REGISTRY[resource]["joins"]:
            # Join via relationship attribute name on the base model
                query = query.join(getattr(model, join))

        # --- Apply filters securely ---
        for key, value in filters.items():
            if key in allowed_filters:
                query = query.filter(getattr(model, key) == value)

        # --- Enforce user scope ---
        if user_scope and hasattr(model, user_scope):
            query = query.filter(getattr(model, user_scope) == current_user.user_id)

        # --- Sorting ---
        if sort_by in allowed_fields:
            query = query.order_by(getattr(model, sort_by))

        # --- Pagination ---
        query = query.limit(per_page).offset((page - 1) * per_page)

        # --- Execute query ---
        results = query.all()

        # --- Convert to list of dicts ---
        data = [dict(zip(selected_fields, row)) for row in results]

        # --- Return response ---
        if export_format == 'csv':
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=selected_fields)
            writer.writeheader()
            writer.writerows(data)
            return Response(output.getvalue(),
                            mimetype='text/csv',
                            headers={
                                "Content-Disposition": f"attachment;"
                                "filename={resource}_report.csv"
                            })
        return jsonify({
        "resource": resource,
        "fields": selected_fields,
        "count": len(data),
        "data": data
        }), 200

    except KeyError as e:
        logger.error("Missing key: %s", e)
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except SQLAlchemyError as e:
        logger.error("Database error: %s", e)
        return jsonify({"error": "Database error occurred"}), 500
    except Exception as e:
        # Final fallback: catch any unexpected errors in report generation.
        # Specific exceptions are handled above; this ensures all
        # failures are logged with context.
        # Logs include route name and request payload for traceability.
        logger.exception("Unexpected error in generate_custom_report", request.json)
        return jsonify({"error": "Internal Server Error"}), 500
