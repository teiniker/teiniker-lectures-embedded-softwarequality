import unittest
import requests

class ArticleServiceTest(unittest.TestCase):

    # curl -i http://localhost:8080/articles
    def test_find_all(self):
        response = requests.get('http://localhost:8080/articles', timeout=5)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        json_data = response.json()
        print(json_data)
        data = json_data['data']
        ids = {data['id'] for data in json_data['data']}
        self.assertTrue(1 in ids)
        self.assertTrue(2 in ids)
        self.assertTrue(3 in ids)

    # curl -i http://localhost:8080/articles/3
    def test_find_by_id(self):
        response = requests.get('http://localhost:8080/articles/3', timeout=5)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        json_data = response.json()
        print(json_data)
        self.assertEqual(3, json_data['id'])
        self.assertEqual("Effective Python", json_data['description'])
        self.assertEqual(2390, json_data['price'])


    # curl -i -X POST localhost:8080/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'
    def test_insert(self):
        payload={"id":666,"description":"Design Patterns","price":9999}
        response = requests.post('http://localhost:8080/articles', timeout=5, json=payload)
        self.assertEqual(201, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        print(response.text)

    #  curl -i -X PUT localhost:8080/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'
    def test_update(self):
        payload={"description":"Design Patterns","price":1111}
        response = requests.put('http://localhost:8080/articles/2', timeout=5, json=payload)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.headers['content-type'])
        print(response.text)

if __name__ == '__main__':
    unittest.main()
