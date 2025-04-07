import unittest
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class SymmetricEncryptionTest(unittest.TestCase):

    def setUp(self):
        self.key = secrets.token_bytes(32)  # 256 bit key
        self.iv = secrets.token_bytes(16)   # equal to block size
        self.cipher = Cipher(algorithms.AES(self.key), modes.CTR(self.iv))

    def test_encryption_and_decryption(self):
        encryptor = self.cipher.encryptor()
        ct = encryptor.update(bytes("This is a secret message.",'utf-8'))
        encryptor.finalize()
        print(ct.hex())

        decryptor = self.cipher.decryptor()
        pt = decryptor.update(ct)
        decryptor.finalize()
        print(pt.hex())
        print(pt.decode('utf-8'))

# Without calling finalize(), the encryption and decryption process may 
# not be fully completed. finalize() typically flushes any remaining data, 
# especially if the algorithm requires block-aligned data.

if __name__ == '__main__':
    unittest.main()
