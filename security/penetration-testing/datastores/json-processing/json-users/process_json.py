import unittest
import json

class JsonTest(unittest.TestCase):

    def test_read_json(self):
        # Exercise
        file = open('users.json', 'r', encoding="utf-8") 
        data = json.load(file)
        file.close()
        
        # Verify
        self.assertEqual(2, len(data['users']))
        first = data['users'][0]
        self.assertEqual(1, first['id'])
        self.assertEqual('homer', first['username'])
        self.assertEqual('duffbeer', first['password'])
        second = data['users'][1]
        self.assertEqual(2, second['id'])
        self.assertEqual('marge', second['username'])
        self.assertEqual('sweethome', second['password'])


if __name__ == '__main__':
    unittest.main()