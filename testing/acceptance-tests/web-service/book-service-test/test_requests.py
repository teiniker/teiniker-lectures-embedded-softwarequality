import requests

BASE_URL = 'http://localhost:8080/books'

# curl -i http://localhost:8080/books/1
def test_find_by_id():
    response = requests.get(f'{BASE_URL}/1', timeout=5)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    expected = {'author': 'Eric Matthes', 'id': 1, 'isbn': '978-1718502703', 'title': 'Python Crash Course'}
    assert response.json() == expected

# curl -i http://localhost:8080/books
def test_find_all():
    response = requests.get(BASE_URL, timeout=5)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'

# curl -i -X POST http://localhost:8080/books -H "Content-Type: application/json"
# -d '{"id":7, "author":"Wes McKinney ", "title":"Python for Data Analysis", "isbn":"978-1098104030"}'
def test_insert():
    payload = {"id": 7, "author": "Wes McKinney ", "title": "Python for Data Analysis", "isbn": "978-1098104030"}
    response = requests.post(BASE_URL, timeout=5, json=payload)
    assert response.status_code == 201

# curl -i -X PUT http://localhost:8080/books/2 -H "Content-Type: application/json"
# -d '{"author":"Brett Slatkin","title":"Effective Python", "isbn":"0134853989"}'
def test_update():
    payload = {"author": "Brett Slatkin", "title": "Effective Python", "isbn": "0134853989"}
    response = requests.put(f'{BASE_URL}/2', timeout=5, json=payload)
    assert response.status_code == 200
