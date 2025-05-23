from flask import Flask
from .routes import api
from .cli import print_cv
from flasgger import Swagger
from flasgger.utils import LazyString

swagger_template = {
    "openapi": "3.0.2",
    "info": {
        "title": "Alexandru Gagea CV API",
        "description": "REST API for CV data secured by Bearer token",
        "version": "1.0"
    },
    "components": {
        "securitySchemes": {
            "Bearer": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
                "description": "Use format: Bearer <token>"
            }
        }
    },
    "security": [
        {
            "Bearer": []
        }
    ]
}

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.cli.add_command(print_cv)
    
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["AUTH_TOKEN"] = "supersecrettoken123"

    app.config['SWAGGER'] = {
        'uiversion': 3,
        'openapi': '3.0.2'
    }

    Swagger(app, template=swagger_template)

    return app
