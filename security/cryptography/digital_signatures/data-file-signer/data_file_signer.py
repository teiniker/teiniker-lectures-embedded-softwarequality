from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class DataFileSigner:
    def __init__(self, private_key)->None:
        self.private_key = private_key

    def save_signature(self, filename:str, signature:bytes)->None:
        with open(filename + '.signature', 'wb') as f:
            f.write(signature)

    def sign_data_file(self, filename:str)->None:
        with open(filename + '.data', 'rb') as f:
            data = f.read()
            print(data.hex())

            signature = self.private_key.sign(
                data,
                padding.PSS(
                    padding.MGF1(
                        hashes.SHA256()),
                        salt_length = padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )
            print(signature.hex())
            self.save_signature(filename, signature)
