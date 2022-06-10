import json
import os

import pytest
from application.app import create_app


@pytest.fixture()
def app():
    app = create_app()
    return app


@pytest.fixture()
def auth_token(client):
    headers = {
        'Content-Type': "application/json",
        'Authorization': os.environ.get("API_SECRET_KEY")
    }

    with open('tests/mocks/login.json') as json_file:
        data = json.load(json_file)

    url = "/auth/token"
    response = client.post(url, data=data, headers=headers)
    response_body = response.get_json()

    if response.status_code == 401:
        raise KeyError('Usuário ou senha inválida')

    return response_body['access_token']


@pytest.fixture()
def auth_header(auth_token):
    headers = {
        'Content-Type': "application/json",
        'Authorization': f"Bearer {auth_token}"
    }

    return headers
