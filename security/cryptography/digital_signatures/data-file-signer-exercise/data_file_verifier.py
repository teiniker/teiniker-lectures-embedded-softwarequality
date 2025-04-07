import unittest

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives import serialization

class DataFileVerifier:
    # TODO
    pass
  

class VerifierTest(unittest.TestCase):
    def setUp(self):
        with open("openssl-public-key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read()
            )
            self.verifier = DataFileVerifier(public_key)
            
    def test_verify_valid(self):
        self.verifier.verify_data_file('measurement')


if __name__ == '__main__':
    unittest.main()
