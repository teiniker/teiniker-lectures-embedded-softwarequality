import pytest
from cryptography.hazmat.primitives import serialization
from file_encryptor import FileEncryptor


@pytest.fixture
def encryptor():
    with open("openssl-public-key.pem", "rb") as key_file:
        pubk = serialization.load_pem_public_key(
            key_file.read()
        )
    return FileEncryptor(pubk)


def test_save_bytes(encryptor):
    data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    encryptor.save('secure.data', data)
