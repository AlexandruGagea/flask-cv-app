import os
from flask import Blueprint, jsonify, request, abort, current_app
from .cv_data import cv_data
from flasgger import swag_from

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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
@swag_from(os.path.join(BASE_DIR, "../docs/personal.yml"))
def personal():
    return jsonify(cv_data["personal"])

@api.route("/experience")
@swag_from(os.path.join(BASE_DIR, "../docs/experience.yml"))
def experience():
    return jsonify(cv_data["experience"])

@api.route("/education")
@swag_from(os.path.join(BASE_DIR, "../docs/education.yml"))
def education():
    return jsonify(cv_data["education"])
