import requests

BASE_URL = 'http://localhost:8080'


def test_get_request():
    # Exercise
    response = requests.get(f'{BASE_URL}/', timeout=5)
    # Verify
    assert response.status_code == 200


def test_post_request():
    # Exercise
    data = {'word': 'cat', 'language': 'Deutsch', 'action': 'Translate'}
    response = requests.post(f'{BASE_URL}/translator', data, timeout=5)
    # Verify
    assert response.status_code == 200
    assert 'Translate: cat into Katze' in response.text


def test_get_request_headers():
    # Exercise
    response = requests.get(f'{BASE_URL}/', timeout=5)
    # Verify
    assert response.headers['Content-Type'] == 'text/html;charset=UTF-8'
