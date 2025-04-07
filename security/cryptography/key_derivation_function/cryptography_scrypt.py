import unittest
import secrets
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

class ScryptTest(unittest.TestCase):

    def test_scrypt(self):
        salt = secrets.token_bytes(16)
        password = b'password'
        kdf = Scrypt(salt=salt, n=2**14, r=8, p=1, length=32)        
        key = kdf.derive(b"password")
        print(key.hex())


if __name__ == '__main__':
    unittest.main()
