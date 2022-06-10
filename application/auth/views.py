from application.auth import auth_bp
from application.auth.controllers.auth import get_access_token
from application.common.error_return import error_return
from flask import jsonify


@auth_bp.post("")
def login():
    """Endpoints to get access token.

    Routes:
        GET: /auth - Get access token.
    """
    try:
        data = get_access_token()
        return jsonify(data), 200
    except Exception as e:
        return error_return(500, str(e))
