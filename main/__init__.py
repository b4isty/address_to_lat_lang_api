from flask import Flask
from flask_cors import CORS

from instance.config import app_config


def create_app(config_name):
    """ Initialize Flask Object and add configuration"""
    config_name = "dev" if not config_name else config_name
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"

    # Swagger UI config
    app.config.SWAGGER_UI_JSONEDITOR = True
    app.config.SWAGGER_UI_DOC_EXPANSION = "none"

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app
