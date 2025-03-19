import unittest
import requests

class SeleniumTest(unittest.TestCase):

    def test_get_request(self):
        # Setup
        url = 'http://localhost:8080/'
        # Exercise
        response = requests.get(url)
        # Verify
        content = response.text
        print(f"Response content: {content}")
        status = response.status_code
        self.assertEqual(200, status)


    def test_post_request(self):
        # Setup
        url = 'http://localhost:8080/translator'    
        data = {'word':'cat',
                'language':'Deutsch',
                'action': 'Translate'}
        # Exercise
        response = requests.post(url, data)
        # Verify
        status = response.status_code
        self.assertEqual(200, status)
        content = response.text
        print(f"Response: {response}")
        self.assertTrue('Translate: cat into Katze' in content)
        # Teardown

    def test_get_request_headers(self):
        # Setup
        url = 'http://localhost:8080/'
        # Exercise
        response = requests.get(url)
        # Verify
        headers = response.headers
        print(f"Response headers: {headers}")
        self.assertEqual('text/html;charset=UTF-8', headers['Content-Type'])

if __name__ == '__main__':
    unittest.main()
