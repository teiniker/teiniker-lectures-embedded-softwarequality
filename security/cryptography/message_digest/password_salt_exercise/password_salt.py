import unittest
import hashlib
import secrets


class PasswordEncryption:
    pass
    # TODO


class PasswordEncryptionTest(unittest.TestCase):
    def setUp(self):
        self.encryption = PasswordEncryption()

    def test_encrypt(self):
        plaintext_password = "trink4bier!"
        encrypted_password = self.encryption.encrypt(plaintext_password)
        print(encrypted_password.hex())

    def test_verify(self):  # (5 Points)
        plaintext_password = "trink4bier!"
        # salt = "e7f7c77cdc8eb67d0918153adc89fed4"
        encrypted_password = bytes.fromhex("e7f7c77cdc8eb67d0918153adc89fed4837bf136db5dab1a66d3365f56c652bb5937abecb0d81e1101f8a6dbc83c1fdc")
        is_valid = self.encryption.verify(plaintext_password, encrypted_password)
        self.assertTrue(is_valid)

    def test_encrypt_and_verify(self): # (5 Points)
        plaintext_password = "trink4bier!"

        encrypted_password = self.encryption.encrypt(plaintext_password)
        print(encrypted_password.hex())

        is_valid = self.encryption.verify(plaintext_password, encrypted_password)
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()
