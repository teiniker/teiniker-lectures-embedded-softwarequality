import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

BASE_URL = 'http://localhost:8080'


def test_get_request():
    # Exercise
    response = requests.get(f'{BASE_URL}/', timeout=5)
    
    # Verify
    assert response.status_code == 200

    soup = BeautifulSoup(response.text, 'html.parser')
    assert soup.title.string.strip() == "Servlet Translator"

    form = soup.find('form')
    assert form.get('method') == 'POST'
    assert form.get('action') == 'translator'

    input_word = soup.find('input', {'name': 'word'})
    assert input_word is not None
    assert input_word.get('type') == 'text'
    assert input_word.get('maxlength') == '30'
    assert input_word.get('size') == '20'

    inputs = soup.find_all('input', {'name': 'action'})
    values = {inp.get('value') for inp in inputs}
    assert 'Reset' in values
    assert 'Translate' in values


def test_post_request():
    # Exercise
    data = {'word': 'cat', 'language': 'Deutsch', 'action': 'Translate'}
    response = requests.post(f'{BASE_URL}/translator', data, timeout=5)
    
    # Verify
    assert response.status_code == 200

    soup = BeautifulSoup(response.text, 'html.parser')
    assert soup.title.string.strip() == "Translation Application"
    assert soup.find('p').string.strip() == "Translate: cat into Katze"

    link = soup.find('a')
    assert link.get('href') == 'index.html'
    assert link.text.strip() == 'back'
