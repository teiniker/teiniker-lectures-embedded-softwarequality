import unittest

from binary_string import operation, ValidationError

class BinaryNumberTest(unittest.TestCase):

    # checking int()
    def test_valid_binary_string(self):
        value = int('11110000', 2)
        self.assertEqual(240, value)

    def test_invalid_binary_string(self):
        with self.assertRaises(ValueError):
            int('012', 2)

    # valid values:
    def test_valid_data(self):
        self.assertEqual(0b0, operation('00'))
        self.assertEqual(0b11, operation('11'))
        self.assertEqual(0b0, operation('0000'))
        self.assertEqual(0b1111, operation('1111'))

    def test_invalid_data_too_short0(self):
        with self.assertRaises(ValidationError):
            operation('0')

    def test_invalid_data_too_short1(self):
        with self.assertRaises(ValidationError):
            operation('1')

    def test_invalid_data_too_long1(self):
        with self.assertRaises(ValidationError):
            operation('00000')

    def test_invalid_data_too_long2(self):
        with self.assertRaises(ValidationError):
            operation('11111')

    def test_invalid_data_too_small_ascii_value(self):
        with self.assertRaises(ValidationError):
            operation('//')

    def test_invalid_data_too_large_ascii_value(self):
        with self.assertRaises(ValidationError):
            operation('22')


if __name__ == '__main__':
    unittest.main()
