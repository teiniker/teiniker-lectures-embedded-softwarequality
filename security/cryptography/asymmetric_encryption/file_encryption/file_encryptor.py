import unittest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class FileEncryptor:
    def __init__(self, public_key)->None:
        print(type(public_key))
        self.public_key = public_key

    def save(self, filename:str, data:bytes)->None:
        ciphertext = self.encrypt(data)
        with open(filename, 'wb') as f:
            f.write(ciphertext)

    def encrypt(self, plaintext:bytes)->bytes:
        ciphertext = self.public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext


class FileEncryptorTest(unittest.TestCase):
    def setUp(self):
        with open("openssl-public-key.pem", "rb") as key_file:
            pubk = serialization.load_pem_public_key(
                key_file.read()
            )
            self.encrypter = FileEncryptor(pubk)

    def test_save_bytes(self):
        data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
        self.encrypter.save('secure.data', data)


if __name__ == '__main__':
    unittest.main()
