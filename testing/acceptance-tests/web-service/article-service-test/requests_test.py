import unittest
import requests


class ArticleServiceTest(unittest.TestCase):

    # curl -i http://localhost:8080/articles
    def test_find_all(self):
        response = requests.get('http://localhost:8080/articles', timeout=5)
        self.assertEqual(200, response.status_code)
        print(response.headers['content-type'])
        print(response.text)

    # curl -i http://localhost:8080/articles/1
    def test_find_by_id(self):
        response = requests.get('http://localhost:8080/articles/1', timeout=5)
        self.assertEqual(200, response.status_code)
        print(response.text)

    # curl -i -X POST localhost:8080/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'
    def test_insert(self):
        payload={"id":666,"description":"Design Patterns","price":9999}
        response = requests.post('http://localhost:8080/articles', timeout=5, json=payload)
        self.assertEqual(201, response.status_code)
        print(response.text)

    #  curl -i -X PUT localhost:8080/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'
    def test_update(self):
        payload={"description":"Design Patterns","price":0}
        response = requests.put('http://localhost:8080/articles/1', timeout=5, json=payload)
        self.assertEqual(200, response.status_code)
        print(response.text)

    # curl -i -X DELETE http://localhost:8080/articles/1
    def test_delete(self):
        response = requests.delete('http://localhost:8080/articles/2', timeout=5)
        self.assertEqual(204, response.status_code)
        print(response.text)


if __name__ == '__main__':
    unittest.main()
