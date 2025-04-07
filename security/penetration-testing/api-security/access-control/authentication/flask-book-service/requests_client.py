import unittest
import requests
from requests.auth import HTTPBasicAuth

class BookServiceTest(unittest.TestCase):

    def test_find_all(self):
        basic = HTTPBasicAuth('bart', 'eatmyshorts')
        response = requests.get('https://localhost:8443/books', verify=False, timeout=5, auth=basic)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        print(response.text)
        content = response.json()
        self.assertEqual(1, content['data'][0]['id'])
        self.assertEqual(2, content['data'][1]['id'])
        self.assertEqual(3, content['data'][2]['id'])
        # More assertions here...

    def test_find_by_id(self):
        basic = HTTPBasicAuth('bart', 'eatmyshorts')
        response = requests.get('https://localhost:8443/books/1', verify=False, timeout=5, auth=basic)
        self.assertEqual(200, response.status_code)
        content = response.json()
        self.assertEqual(1, content['id'])
        self.assertEqual('Eric Matthes', content['author'])
        self.assertEqual('Python Crash Course', content['title'])
        self.assertEqual('978-1718502703', content['isbn'])

    def test_insert(self):
        basic = HTTPBasicAuth('bart', 'eatmyshorts')
        payload={"id":7, "author":"Wes McKinney", "title":"Python for Data Analysis", "isbn":"978-1098104030"}
        response = requests.post('https://localhost:8443/books', verify=False, timeout=5, auth=basic, json=payload)
        self.assertEqual(201, response.status_code)
        content = response.json()
        self.assertEqual(7, content['id'])
        self.assertEqual('Wes McKinney', content['author'])
        self.assertEqual('Python for Data Analysis', content['title'])
        self.assertEqual('978-1098104030', content['isbn'])

    def test_update(self):
        basic = HTTPBasicAuth('bart', 'eatmyshorts')
        payload={"author":"Brett Slatkin","title":"Effective Python", "isbn":"0134853989"}
        response = requests.put('https://localhost:8443/books/2', verify=False, timeout=5, auth=basic, json=payload)
        self.assertEqual(200, response.status_code)
        content = response.json()
        self.assertEqual(2, content['id'])
        self.assertEqual('Brett Slatkin', content['author'])
        self.assertEqual('Effective Python', content['title'])
        self.assertEqual('0134853989', content['isbn'])
        
    # If we run this test, we have to restart the service to restore the original data!!
    # def test_delete(self):
    #     basic = HTTPBasicAuth('bart', 'eatmyshorts')
    #     response = requests.delete('https://localhost:8443/books/3', verify=False, timeout=5, auth=basic)
    #     self.assertEqual(204, response.status_code)


if __name__ == '__main__':
    unittest.main()
