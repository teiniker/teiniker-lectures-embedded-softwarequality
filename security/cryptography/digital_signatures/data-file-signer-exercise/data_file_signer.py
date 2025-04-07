import unittest

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives import serialization

class DataFileSigner:
    # TODO
    pass


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
