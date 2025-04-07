import unittest

from cryptography.hazmat.primitives import serialization

class AsymmetricKeysTest(unittest.TestCase):
    # Generate "openssl-private-key.pem" via opensSSL
    def test_load_private_key(self):
        with open("openssl-private-key.pem", "rb") as key_file:
            pk = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
            print('Private key: ' + str(pk))
            print('Public  key: ' + str(pk.public_key()))

    # Generate "openssl-public-key.pem" via opensSSL
    def test_load_public_key(self):
        with open("openssl-public-key.pem", "rb") as key_file:
            pubk = serialization.load_pem_public_key(
                key_file.read()
            )
            print('Public key: ' + str(pubk))

if __name__ == '__main__':
    unittest.main()
