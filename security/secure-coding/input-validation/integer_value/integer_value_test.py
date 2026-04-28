import unittest

from integer_value import operation, ValidationError

# Boundary Value Analysis:
#   Valid numbers: 1, 99
#   Invalid numbers: 0, 100

class IntegerValueTest(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(1, operation(1))
        self.assertEqual(99, operation(99))

    def test_invalid_too_small(self):
        with self.assertRaises(ValidationError):
            operation(0)

    def test_invalid_too_large(self):
        with self.assertRaises(ValidationError):
            operation(100)


if __name__ == '__main__':
    unittest.main()
