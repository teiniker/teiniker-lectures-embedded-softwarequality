import unittest

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives import serialization

class DataFileSigner:
    def __init__(self, private_key)->None:
        self.private_key = private_key

    def save_signature(self, filename:str, signature)->None:
        with open(filename + '.signature', 'wb') as f:
            f.write(signature)

    def sign_data_file(self, filename:str)->None:
        with open(filename + '.data', 'rb') as f:
            data = f.read()
            print(data.hex())

            signature = self.private_key.sign(
                data,
                padding.PSS(
                    padding.MGF1(
                        hashes.SHA256()),
                        salt_length = padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )
            print(signature.hex())
            self.save_signature(filename, signature)


class SignatureTest(unittest.TestCase):

    def setUp(self):
        with open("openssl-private-key.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None
            )
            print('Private key: ' + str(private_key))
            self.signer = DataFileSigner(private_key)

    def test_signing(self):
        self.signer.sign_data_file('measurement')


if __name__ == '__main__':
    unittest.main()
