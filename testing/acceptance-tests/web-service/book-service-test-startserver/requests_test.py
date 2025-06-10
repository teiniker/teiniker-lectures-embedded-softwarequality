import unittest
import time
import multiprocessing
import requests
from book_service import app

def run_app():
    app.run(port=8080, debug=False, use_reloader=False)

class BookServiceTest(unittest.TestCase):

    def setUp(self):
        self.server = multiprocessing.Process(target=run_app)
        self.server.start()
        time.sleep(1)  # Give the server time to start

    def tearDown(self):
        self.server.terminate()
        self.server.join()

    def test_find_by_id(self):
        response = requests.get('http://localhost:8080/books/1', timeout=5)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        # Verify the JSON response
        json_data = response.json()
        self.assertEqual(1, json_data['id'])
        self.assertEqual('Eric Matthes', json_data['author'])
        self.assertEqual('978-1718502703', json_data['isbn'])
        self.assertEqual('Python Crash Course', json_data['title'])

    def test_find_all(self):
        response = requests.get('http://localhost:8080/books', timeout=5)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        # Verify all the 'id' fields
        json_data = response.json()
        ids = []
        for book in json_data['data']:
            ids.append(book['id'])
        self.assertEqual(1, ids[0])
        self.assertEqual(2, ids[1])
        self.assertEqual(3, ids[2])

    def test_insert(self):
        payload={"id":7, "author":"Wes McKinney ", "title":"Python for Data Analysis", "isbn":"978-1098104030"}
        response = requests.post('http://localhost:8080/books', timeout=5, json=payload)
        self.assertEqual(201, response.status_code)

    def test_update(self):
        payload={"author":"Brett Slatkin","title":"Effective Python", "isbn":"0134853989"}
        response = requests.put('http://localhost:8080/books/2', timeout=1, json=payload)
        self.assertEqual(200, response.status_code)

    def test_delete(self):
        response = requests.delete('http://localhost:8080/books/2', timeout=1)
        self.assertEqual(204, response.status_code)

if __name__ == '__main__':
    unittest.main()
