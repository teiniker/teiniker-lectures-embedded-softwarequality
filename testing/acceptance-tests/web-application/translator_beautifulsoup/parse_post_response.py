import unittest
from bs4 import BeautifulSoup

html_content = '''
<!DOCTYPE HTML>
<html>
<head>
    <title>Translation Application</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
    <h2>
        <p>Translate: cat into Katze</p>
    </h2>
    <p/>
    <a href="index.html"> back</a>
</body>
</html>
'''

class TestTranslationHTML(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def test_title(self):
        title = self.soup.title.string.strip()
        self.assertEqual(title, "Translation Application")

    def test_translate_paragraph(self):
        paragraph = self.soup.find('p').string.strip()
        self.assertEqual(paragraph, "Translate: cat into Katze")

    def test_back_link(self):
        link = self.soup.find('a')
        self.assertEqual(link.get('href'), 'index.html')
        self.assertEqual(link.text.strip(), 'back')

if __name__ == '__main__':
    unittest.main()