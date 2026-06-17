import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

import pytest


@pytest.fixture
def key_and_nonce():
    key = secrets.token_bytes(32)   # 256-bit key
    nonce = secrets.token_bytes(12)  # 96-bit nonce (recommended for GCM)
    return key, nonce


def test_encryption_and_decryption(key_and_nonce):
    key, nonce = key_and_nonce
    plaintext = bytes("This is a secret message.", 'utf-8')

    encryptor = Cipher(algorithms.AES(key), modes.GCM(nonce)).encryptor()
    ct = encryptor.update(plaintext)
    encryptor.finalize()
    tag = encryptor.tag  # 16-byte authentication tag produced after finalize()
    print(ct.hex())
    print(tag.hex())

    # GCM verifies the authentication tag during finalize(); raises InvalidTag on mismatch
    decryptor = Cipher(algorithms.AES(key), modes.GCM(nonce, tag)).decryptor()
    pt = decryptor.update(ct)
    decryptor.finalize()
    print(pt.decode('utf-8'))

    assert pt == plaintext
