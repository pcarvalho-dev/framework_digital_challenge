from flask import Blueprint

challenge_bp = Blueprint("challenge", __name__)

from . import views

def init_app(app):
    app.register_blueprint(challenge_bp, url_prefix="/challenge")
