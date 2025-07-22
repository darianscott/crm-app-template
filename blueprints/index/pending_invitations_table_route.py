from flask import Blueprint, jsonify
from backend.data_controllers.dashboard.pending_invitations_table import get_pending_invitations_table

bp = Blueprint("tables", __name__)

@bp.route("/dashboard/pending-invitations-table")
def pending_invitations_table():
    data = get_pending_invitations_table()
    return jsonify(data)

