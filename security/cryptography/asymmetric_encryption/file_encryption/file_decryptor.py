from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class FileDecryptor:
    def __init__(self, private_key)->None:
        print(type(private_key))
        self.private_key = private_key

    def load(self, filename:str)->bytes:
        with open(filename, 'rb') as f:
            ciphertext = f.read()
        return self.decrypt(ciphertext)

    def decrypt(self, ciphertext:bytes)->bytes:
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext
