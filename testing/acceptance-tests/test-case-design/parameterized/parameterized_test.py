import unittest

from binary_string import operation, ValidationError

# Parameterized Tests
#
# If the logic to set up the test fixture is the same but uses different data,
# we can extract the common fixture setup, exercise SUT, and verify phases of
# the test into a new parameterized test method.
#
# We define very simple test methods for each test, which then call the
# parameterized test and pass in the data required to make this test unique.

class BinaryNumberTest(unittest.TestCase):

    def parameterized_test(self, expected, input_data):
        actual = operation(input_data)
        self.assertEqual(expected, actual)

    def parameterized_test_with_exception(self, exception, input_data):
        try:
            operation(input_data)
            self.fail()
        except exception:
            pass

    def test_valid_data1(self):
        self.parameterized_test(0b0, '00')

    def test_valid_data2(self):
        self.parameterized_test(0b11, '11')

    def test_valid_data3(self):
        self.parameterized_test(0b0, '0000')

    def test_valid_data4(self):
        self.parameterized_test(0b1111, '1111')

    def test_invalid_data_too_short0(self):
        self.parameterized_test_with_exception(ValidationError, '0')

    def test_invalid_data_too_short1(self):
        self.parameterized_test_with_exception(ValidationError, '1')

    def test_invalid_data_too_long1(self):
        self.parameterized_test_with_exception(ValidationError, '00000')

    def test_invalid_data_too_long2(self):
        self.parameterized_test_with_exception(ValidationError, '11111')

    def test_invalid_data_too_small_ascii_value(self):
        self.parameterized_test_with_exception(ValidationError, '//')

    def test_invalid_data_too_large_ascii_value(self):
        self.parameterized_test_with_exception(ValidationError, '22')

if __name__ == '__main__':
    unittest.main()

# References:
# > Parameterized Test
#    http://xunitpatterns.com/Parameterized%20Test.html
# > Python Exception Handling - Try, Except and Finally
#   https://www.programiz.com/python-programming/exception-handling
