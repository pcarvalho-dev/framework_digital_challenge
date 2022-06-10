import json
from random import randrange


def test_get_user_by_id_request(client, auth_header):
    """
    Test get user by id request
    """
    users_request = client.get("/users", headers=auth_header)
    users_response = users_request.get_json()
    user_id = users_response[0]["id"]

    user_request = client.get(f"/users/{user_id}", headers=auth_header)
    user_response = user_request.get_json()

    assert user_request.status_code == 200
    assert user_response["id"] == users_response[0]["id"]
    assert user_response["email"] == users_response[0]["email"]
    assert user_response["username"] == users_response[0]["username"]


def test_get_user_list_request(client, auth_header):
    """
    Test get users list pagination
    """
    page = randrange(3)
    per_page = randrange(10)
    users_request = client.get(
        f"/users?page={page}&per_page={per_page}", headers=auth_header)
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
        "/users", headers=auth_header, data=data)
    user_response = user_request.get_json()

    assert user_request.status_code == 200
    assert "id" in user_response[0]
    assert "email" in user_response[0]
    assert "username" in user_response[0]


def test_update_user_request(client, auth_header):
    """
    Test update user route
    """
    with open('tests/mocks/create_user.json') as json_file:
        data = json.load(json_file)

    users_request = client.get("/users", headers=auth_header)
    users_response = users_request.get_json()
    user_id = users_response[0]["id"]

    user_request = client.put(
        f"/users/{user_id}", headers=auth_header, data=data)
    user_response = user_request.get_json()

    assert user_request.status_code == 200
    assert "id" in user_response[0]
    assert "email" in user_response[0]
    assert "username" in user_response[0]
    assert user_response["username"] == data["username"]
    assert user_response["email"] == data["email"]


def test_user_delete_request(client, auth_header):
    """
    Test delete user route
    """
    users_request = client.get("/users", headers=auth_header)
    users_response = users_request.get_json()
    user_id = users_response[0]["id"]

    user_request_delete = client.delete(
        f"/users/{user_id}", headers=auth_header)

    user_request_check = client.get(f"/users/{user_id}", headers=auth_header)

    assert user_request_delete.status_code == 204
    assert user_request_check.status_code == 404
