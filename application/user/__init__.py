from flask import Blueprint

user_bp = Blueprint("user", __name__)

from . import views

def init_app(app):
    app.register_blueprint(user_bp, url_prefix="/users")
