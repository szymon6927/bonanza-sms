import requests
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__,
                instance_relative_config=True,
                static_folder="../dist/static",
                template_folder="../dist")
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        if app.debug:
            return requests.get('http://localhost:8081/{}'.format(path)).text
        return render_template("index.html")

    migrate = Migrate(app, db)

    from app.models import Users, Clients

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
