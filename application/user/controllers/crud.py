from application.common.error_return import error_return
from application.user.models import User
from application.user.schemas import UserSchema
from flask import request


def create_user() -> dict:
    """Create a new user

    Returns:
        dict: Dict with user data using schema.
    """
    request_body = request.get_json()
    data = User().manage_body(request_body).save()
    return UserSchema().dump(data)


def read_users() -> list:
    """Read all users

    Returns:
        list: List of dicts with users data using schema.
    """
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=5, type=int)

    users = User.query.filter_by(
        deleted_at=None).paginate(page, per_page, False)
    return UserSchema(many=True).dump(users.items)


def read_user(id: int) -> dict:
    """Read a user by id

    Args:
        id (int): Id of user to read.

    Returns:
        dict: Dict with user data using schema.
    """
    user = User.query.filter_by(id=id, deleted_at=None).first()
    return UserSchema().dump(user)


def update_user(id: int) -> dict:
    """Update a user by id

    Args:
        id (int): Id of user to update.

    Returns:
        dict: Dict with user data using schema.
    """
    request_body = request.get_json()
    user = User.query.filter_by(id=id, deleted_at=None).first()
    if user:
        data = user.manage_body(request_body).update()
        return UserSchema().dump(data)
    else:
        return error_return(404, "User Not Found")


def delete_user(id: int) -> None:
    """Delete a user by id

    Args:
        id (int): Id of user to delete.
    """
    user = User.query.filter_by(id=id, deleted_at=None).first()
    user.delete()
