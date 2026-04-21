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

soup = BeautifulSoup(html_content, 'html.parser')


def test_title():
    title = soup.title.string.strip()
    assert title == "Servlet Translator"


def test_form_attributes():
    form = soup.find('form')
    assert form.get('method') == 'POST'
    assert form.get('action') == 'translator'


def test_input_word_field():
    input_word = soup.find('input', {'name': 'word'})
    assert input_word is not None
    assert input_word.get('type') == 'text'
    assert input_word.get('maxlength') == '30'
    assert input_word.get('size') == '20'


def test_language_select_options():
    select = soup.find('select', {'name': 'language'})
    assert select is not None
    options = [option.text for option in select.find_all('option')]
    assert 'Deutsch' in options[0]
    assert 'Francais' in options[1]


def test_action_buttons():
    inputs = soup.find_all('input', {'name': 'action'})
    values = {inp.get('value') for inp in inputs}
    assert 'Reset' in values
    assert 'Translate' in values
