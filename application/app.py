from application.common.error_return import error_return
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
    
    @app.errorhandler(404)
    def resource_not_found(e):
        return error_return(404, str(e))
    
    from application import user
    user.init_app(app)
    
    from application import auth
    auth.init_app(app)
    
    from application import challenge_api
    challenge_api.init_app(app)

    return app
