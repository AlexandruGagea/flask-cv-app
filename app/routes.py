from flask import Blueprint, jsonify
from .cv_data import cv_data
from .auth import require_auth

api = Blueprint('api', __name__)

@api.route("/personal")
@require_auth
def personal():
    return jsonify(cv_data["personal"])

@api.route("/experience")
@require_auth
def experience():
    return jsonify(cv_data["experience"])

@api.route("/education")
@require_auth
def education():
    return jsonify(cv_data["education"])
