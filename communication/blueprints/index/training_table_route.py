from flask import Blueprint, jsonify
from backend.services.dashboard.training_hours_table import get_training_table

bp = Blueprint("tables", __name__)

@bp.route("/dashboard/training-hours-table")
def license_table():
    data = get_training_table()
    return jsonify(data)
