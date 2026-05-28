import pytest

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Generating private and public key
@pytest.fixture
def key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    public_key = private_key.public_key()
    return private_key, public_key


def test_save_and_load_private_key(key_pair):
    private_key, _ = key_pair

    # Save private key
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private_key.pem', 'wb') as f:
        f.write(pem)

    # Load private key
    with open("private_key.pem", "rb") as key_file:
        pk = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
        print('Private key: ' + str(pk))
        print('Public  key: ' + str(pk.public_key()))
        assert pk.key_size == 4096


def test_save_and_load_public_key(key_pair):
    _, public_key = key_pair

    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(pem)

    # Load public key
    with open("public_key.pem", "rb") as key_file:
        pubk = serialization.load_pem_public_key(
            key_file.read()
        )
        print('Public key: ' + str(pubk))
        assert pubk.key_size == 4096
