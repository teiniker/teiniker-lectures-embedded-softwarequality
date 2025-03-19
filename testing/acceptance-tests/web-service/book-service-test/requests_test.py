import unittest
import requests

class BookServiceTest(unittest.TestCase):

    def test_find_by_id(self):
        response = requests.get('http://localhost:8080/books/1', timeout=5)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        json_data = response.json()
        print(response.json())
        expected = {'author': 'Eric Matthes', 'id': 1, 'isbn': '978-1718502703', 'title': 'Python Crash Course'}
        self.assertEqual(expected, json_data)

    def test_find_all(self):
        response = requests.get('http://localhost:8080/books', timeout=5)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        print(response.json())

    def test_insert(self):
        payload={"id":7, "author":"Wes McKinney ", "title":"Python for Data Analysis", "isbn":"978-1098104030"}
        response = requests.post('http://localhost:8080/books', timeout=5, json=payload)
        self.assertEqual(201, response.status_code)

    def test_update(self):
        payload={"author":"Brett Slatkin","title":"Effective Python", "isbn":"0134853989"}
        response = requests.put('http://localhost:8080/books/2', timeout=5, json=payload)
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
