import requests


BASE_URL = 'https://localhost:8443/articles'


def test_find_all():
    response = requests.get(BASE_URL, verify=False, timeout=5)
    print(response.status_code)
    print(response.headers['content-type'])
    print(response.text)
    assert response.status_code == 200


def test_find_by_id():
    response = requests.get(f'{BASE_URL}/1', verify=False, timeout=5)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200


def test_insert():
    payload = {"id": 666, "description": "Design Patterns", "price": 9999}
    response = requests.post(BASE_URL, verify=False, timeout=5, json=payload)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201


def test_update():
    payload = {"description": "Design Patterns", "price": 0}
    response = requests.put(f'{BASE_URL}/1', verify=False, timeout=5, json=payload)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200


def test_delete():
    response = requests.delete(f'{BASE_URL}/2', verify=False, timeout=5)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 204
