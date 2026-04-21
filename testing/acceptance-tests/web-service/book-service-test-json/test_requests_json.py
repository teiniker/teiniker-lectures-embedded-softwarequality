import requests

BASE_URL = 'http://localhost:8080/books'

def test_find_by_id():
    response = requests.get(f'{BASE_URL}/1', timeout=5)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    json_data = response.json()
    assert json_data['id'] == 1
    assert json_data['author'] == 'Eric Matthes'
    assert json_data['isbn'] == '978-1718502703'
    assert json_data['title'] == 'Python Crash Course'

def test_find_all():
    response = requests.get(BASE_URL, timeout=5)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    ids = [book['id'] for book in response.json()['data']]
    assert ids[0] == 1
    assert ids[1] == 2
    assert ids[2] == 3

def test_insert():
    payload = {"id": 7, "author": "Wes McKinney ", "title": "Python for Data Analysis", "isbn": "978-1098104030"}
    response = requests.post(BASE_URL, timeout=5, json=payload)
    assert response.status_code == 201

def test_update():
    payload = {"author": "Brett Slatkin", "title": "Effective Python", "isbn": "0134853989"}
    response = requests.put(f'{BASE_URL}/2', timeout=5, json=payload)
    assert response.status_code == 200
