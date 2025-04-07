import unittest
import hashlib
import secrets


class PasswordEncryption:

    def encrypt(self, plaintext_password:str, iterations:int)->bytes:
        salt = secrets.token_bytes(16)
        print(f'salt: {salt.hex()}')
        encrypted_password = self.encrypt_with_salt(salt, plaintext_password, iterations)
        print(f'encrypted: {encrypted_password.hex()}')
        return encrypted_password

    def verify(self, plaintext_password:str, encrypted_password:bytes, iterations:int)->bool:
        salt = encrypted_password[0:16]
        print(f'salt: {salt.hex()}')
        new_encrypted_password = self.encrypt_with_salt(salt, plaintext_password, iterations)
        print(f'encrypted: {new_encrypted_password.hex()}')
        return new_encrypted_password  == encrypted_password

    def encrypt_with_salt(self, salt:bytes, plaintext_password:str, iterations:int)->bytes:
        password_bytes = salt + bytes(plaintext_password,'utf-8')
        print(f'password_bytes: {password_bytes.hex()}')
        digest = hashlib.sha256()
        for _ in range(iterations):
            digest.update(password_bytes)
            password_bytes = digest.digest()
        encrypted_password = salt + password_bytes
        return encrypted_password


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
