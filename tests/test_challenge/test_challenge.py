import json
from random import randrange


def test_get_challenge_request(client, auth_header):
    """
    Test get challenge request
    """

    challenge_request = client.get("/challenge", headers=auth_header)
    challenge_response = challenge_request.get_json()

    assert challenge_request.status_code == 200
    assert len(challenge_response) == 5
    assert "id" in challenge_response[0]
    assert "title" in challenge_response[0]