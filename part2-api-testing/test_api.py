# Tests for the API

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_success():
    # Gets user 1
    res = requests.get(f"{BASE_URL}/users/1")
    assert res.status_code == 200
    data = res.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data

def test_create_post():
    # Creates a post
    post_data = {"title": "test", "body": "hello", "userId": 1}
    res = requests.post(f"{BASE_URL}/posts", json=post_data)
    assert res.status_code == 201
    data = res.json()
    for key in post_data:
        assert data[key] == post_data[key]

def test_user_not_found():
    # Gets user that doesn't exist
    res = requests.get(f"{BASE_URL}/users/999")
    assert res.status_code == 404

