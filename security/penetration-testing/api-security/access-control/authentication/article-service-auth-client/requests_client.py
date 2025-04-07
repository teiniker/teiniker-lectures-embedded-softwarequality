import unittest
import requests
from requests.auth import HTTPBasicAuth

class ArticleServiceTest(unittest.TestCase):

    def test_find_all(self):
        basic = HTTPBasicAuth('student', 'student')
        response = requests.get('https://localhost:8443/articles', verify=False, timeout=5, auth=basic)
        print(response.status_code)
        print(response.headers['content-type'])
        print(response.text)


    def test_find_by_id(self):
        basic = HTTPBasicAuth('student', 'student')
        response = requests.get('https://localhost:8443/articles/1', verify=False, timeout=5, auth=basic)
        print(response.status_code)
        print(response.text)

    def test_insert(self):
        basic = HTTPBasicAuth('student', 'student')
        payload={"id":666,"description":"Design Patterns","price":9999}
        response = requests.post('https://localhost:8443/articles', verify=False, timeout=5, auth=basic, json=payload)
        print(response.status_code)
        print(response.text)

    def test_update(self):
        basic = HTTPBasicAuth('student', 'student')
        payload={"description":"Design Patterns","price":0}
        response = requests.put('https://localhost:8443/articles/1', verify=False, timeout=5, auth=basic, json=payload)
        print(response.status_code)
        print(response.text)

    def test_delete(self):
        basic = HTTPBasicAuth('student', 'student')
        response = requests.delete('https://localhost:8443/articles/2', verify=False, timeout=5, auth=basic)
        print(response.status_code)
        print(response.text)


if __name__ == '__main__':
    unittest.main()
