import unittest
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class KeyDerivationFunctionTest(unittest.TestCase):

    def test_PBKDF2(self):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(b"password")
        print(key.hex())

if __name__ == '__main__':
    unittest.main()
