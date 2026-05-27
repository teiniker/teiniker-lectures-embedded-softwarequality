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
