import json
from random import randrange


def test_get_user_by_id_request(client, auth_header):
    """
    Test get user by id request
    """

    with open('tests/mocks/create_user.json') as json_file:
        data = json.load(json_file)

    create_user_request = client.post(
        "/users", headers=auth_header, data=json.dumps(data))
    create_user_response = create_user_request.get_json()
    user_id = create_user_response["id"]

    user_request = client.get(f"/users/{user_id}", headers=auth_header)
    user_response = user_request.get_json()

    assert user_request.status_code == 200
    assert user_response["id"] == create_user_response["id"]
    assert user_response["email"] == create_user_response["email"]
    assert user_response["username"] == create_user_response["username"]


def test_get_user_list_request(client, auth_header):
    """
    Test get users list pagination
    """
    per_page = randrange(10)
    for i in range(0, per_page):
        with open('tests/mocks/create_user.json') as json_file:
            data = json.load(json_file)
        client.post("/users", headers=auth_header, data=json.dumps(data))
    users_request = client.get(
        f"/users?page=1&per_page={per_page}", headers=auth_header)
    users_response = users_request.get_json()

    assert users_request.status_code == 200
    assert len(users_response) == per_page
    if len(users_response) > 0:
        assert "id" in users_response[0]
        assert "email" in users_response[0]
        assert "username" in users_response[0]


def test_create_user_request(client, auth_header):
    """
    Test create user route
    """

    with open('tests/mocks/create_user.json') as json_file:
        data = json.load(json_file)

    user_request = client.post(
        "/users", headers=auth_header, data=json.dumps(data))
    user_response = user_request.get_json()

    assert user_request.status_code == 201
    assert "id" in user_response
    assert "email" in user_response
    assert "username" in user_response


def test_update_user_request(client, auth_header):
    """
    Test update user route
    """
    
    with open('tests/mocks/create_user.json') as json_file:
        data = json.load(json_file)

    create_user_request = client.post(
        "/users", headers=auth_header, data=json.dumps(data))
    create_user_response = create_user_request.get_json()
    user_id = create_user_response["id"]

    with open('tests/mocks/update_user.json') as json_file:
        update_data = json.load(json_file)
        
    user_request = client.put(
        f"/users/{user_id}", headers=auth_header, data=json.dumps(update_data))
    user_response = user_request.get_json()

    assert user_request.status_code == 200
    assert "id" in user_response
    assert "email" in user_response
    assert "username" in user_response
    assert user_response["username"] == update_data["username"]
    assert user_response["email"] == update_data["email"]


def test_user_delete_request(client, auth_header):
    """
    Test delete user route
    """
    
    with open('tests/mocks/create_user.json') as json_file:
        data = json.load(json_file)

    create_user_request = client.post(
        "/users", headers=auth_header, data=json.dumps(data))
    create_user_response = create_user_request.get_json()
    user_id = create_user_response["id"]

    user_request_delete = client.delete(
        f"/users/{int(user_id)}", headers=auth_header)

    user_request_check = client.get(f"/users/{user_id}", headers=auth_header)

    assert user_request_delete.status_code == 204
    assert user_request_check.status_code == 404
