import unittest

from hex_string import operation, ValidationError


class HexNumberTest(unittest.TestCase):

    def test_valid_hex_string(self):
        self.assertEqual(0xaa, int('AA', 16))

    def test_invalid_hex_string(self):
        with self.assertRaises(ValueError):
            int('AG', 16)

    def test_valid_data(self):
        self.assertEqual(0x00, operation('00'))
        self.assertEqual(0x99, operation('99'))
        self.assertEqual(0xaa, operation('AA'))
        self.assertEqual(0xff, operation('FF'))
        self.assertEqual(0, operation('0000'))
        self.assertEqual(0x9999, operation('9999'))
        self.assertEqual(0xaaaa, operation('AAAA'))
        self.assertEqual(0xffff, operation('FFFF'))

    def test_invalid_data_too_short1(self):
        with self.assertRaises(ValidationError):
            operation('A')

    def test_invalid_data_too_short2(self):
        with self.assertRaises(ValidationError):
            operation('F')

    def test_invalid_data_too_short3(self):
        with self.assertRaises(ValidationError):
            operation('0')

    def test_invalid_data_too_short4(self):
        with self.assertRaises(ValidationError):
            operation('9')

    def test_invalid_data_too_long1(self):
        with self.assertRaises(ValidationError):
            operation('AAAAA')

    def test_invalid_data_too_long2(self):
        with self.assertRaises(ValidationError):
            operation('FFFFF')

    def test_invalid_data_too_long3(self):
        with self.assertRaises(ValidationError):
            operation('00000')

    def test_invalid_data_too_long4(self):
        with self.assertRaises(ValidationError):
            operation('99999')

    def test_invalid_data_too_small_ascii_code1(self):
        with self.assertRaises(ValidationError):
            operation('@@')

    def test_invalid_data_too_small_ascii_code2(self):
        with self.assertRaises(ValidationError):
            operation('//')

    def test_invalid_data_too_large_ascii_code1(self):
        with self.assertRaises(ValidationError):
            operation('GG')

    def test_invalid_data_too_large_ascii_code2(self):
        with self.assertRaises(ValidationError):
            operation('::')


if __name__ == '__main__':
    unittest.main()
