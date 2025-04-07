import unittest
import hashlib
import os


class PasswordEncryption:

    def encrypt(self, password):
        # TODO
        pass

    def verify(self, password, password_hash):
        # TODO
        pass


class PasswordEncryptionTest(unittest.TestCase):
    def setUp(self):
        self.encyption = PasswordEncryption()

    def test_encrypt(self):
        password = "trink4bier!"
        hash = self.encyption.encrypt(password)
        print(hash)
        self.assertEqual("f806c28ecedb097b27e4d93a08a3e2fdb1b7e0766b4c6b73c0b9c162b9e5ecc2", hash)

    def test_verify(self):
        password = "trink4bier!"
        hash = "f806c28ecedb097b27e4d93a08a3e2fdb1b7e0766b4c6b73c0b9c162b9e5ecc2"
        is_valid = self.encyption.verify(password, hash)
        self.assertTrue(is_valid)

    def test_bruteforce(self):
        # TODO
        pass


if __name__ == '__main__':
    unittest.main()

# References:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
