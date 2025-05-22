from flask import Blueprint, jsonify
from .cv_data import cv_data

api = Blueprint('api', __name__)

@api.route("/personal")
def personal():
    return jsonify(cv_data["personal"])

@api.route("/experience")
def experience():
    return jsonify(cv_data["experience"])

@api.route("/education")
def education():
    return jsonify(cv_data["education"])
