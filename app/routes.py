from flask import Blueprint, jsonify, request, abort, current_app
from .cv_data import cv_data
from .utils import doc_auth


api = Blueprint('api', __name__)

@api.before_request
def authenticate():
    token_header = request.headers.get("Authorization")
    token_query = request.args.get("token")
    expected = f"Bearer {current_app.config['AUTH_TOKEN']}"
    expected_raw = current_app.config['AUTH_TOKEN']

    if token_header == expected or token_query == expected_raw:
        return
    abort(401, description="Unauthorized: Invalid or missing token")

@api.route("/personal")
@doc_auth("docs/personal.yml")
def personal():
    return jsonify(cv_data["personal"])

@api.route("/experience")
@doc_auth("docs/experience.yml")
def experience():
    return jsonify(cv_data["experience"])

@api.route("/education")
@doc_auth("docs/education.yml")
def education():
    return jsonify(cv_data["education"])
