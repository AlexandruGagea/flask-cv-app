from flask import Flask
from .routes import api
from .cli import register_cli

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    register_cli(app)
    
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["AUTH_TOKEN"] = "supersecrettoken123"

    return app
