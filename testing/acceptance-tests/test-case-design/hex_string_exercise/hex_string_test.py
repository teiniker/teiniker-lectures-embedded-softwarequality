import unittest

from hex_string import operation, ValidationError

class HexNumberTest(unittest.TestCase):

    def test_valid_hex_string(self):
        self.assertEqual(0xaa, int('AA', 16))

    def test_invalid_hex_string(self):
        with self.assertRaises(ValueError):
            int('AG', 16)

# TODO: Implement test cases here!

if __name__ == '__main__':
    unittest.main()
