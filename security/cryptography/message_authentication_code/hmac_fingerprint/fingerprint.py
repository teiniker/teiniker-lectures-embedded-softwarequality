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
