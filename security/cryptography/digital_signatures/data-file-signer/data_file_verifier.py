import unittest

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives import serialization

class DataFileVerifier:
    def __init__(self, public_key)->None:
        self.public_key = public_key

    def load_signature(self, filename:str):
        with open(filename + '.signature', 'rb') as f:
            signature = f.read()
            return signature

    def verify_data_file(self, filename:str)->None:
        with open(filename + '.data', 'rb') as f:
            data = f.read()
            print('Data: ' + data.hex())

            signature = self.load_signature(filename)

            self.public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf = padding.MGF1(hashes.SHA256()),
                    salt_length = padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            # If the signature does not match, verify() will raise an InvalidSignature exception.


class VerifierTest(unittest.TestCase):
    def setUp(self):
        with open("openssl-public-key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read()
            )
            self.verifier = DataFileVerifier(public_key)

    def test_verify_valid(self):
        self.verifier.verify_data_file('measurement')

    def test_verify_invalid(self):
        with self.assertRaises(InvalidSignature):
            self.verifier.verify_data_file('measurement2')


if __name__ == '__main__':
    unittest.main()
