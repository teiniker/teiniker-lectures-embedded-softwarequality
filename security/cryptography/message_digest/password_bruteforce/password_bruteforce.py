import hashlib

# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt

class PasswordEncryption:

    def encrypt(self, password:str)->str:
        password_bytes = bytes(password,'utf-8')
        digest = hashlib.sha256()
        digest.update(password_bytes)
        password_hash = digest.hexdigest()
        return password_hash

    def verify(self, password:str, password_hash:str)->bool:
        hash_value = self.encrypt(password)
        return hash_value == password_hash
