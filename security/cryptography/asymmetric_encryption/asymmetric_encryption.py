import unittest
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class AsymmetricEncryptionTest(unittest.TestCase):

    def setUp(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=4096)
        self.public_key = self.private_key.public_key()


    def test_encryption_and_decryption(self):
        message = b"Some data we want to encrypt"
        print('Message   : ' + message.decode('utf-8'))
        print('Message   : ' + message.hex())

        # encrypt a message
        ciphertext = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print('Ciphertext: ' + ciphertext.hex())

        # decrypt a message
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print('Plaintext : ' + plaintext.hex())
        print('Plaintext : ' + plaintext.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
