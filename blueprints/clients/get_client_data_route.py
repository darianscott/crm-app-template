from flask import Blueprint, jsonify, request
from backend.models.client_model import Client
from backend.data_controllers.clients import sea

bp = Blueprint("client", __name__, url_prefix="client")

@bp.route('/api/client/search', methods=['GET'])
def search_client():
    first = request.args.get('first_name')
    last = request.args.get('last_name')
    matches = Client.query.filter_by(first_name=first, last_name=last).all()
    return jsonify([client.to_dict() for client in matches])
