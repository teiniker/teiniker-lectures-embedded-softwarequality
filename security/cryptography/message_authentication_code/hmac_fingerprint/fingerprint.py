import unittest
import hashlib
import hmac

class Fingerprint:
    def __init__(self, key:str)->None:
        self.key_bytes = bytes.fromhex(key)
        print('key_bytes = ' + str(self.key_bytes))

    def from_file(self, filename:str)->str:
        with open(filename, 'rb') as f:
            buffer = f.read()
        return self.from_bytes(buffer)

    def from_string(self, text:str)->str:
        return self.from_bytes(bytes(text, 'utf-8'))

    def from_bytes(self, data:bytes)->str:
        digest = hmac.new(self.key_bytes, data, hashlib.sha256)
        value = digest.hexdigest()
        return value


class FingerprintTest(unittest.TestCase):
    def setUp(self):
        # The key consists of 32 random bytes
        key = "fce0ddc9bf4ad0f68d92af77b42b486bd10c27bc1b45a4c4929cda4f63bf0386"
        self.fingerprint = Fingerprint(key)

    def test_from_bytes(self):
        data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
        mac = self.fingerprint.from_bytes(data)
        print(f'mac of byte array = {mac}')
        self.assertEqual("9864b5619d85f2c0d8025bdfcf375d9f1c95aca25fea7fa235053f2f60925086", mac)

    def test_from_string(self):
        text = 'Pleased to meet you, hope you guess my name'
        mac = self.fingerprint.from_string(text)
        print(f'mac of string    = {mac}')
        self.assertEqual("a88533ad56b2acaa1d569cae1a9a6785b0a5cd2dc266ee601dc33667ff9daa6f", mac)

    def test_from_file(self):
        filename = "./tux.jpeg"
        mac = self.fingerprint.from_file(filename)
        print(f'mac of file      = {mac}')
        self.assertEqual("0f23c00edc0ae15fea5834e0ea0b447d549938fc5f267920741caf2dce1c5490", mac)

if __name__ == '__main__':
    unittest.main()
