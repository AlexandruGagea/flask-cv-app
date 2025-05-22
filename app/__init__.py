from flask import Flask
from .routes import api
from .cli import print_cv
from flasgger import Swagger

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Alexandru Gagea CV API",
        "description": "REST API for CV data secured by Bearer token",
        "version": "1.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Use format: **Bearer &lt;token&gt;**"
        }
    }
}

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.cli.add_command(print_cv)
    
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["AUTH_TOKEN"] = "supersecrettoken123"
    app.config['SWAGGER'] = {
        'title': 'Alexandru Gagea CV API',
        'uiversion': 3
    }

    Swagger(app, template=swagger_template)

    return app
