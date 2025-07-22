from flask import Blueprint, jsonify
from backend.data_controllers.dashboard.training_hours_table import get_training_hours_table

bp = Blueprint("tables", __name__)

@bp.route("/dashboard/training_hours_table")
def training_hours_table():
    data = get_training_hours_table()
    return jsonify(data)
