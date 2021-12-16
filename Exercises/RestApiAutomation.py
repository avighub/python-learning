"""
pre requisite:
    - pytest
    - requests
    - dummy AUT: https://reqres.in/
"""
import pytest
import requests


# GET Request
def test_get_single_user_details_and_check_for_200code():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    assert response.headers["Age"] == 2330


def test_get_single_user_details_and_check_for_headers():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    assert response.headers["Access-control-Allow-Origin"] == "*"


def test_get_single_user_details_and_check_for_id():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    response_body = response.json()
    assert "data" in response_body
# POST Request
