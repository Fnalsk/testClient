import requests
from flask import Response

from constants import BASE_APP_URI
from exceptions import NotFound
from application.features.utils import jsonify_meta, is_success_status_code


def test_deletion() -> Response:
    """
    Test the deletion of a key from the database.
    """
    key = "key"
    insert_sample_key_value_pair(key, "value")

    requests.delete(f"{BASE_APP_URI}/delete-key/{key}")

    get_value_response = requests.get(f"{BASE_APP_URI}/get-value/{key}")
    assert get_value_response.status_code == NotFound.status
    return jsonify_meta("Deletion test successful.")


def test_overwrite() -> Response:
    """
    Test overwriting of a value in the database.
    """
    insert_sample_key_value_pair("key", "value")
    insert_sample_key_value_pair("key", "value2")
    return jsonify_meta("Overwrite test successful.")


def insert_sample_key_value_pair(key: str, value: str) -> None:
    """
    Request the server to insert a key value pair for testing.
    """
    requests.post(
        f"{BASE_APP_URI}/store-value",
        json={
            "meta": {
                "key": key,
                "value": value
            }
        }
    )
    get_value_response = requests.get(f"{BASE_APP_URI}/get-value/{key}")
    assert is_success_status_code(get_value_response.status_code)
    assert get_value_response.json()["meta"]["value"] == value



