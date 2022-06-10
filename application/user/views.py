from application.common.error_return import error_return
from application.user import user_bp
from application.user.controllers.crud import (create_user, delete_user,
                                               read_user, read_users,
                                               update_user)
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity


@user_bp.get("")
@user_bp.post("")
def user_routes():
    """Endpoints to get and create users.

    Routes:
        GET: /user - Get all users.
        POST: /user - Create a new user.
    """
    try:
        if request.method == "GET":
            data = read_users()
            return jsonify(data)
        if request.method == "POST":
            data = create_user()
            return data
    except Exception as e:
        return error_return(500, str(e))
    
@user_bp.get("/<int:user_id>")
@user_bp.put("/<int:user_id>")
@user_bp.delete("/<int:user_id>")
@jwt_required()
def user_routes_by_id(user_id):
    """Endpoints to get, update and delete users.

    Routes:
        GET: /user - Get user by id.
        PUT: /user - Update user by id.
        DELETE: /user - Delete user by id.
    """
    try:
        if request.method == "GET":
            data = read_user(user_id)
            return data
        if request.method == "PUT":
            data = update_user()
            return data
        if request.method == "DELETE":
            data = delete_user(user_id)
            return data
    except Exception as e:
        return error_return(500, str(e))
