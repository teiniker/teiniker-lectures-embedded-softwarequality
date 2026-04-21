import requests

BASE_URL = 'http://localhost:8080/articles'


# curl -i http://localhost:8080/articles
def test_find_all():
    # Exercise
    response = requests.get(BASE_URL, timeout=5)
    # Verify
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    json_data = response.json()
    ids = {item['id'] for item in json_data['data']}
    assert 1 in ids
    assert 2 in ids
    assert 3 in ids


# curl -i http://localhost:8080/articles/3
def test_find_by_id():
    # Exercise
    response = requests.get(f'{BASE_URL}/3', timeout=5)
    # Verify
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    json_data = response.json()
    assert json_data['id'] == 3
    assert json_data['description'] == "Effective Python"
    assert json_data['price'] == 2390


# curl -i -X POST localhost:8080/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'
def test_insert():
    # Exercise
    payload = {"id": 666, "description": "Design Patterns", "price": 9999}
    response = requests.post(BASE_URL, timeout=5, json=payload)
    # Verify
    assert response.status_code == 201
    assert response.headers['content-type'] == 'application/json'


# curl -i -X PUT localhost:8080/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'
def test_update():
    # Exercise
    payload = {"description": "Design Patterns", "price": 1111}
    response = requests.put(f'{BASE_URL}/2', timeout=5, json=payload)
    # Verify
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
