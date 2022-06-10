import os

from application.auth import auth_bp
from application.user.models import User
from flask import abort, request
from flask_jwt_extended import create_access_token
from sqlalchemy import or_


@auth_bp.post("")
def login():
    basic = request.headers.get("Authorization")
    login = request.json.get("login", None)
    password = request.json.get("password", None)
    secret_key = os.environ.get('API_SECRET_KEY')

    if basic != secret_key:
        abort(401, "Invalid Basic Token")
    if not basic:
        abort(401, "Missing Basic Token")

    user = User.query.filter(or_(
        User.username == login,
        User.email == login
    )).first()

    if user:
        if user.check_password(password):
            access_token = create_access_token(identity=login)
            return {"access_token": access_token}
        else:
            abort(401, "Invalid Password")
    else:
        abort(404, "User not found")
