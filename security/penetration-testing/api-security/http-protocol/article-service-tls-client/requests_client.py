import unittest
import requests


class ArticleServiceTest(unittest.TestCase):

    def test_find_all(self):
        response = requests.get('https://localhost:8443/articles', verify=False, timeout=5)
        print(response.status_code)
        print(response.headers['content-type'])
        print(response.text)


    def test_find_by_id(self):
        response = requests.get('https://localhost:8443/articles/1', verify=False, timeout=5)
        print(response.status_code)
        print(response.text)

    def test_insert(self):
        payload={"id":666,"description":"Design Patterns","price":9999}
        response = requests.post('https://localhost:8443/articles', verify=False, timeout=5, json=payload)
        print(response.status_code)
        print(response.text)

    def test_update(self):
        payload={"description":"Design Patterns","price":0}
        response = requests.put('https://localhost:8443/articles/1', verify=False, timeout=5, json=payload)
        print(response.status_code)
        print(response.text)

    def test_delete(self):
        response = requests.delete('https://localhost:8443/articles/2', verify=False, timeout=5)
        print(response.status_code)
        print(response.text)


if __name__ == '__main__':
    unittest.main()
