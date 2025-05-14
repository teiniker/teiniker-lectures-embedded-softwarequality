import unittest
from bs4 import BeautifulSoup

html_content = '''
<html>
<head>
    <title>Servlet Translator</title>
</head>
<body>
<h2>Translator </h2>
<form method="POST" action="translator" >
    <table border="0" >
        <colgroup>
            <col width="100"> <col width="100">
        </colgroup>
        <tr>
            <th align="left">
                Word:
            </th>
            <th align="left">
                <input type="text" name="word" maxlength="30" size="20"> <br>
            </th>
        </tr>

        <tr>
            <th align="left">
                Language
            </th>
            <th>
                <select name="language">
                    <option> Deutsch
                    <option> Francais
                </select>
            </th>
        </tr>
    </table>

    <table >
        <colgroup>
            <col width="50"> <col width="50"> <col width="50">
        </colgroup>
        <tr>
            <th>
                <input type="reset"  name="action" value="Reset">
            </th>
            <th/>
            <th>
                <input type="submit" name="action" value="Translate">
            </th>
        </tr>
    </table>
</form>
</body>
</html>
'''

class TestTranslatorFormHTML(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(html_content, 'html.parser')
    
    def test_title(self):
        title = self.soup.title.string.strip()
        self.assertEqual(title, "Servlet Translator")
    
    def test_form_attributes(self):
        form = self.soup.find('form')
        self.assertEqual(form.get('method'), 'POST')
        self.assertEqual(form.get('action'), 'translator')

    def test_input_word_field(self):
        input_word = self.soup.find('input', {'name': 'word'})
        self.assertIsNotNone(input_word)
        self.assertEqual(input_word.get('type'), 'text')
        self.assertEqual(input_word.get('maxlength'), '30')
        self.assertEqual(input_word.get('size'), '20')
    
    def test_language_select_options(self):
        select = self.soup.find('select', {'name': 'language'})
        self.assertIsNotNone(select)
        options = [option.text for option in select.find_all('option')]
        print(options)
        self.assertTrue('Deutsch' in options[0])
        self.assertTrue('Francais' in options[1])
    
    def test_action_buttons(self):
        inputs = self.soup.find_all('input', {'name': 'action'})
        values = {inp.get('value') for inp in inputs}
        self.assertIn('Reset', values)
        self.assertIn('Translate', values)

if __name__ == '__main__':
    unittest.main()
