import pytest

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Signature
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/index.html
# A private key can be used to sign a message.
# This allows anyone with the public key to verify that the message was created
# by someone who possesses the corresponding private key.


@pytest.fixture
def key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    public_key = private_key.public_key()
    return private_key, public_key


def test_sign_and_verify(key_pair):
    private_key, public_key = key_pair
    message = b"Some data we want to sign"
    print('Message   : ' + message.decode('utf-8'))

    # sign a message
    pss_padding = padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    )
    signature = private_key.sign(message, pss_padding, hashes.SHA256())
    # Probabilistic Signature Scheme (PSS) is a padding scheme designed
    # by Mihir Bellare and Phillip Rogaway.
    print('Signature: ' + signature.hex())

    # verify a message
    verify_pss_padding = padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    )
    public_key.verify(
        signature,
        message,
        verify_pss_padding,
        hashes.SHA256()
    )
    # If the signature does not match, verify() will raise an
    # InvalidSignature exception.
