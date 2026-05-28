import pytest
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


@pytest.fixture
def key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    public_key = private_key.public_key()
    return private_key, public_key


def test_encryption_and_decryption(key_pair):
    private_key, public_key = key_pair
    message = b"Some data we want to encrypt"
    print('Message   : ' + message.decode('utf-8'))
    print('Message   : ' + message.hex())

    # encrypt a message
    oaep_padding = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
    ciphertext = public_key.encrypt(message, oaep_padding)
    print('Ciphertext: ' + ciphertext.hex())

    # decrypt a message
    oaep_padding = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
    plaintext = private_key.decrypt(ciphertext, oaep_padding)
    print('Plaintext : ' + plaintext.decode('utf-8'))

    assert plaintext == message
