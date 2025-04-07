import unittest
import hashlib
import secrets


class PasswordEncryption:
    # TODO
    pass


class PasswordEncryptionTest(unittest.TestCase):
    def setUp(self):
        self.encryption = PasswordEncryption()

    def test_encrypt(self):
        plaintext_password = "trink4bier!"
        encrypted_password = self.encryption.encrypt(plaintext_password, 1024)
        print(encrypted_password.hex())


    def test_verify(self):
        plaintext_password = "trink4bier!"
        encrypted_password = bytes.fromhex("7eda9a8030dfb2abc70a45a5548b9d557b6d64c0ece13f44fad1bc621aa9b34e5249c14165335605bf135dd25454c73b")
        is_valid = self.encryption.verify(plaintext_password, encrypted_password, 1024)
        self.assertTrue(is_valid)

    def test_encrypt_and_verify(self):
        plaintext_password = "trink4bier!"

        encrypted_password = self.encryption.encrypt(plaintext_password, 1024)
        print(encrypted_password.hex())

        is_valid = self.encryption.verify(plaintext_password, encrypted_password, 1024)
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()
