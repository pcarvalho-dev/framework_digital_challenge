from application.challenge_api import challenge_bp
from application.challenge_api.controllers.api_integrate import \
    get_data_from_api
from application.common.error_return import error_return
from flask import jsonify, request
from flask_jwt_extended import jwt_required


@challenge_bp.get("")
@jwt_required()
def user_routes():
    """Endpoint to get challenge api data.

    Routes:
        GET: /user - Get all data in https://jsonplaceholder.typicode.com/todos.
    """
    try:
        if request.method == "GET":
            data = get_data_from_api()
            return jsonify(data)
    except Exception as e:
        return error_return(500, str(e))
    
