from flask import Blueprint, jsonify
from backend.services.dashboard.user_activity_table import get_user_activity_table

bp = Blueprint("tables", __name__)

@bp.route("/dashboard/user-activity-table")
def license_table():
    data = get_user_activity_table()
    return jsonify(data)
