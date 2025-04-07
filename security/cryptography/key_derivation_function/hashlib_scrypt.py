import unittest
import secrets
from hashlib import scrypt

class ScryptTest(unittest.TestCase):

    def test_scrypt(self):
        salt = secrets.token_bytes(16)
        password = b'password'
        key_len = 32        
        key = scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=key_len)
        print(key.hex())


if __name__ == '__main__':
    unittest.main()
