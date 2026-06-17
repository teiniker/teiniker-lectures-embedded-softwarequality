import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

import pytest


@pytest.fixture
def cipher():
    key = secrets.token_bytes(32)  # 256 bit key
    nonce = secrets.token_bytes(16)   # equal to block size
    return Cipher(algorithms.AES(key), modes.CTR(nonce))


def test_encryption_and_decryption(cipher):
    plaintext = bytes("This is a secret message.", 'utf-8')

    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext)
    encryptor.finalize()
    print(ct.hex())

    decryptor = cipher.decryptor()
    pt = decryptor.update(ct)
    decryptor.finalize()
    print(pt.decode('utf-8'))

    assert pt == plaintext

# Without calling finalize(), the encryption and decryption process may
# not be fully completed. finalize() typically flushes any remaining data,
# especially if the algorithm requires block-aligned data.
