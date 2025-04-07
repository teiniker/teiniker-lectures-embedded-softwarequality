import unittest
import hashlib
import secrets


class PasswordEncryption:

    def encrypt(self, plaintext_password:str)->bytes:
        salt = secrets.token_bytes(16)
        print(f'salt: {salt.hex()}')
        encrypted_password = self.encrypt_with_salt(salt, plaintext_password)
        print(f'encrypted: {encrypted_password.hex()}')
        return encrypted_password

    def verify(self, plaintext_password:str, encrypted_password:bytes)->bool:
        salt = encrypted_password[0:16]
        print(f'salt: {salt.hex()}')
        new_encrypted_password = self.encrypt_with_salt(salt, plaintext_password)
        print(f'encrypted: {new_encrypted_password.hex()}')
        return new_encrypted_password  == encrypted_password

    def encrypt_with_salt(self, salt:bytes, plaintext_password:str)->bytes:
        password_bytes = bytes(plaintext_password,'utf-8')
        digest = hashlib.sha256()
        digest.update(salt)
        digest.update(password_bytes)
        password_hash = digest.digest()
        encrypted_password = salt + password_hash
        return encrypted_password


class PasswordEncryptionTest(unittest.TestCase):
    def setUp(self):
        self.encryption = PasswordEncryption()

    def test_encrypt(self):
        plaintext_password = "trink4bier!"
        encrypted_password = self.encryption.encrypt(plaintext_password)
        print(encrypted_password.hex())

    def test_verify(self):
        plaintext_password = "trink4bier!"
        encrypted_password = bytes.fromhex("e7f7c77cdc8eb67d0918153adc89fed4837bf136db5dab1a66d3365f56c652bb5937abecb0d81e1101f8a6dbc83c1fdc")
        is_valid = self.encryption.verify(plaintext_password, encrypted_password)
        self.assertTrue(is_valid)

    def test_encrypt_and_verify(self):
        plaintext_password = "trink4bier!"

        encrypted_password = self.encryption.encrypt(plaintext_password)
        print(encrypted_password.hex())

        is_valid = self.encryption.verify(plaintext_password, encrypted_password)
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()
