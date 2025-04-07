import unittest
import requests


class ArticleServiceTest(unittest.TestCase):

    def test_find_all(self):
        response = requests.get('http://localhost:8080/articles', timeout=5)
        print(response.status_code)
        print(response.headers['content-type'])
        print(response.text)


    def test_find_by_id(self):
        response = requests.get('http://localhost:8080/articles/1', timeout=5)
        print(response.status_code)
        print(response.text)

    def test_insert(self):
        payload={"id":666,"description":"Design Patterns","price":9999}
        response = requests.post('http://localhost:8080/articles', timeout=5, json=payload)
        print(response.status_code)
        print(response.text)

    def test_update(self):
        payload={"description":"Design Patterns","price":0}
        response = requests.put('http://localhost:8080/articles/1', timeout=5, json=payload)
        print(response.status_code)
        print(response.text)

    def test_delete(self):
        response = requests.delete('http://localhost:8080/articles/2', timeout=5)
        print(response.status_code)
        print(response.text)


if __name__ == '__main__':
    unittest.main()
