import unittest
import hashlib
import os

class Fingerprint:
    def from_file(self, filename:str) -> str:
        print(os.getcwd())
        with open(filename, 'rb') as f:
            buffer = f.read()
        return self.from_bytes(buffer)

    def from_string(self, text:str) -> str:
        return self.from_bytes(bytes(text,'utf-8'))

    def from_bytes(self, data:bytes) -> str:
        digest = hashlib.sha256()
        digest.update(data)
        password_hash = digest.hexdigest()
        return password_hash


class FingerprintTest(unittest.TestCase):
    def setUp(self):
        self.fingerprint = Fingerprint()

    def test_from_bytes(self):
        data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
        hash = self.fingerprint.from_bytes(data)
        self.assertEqual("be45cb2605bf36bebde684841a28f0fd43c69850a3dce5fedba69928ee3a8991", hash)

    def test_from_string(self):
        text = 'Pleased to meet you, hope you guess my name'
        hash = self.fingerprint.from_string(text)
        self.assertEqual("3b8be20de1d75d3087f5591b0687d9b3fd036a68b42dc27c5c9618a9bb72732e", hash)

    def test_from_file(self):
        filename = "./tux.jpeg"
        hash = self.fingerprint.from_file(filename)
        self.assertEqual("44eefdc0d4b5ea8d999d743e2651044f8033585ef3c97b2d69b508ad8c282cf1", hash)
        # compare with $ sha256sum tux.jpg

if __name__ == '__main__':
    unittest.main()
