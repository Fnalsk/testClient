import requests

from typing import Any
from flask import Response
from flask.json import jsonify as flask_jsonify
from constants import BASE_APP_URI


def insert_sample_key_value_pair(key: str, value: str) -> None:
    """
    Request the server to insert a key value pair for testing.
    """
    requests.post(
        f"{BASE_APP_URI}/store-value",
        jsonify_meta(
            {
                "key": key,
                "value": value
            }
        )
    )
    get_value_response = requests.get(f"{BASE_APP_URI}/get-value/{key}")
    assert is_success_status_code(get_value_response.status_code)
    assert get_value_response.json()["meta"]["value"] == value


def jsonify_meta(message: Any) -> Response:
    """
    Formats a JSON response containing meta information that adheres to JSON API specification.
    """
    return flask_jsonify(**{"meta": message})


def is_success_status_code(code: int) -> bool:
    """
    Return whether the given status code is a success.
    """
    return (code // 100) == 2

