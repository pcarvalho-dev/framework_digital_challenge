from application.user import user_bp
from application.user.controllers.crud import create_user, delete_user, read_user, read_users, update_user
from flask import request


@user_bp.get("")
@user_bp.post("")
def user_routes():
    try:
        if request.method == 'GET':
            data = read_users()
            return data
        if request.method == 'POST':
            data = create_user()
            return data
    except Exception as e:
        raise e
    
@user_bp.get("/<int:user_id>")
@user_bp.put("/<int:user_id>")
@user_bp.delete("/<int:user_id>")
def user_routes_by_id(user_id):
    try:
        if request.method == 'GET':
            data = read_user(user_id)
            return data
        if request.method == 'PUT':
            data = update_user()
            return data
        if request.method == 'DELETE':
            data = delete_user(user_id)
            return data
    except Exception as e:
        raise e
