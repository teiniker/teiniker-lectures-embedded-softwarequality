import unittest

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Signature
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/index.html
# A private key can be used to sign a message.
# This allows anyone with the public key to verify that the message was created
# by someone who possesses the corresponding private key.

class SignatureTest(unittest.TestCase):

    def setUp(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=4096)
        self.public_key = self.private_key.public_key()


    def test_sign_and_verify(self):
        message = b"Some data we want to sign"
        print('Message   : ' + message.decode('utf-8'))

        # singn a message
        signature = self.private_key.sign(
            message,
            padding.PSS(
                padding.MGF1(
                    hashes.SHA256()),
                    salt_length = padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        # Probabilistic Signature Scheme (PSS) is a padding scheme designed
        # by Mihir Bellare and Phillip Rogaway.
        print('Signature: ' + signature.hex())

        # verify a message
        self.public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf = padding.MGF1(hashes.SHA256()),
                salt_length = padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        # If the signature does not match, verify() will raise an InvalidSignature exception.

if __name__ == '__main__':
    unittest.main()
