from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class DataFileVerifier:
    def __init__(self, public_key)->None:
        self.public_key = public_key

    def load_signature(self, filename:str)->bytes:
        with open(filename + '.signature', 'rb') as f:
            signature = f.read()
            return signature

    def verify_data_file(self, filename:str)->None:
        with open(filename + '.data', 'rb') as f:
            data = f.read()
            print('Data: ' + data.hex())

            signature = self.load_signature(filename)

            self.public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf = padding.MGF1(hashes.SHA256()),
                    salt_length = padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            # If the signature does not match, 
            # verify() will raise an InvalidSignature exception.

