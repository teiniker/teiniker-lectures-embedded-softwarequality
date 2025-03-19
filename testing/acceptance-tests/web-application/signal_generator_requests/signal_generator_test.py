import unittest
import requests

class SignalGeneratorTest(unittest.TestCase):

    # curl -i -X POST localhost:8080/generator -H "Content-Type: application/x-www-form-urlencoded" 
    #   -d 'amplitude=5&offset=-2.5&waveform=AC+%28square%29&action=Set'
    # Check for status = 200 and "Signal: AC (square) : 5 [V], -2.5 [V] offset"
    def test_happy_path(self):
        # Setup
        url = 'http://localhost:8080/generator'
        content_type = 'application/x-www-form-urlencoded'
        form_data = {
            'amplitude': 5,
            'offset': -2.5,
            'waveform': 'AC (square)',
            'action' : 'Set'
        }

        # Exercise
        response = requests.post(url,  data=form_data, timeout=5,
            headers={'Content-Type': content_type})
        
        # Verify
        status = response.status_code
        content = response.text
        print(content)
        self.assertEqual(200, status)
        self.assertTrue('Signal: AC (square) : 5 [V], -2.5 [V] offset' in content)


    # curl -i -X POST localhost:8080/generator -H "Content-Type: application/x-www-form-urlencoded"
    #   -d 'amplitude=11&offset=2.5&waveform=AC+%28triangular%29&action=Set'
    # Check for status = 200 and "Invalid signal configuration"
    def test_invalid_amplitude(self):
        # Setup
        url = 'http://localhost:8080/generator'
        content_type = 'application/x-www-form-urlencoded'
        form_data = {
            'amplitude': 11,
            'offset': 2.5,
            'waveform': 'AC (triangular)',
            'action' : 'Set'
        }

        # Exercise
        response = requests.post(url,  data=form_data, timeout=5,
            headers={'Content-Type': content_type})

        # Verify
        status = response.status_code
        content = response.text
        print(content)
        self.assertEqual(200, status)
        self.assertTrue('Invalid signal configuration' in content)


    # curl -i -X POST localhost:8080/generator -H "Content-Type: application/x-www-form-urlencoded"
    #  -d 'amplitude=5&offset=-11&waveform=DC&action=Set'
    # Check for status = 200 and "Invalid signal configuration"
    def test_invalid_offset(self):
        # Setup
        url = 'http://localhost:8080/generator'
        content_type = 'application/x-www-form-urlencoded'
        form_data = {
            'amplitude': 5,
            'offset': -11,
            'waveform': 'DC',
            'action' : 'Set'
        }

        # Exercise
        response = requests.post(url,  data=form_data, timeout=5,
            headers={'Content-Type': content_type})

        # Verify
        status = response.status_code
        content = response.text
        print(content)
        self.assertEqual(200, status)
        self.assertTrue('Invalid signal configuration' in content)


if __name__ == '__main__':
    unittest.main()
