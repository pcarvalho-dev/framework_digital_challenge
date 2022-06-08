from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    JWTManager(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"Hello": "World!"}), 200

    return app
