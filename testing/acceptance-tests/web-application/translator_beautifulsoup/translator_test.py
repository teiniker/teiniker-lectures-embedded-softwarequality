import unittest
import requests
from bs4 import BeautifulSoup

class BeautifulSoupTest(unittest.TestCase):

    def test_get_request(self):
        # Setup
        url = 'http://localhost:8080/'
        # Exercise
        response = requests.get(url)
        # Verify
        self.assertEqual(200, response.status_code)
        
        # Parse the HTML content
        content = response.text
        #print(content)
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.title.string.strip()
        self.assertEqual(title, "Servlet Translator")

        form = soup.find('form')
        self.assertEqual(form.get('method'), 'POST')
        self.assertEqual(form.get('action'), 'translator')

        input_word = soup.find('input', {'name': 'word'})
        self.assertIsNotNone(input_word)
        self.assertEqual(input_word.get('type'), 'text')
        self.assertEqual(input_word.get('maxlength'), '30')
        self.assertEqual(input_word.get('size'), '20')

        inputs = soup.find_all('input', {'name': 'action'})
        values = {inp.get('value') for inp in inputs}
        self.assertIn('Reset', values)
        self.assertIn('Translate', values)


    def test_post_request(self):
        # Setup
        url = 'http://localhost:8080/translator'    
        data = {'word':'cat',
                'language':'Deutsch',
                'action': 'Translate'}
        # Exercise
        response = requests.post(url, data)
        # Verify
        self.assertEqual(200, response.status_code)

        # Parse the HTML content
        content = response.text
        #print(content)
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.title.string.strip()
        self.assertEqual(title, "Translation Application")

        paragraph = soup.find('p').string.strip()
        self.assertEqual(paragraph, "Translate: cat into Katze")

        link = soup.find('a')
        self.assertEqual(link.get('href'), 'index.html')
        self.assertEqual(link.text.strip(), 'back')


if __name__ == '__main__':
    unittest.main()
