from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class FileEncryptor:
    def __init__(self, key:bytes, iv:bytes)->None:
        self.cipher = Cipher(algorithms.AES(key), modes.CTR(iv))

    def load(self, filename:str)->bytes:
        with open(filename, 'rb') as f:
            ciphertext = f.read()
        return self.decrypt(ciphertext)

    def save(self, filename:str, data:bytes)->None:
        ciphertext = self.encrypt(data)
        with open(filename, 'wb') as f:
            f.write(ciphertext)

    def encrypt(self, plaintext:bytes)->bytes:
        encryptor = self.cipher.encryptor()
        ciphertext = encryptor.update(plaintext)
        return ciphertext

    def decrypt(self, ciphertext:bytes)->bytes:
        decryptor = self.cipher.decryptor()
        plaintext = decryptor.update(ciphertext)
        return plaintext
