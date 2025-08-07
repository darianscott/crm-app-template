'''
This is the predefined report controller. The controller
handles the creation and management of predefined reports.
'''

import logging
import io
import csv
from typing import TypedDict
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from models.registry.model_registry import MODEL_REGISTRY
from extensions import db

class ReportPayload(TypedDict):
    '''
    Represents how the report payload should be structured.
    '''
    resource: str
    fields: list[str]
    filters: dict[str, str]
    sort_by: str | None
    format: str
    page: int
    per_page: int

    # Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

defined_bp = Blueprint('defined_reports', __name__, url_prefix='/api/defined_reports')


@defined_bp.route('/', methods=['POST'])
def predefined_reports(payload: ReportPayload) -> dict:
    '''
    Create a new defined report based on the provided data.
    '''
    logger.info(f"Creating predefined report for user {current_user.id}")
    try:
        # Validate and process the payload
        # ...
        return jsonify({"message": "Report created successfully"}), 201
    except SQLAlchemyError as e:
        logger.error(f"Error creating report: {e}")
        return jsonify({"error": "Failed to create report"}), 500
