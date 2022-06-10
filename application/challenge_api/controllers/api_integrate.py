import requests
from application.challenge_api.schemas import ApiSchema


def get_data_from_api():
    url = "https://jsonplaceholder.typicode.com/todos"
    r = requests.get(url)
    response_body = r.json()

    return ApiSchema(many=True).dump(response_body[:5])
