import unittest
import hashlib
import os

# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt

class PasswordEncryption:

    def encrypt(self, password:str)->str:
        password_bytes = bytes(password,'utf-8')
        digest = hashlib.sha256()
        digest.update(password_bytes)
        password_hash = digest.hexdigest()
        return password_hash

    def verify(self, password:str, password_hash:str)->bool:
        hash = self.encrypt(password)
        return hash == password_hash


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

    def test_wordlist(self):
        password_hash = "04e77bf8f95cb3e1a36a59d1e93857c411930db646b46c218a0352e432023cf2"
        print(os.getcwd())
        file = open('wordlist.txt')
        lines = file.read().splitlines()
        for line in lines:
            hash = self.encyption.encrypt(line)
            print (line + " : " + hash)
            if(hash == password_hash):
                print(">>> found password = " + line)
                break
        file.close()

if __name__ == '__main__':
    unittest.main()
