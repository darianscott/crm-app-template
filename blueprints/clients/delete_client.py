from flask import Blueprint, jsonify, request 
from backend.services.clients import add_client_service

bp = Blueprint("client", __name__, url_prefix="client")