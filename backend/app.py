from flask import Flask
from flask_smorest import Api
from os import environ

from db import db
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    app.config["PROPAGATE_EXCEPTIONS"] = True
    
    mySQLUser = environ.get("MYSQL_USER")
    mySQLPassword = environ.get("MYSQL_PASSWORD")
    mySQLDatabase = environ.get("MYSQL_DATABASE")
    mySQLHost = environ.get("MYSQL_HOST")

    # Configuring database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{mySQLUser}:{mySQLPassword}@{mySQLHost}/{mySQLDatabase}"

    # Disable modification tracking
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)

    return app
