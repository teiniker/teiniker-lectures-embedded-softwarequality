import unittest
import secrets
from hashlib import pbkdf2_hmac


class KeyDerivationFunctionTest(unittest.TestCase):

    def test_PBKDF2(self):
        salt = secrets.token_bytes(16)
        password = b'password'
        iterations = 500000
        key_len = 32
        key = pbkdf2_hmac('sha256', password, salt, iterations, key_len)
        print(key.hex())
    

if __name__ == '__main__':
    unittest.main()
