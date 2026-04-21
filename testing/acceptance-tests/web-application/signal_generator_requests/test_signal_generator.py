import requests

BASE_URL = 'http://localhost:8080/generator'
CONTENT_TYPE = 'application/x-www-form-urlencoded'


# curl -i -X POST localhost:8080/generator -H "Content-Type: application/x-www-form-urlencoded"
#   -d 'amplitude=5&offset=-2.5&waveform=AC+%28square%29&action=Set'
# Check for status = 200 and "Signal: AC (square) : 5 [V], -2.5 [V] offset"
def test_happy_path():
    form_data = {
        'amplitude': 5,
        'offset': -2.5,
        'waveform': 'AC (square)',
        'action': 'Set'
    }
    response = requests.post(BASE_URL, data=form_data, timeout=5,
        headers={'Content-Type': CONTENT_TYPE})
    assert response.status_code == 200
    assert 'Signal: AC (square) : 5 [V], -2.5 [V] offset' in response.text


# curl -i -X POST localhost:8080/generator -H "Content-Type: application/x-www-form-urlencoded"
#   -d 'amplitude=11&offset=2.5&waveform=AC+%28triangular%29&action=Set'
# Check for status = 200 and "Invalid signal configuration"
def test_invalid_amplitude():
    form_data = {
        'amplitude': 11,
        'offset': 2.5,
        'waveform': 'AC (triangular)',
        'action': 'Set'
    }
    response = requests.post(BASE_URL, data=form_data, timeout=5,
        headers={'Content-Type': CONTENT_TYPE})
    assert response.status_code == 200
    assert 'Invalid signal configuration' in response.text


# curl -i -X POST localhost:8080/generator -H "Content-Type: application/x-www-form-urlencoded"
#  -d 'amplitude=5&offset=-11&waveform=DC&action=Set'
# Check for status = 200 and "Invalid signal configuration"
def test_invalid_offset():
    form_data = {
        'amplitude': 5,
        'offset': -11,
        'waveform': 'DC',
        'action': 'Set'
    }
    response = requests.post(BASE_URL, data=form_data, timeout=5,
        headers={'Content-Type': CONTENT_TYPE})
    assert response.status_code == 200
    assert 'Invalid signal configuration' in response.text
