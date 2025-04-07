import unittest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class FileDecryptor:
    def __init__(self, private_key)->None:
        print(type(private_key))
        self.private_key = private_key

    def load(self, filename:str)->bytes:
        with open(filename, 'rb') as f:
            ciphertext = f.read()
        return self.decrypt(ciphertext)

    def decrypt(self, ciphertext:bytes)->bytes:
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext


class FileEncryptorTest(unittest.TestCase):
    def setUp(self):
        with open("openssl-private-key.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None
            )
            print('Private key: ' + str(private_key))
            self.decrypter = FileDecryptor(private_key)

    def test_load_bytes(self):
        data = self.decrypter.load('secure.data')
        print(data)
        self.assertEqual("000102030405060708090a0b0c0d0e0f", data.hex())


if __name__ == '__main__':
    unittest.main()
