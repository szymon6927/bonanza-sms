import requests
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
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

    @app.route('/client', methods=["POST"])
    def get_client():
        test = request.form["phone"]
        print(test, flush=True)

    return app
