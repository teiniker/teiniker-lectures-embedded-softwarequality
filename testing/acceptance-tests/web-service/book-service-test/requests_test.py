import unittest
import requests

class BookServiceTest(unittest.TestCase):

    # curl -i http://localhost:8080/books/1
    def test_find_by_id(self):
        # Exercise
        response = requests.get('http://localhost:8080/books/1', timeout=5)
        
        # Verify
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        json_data = response.json()
        print(response.json())
        expected = {'author': 'Eric Matthes', 'id': 1, 'isbn': '978-1718502703', 'title': 'Python Crash Course'}
        self.assertEqual(expected, json_data)

    # curl -i http://localhost:8080/books
    def test_find_all(self):
        response = requests.get('http://localhost:8080/books', timeout=5)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        print(response.json())

    # curl -i -X POST http://localhost:8080/books -H "Content-Type: application/json" 
    # -d '{"id":7, "author":"Wes McKinney ", "title":"Python for Data Analysis", "isbn":"978-1098104030"}'
    def test_insert(self):
        payload={"id":7, "author":"Wes McKinney ", "title":"Python for Data Analysis", "isbn":"978-1098104030"}
        response = requests.post('http://localhost:8080/books', timeout=5, json=payload)
        self.assertEqual(201, response.status_code)

    # curl -i -X PUT http://localhost:8080/books/2 -H "Content-Type: application/json" 
    # -d '{"author":"Brett Slatkin","title":"Effective Python", "isbn":"0134853989"}'   
    def test_update(self):
        payload={"author":"Brett Slatkin","title":"Effective Python", "isbn":"0134853989"}
        response = requests.put('http://localhost:8080/books/2', timeout=5, json=payload)
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
