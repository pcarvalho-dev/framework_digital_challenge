from flask import Blueprint

auth_bp = Blueprint("login", __name__)

from . import views


def init_app(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
