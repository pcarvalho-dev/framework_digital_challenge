from extensions import cors, db, jwt, ma, migrate
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Extensions
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"Hello": "World!"}), 200
    
    from application import user
    user.init_app(app)

    return app
