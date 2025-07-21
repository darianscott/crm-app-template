from flask import Blueprint, jsonify
from backend.services.dashboard.license_table import get_license_table

bp = Blueprint("tables", __name__)

@bp.route("/dashboard/license-table")
def license_table():
    data = get_license_table()
    return jsonify(data)

