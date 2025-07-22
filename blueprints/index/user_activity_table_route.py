from flask import Blueprint, jsonify
from backend.data_controllers.dashboard.user_activity_table import get_user_activity_table

bp = Blueprint("tables", __name__)

@bp.route("/dashboard/user-activity-table")
def get_user_activity_table():
    data = get_user_activity_table()
    return jsonify(data)
