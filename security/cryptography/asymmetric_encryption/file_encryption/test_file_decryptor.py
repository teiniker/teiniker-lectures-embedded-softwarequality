import pytest
from file_decryptor import FileDecryptor
from cryptography.hazmat.primitives import serialization


@pytest.fixture
def decryptor():
    with open("openssl-private-key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )
        print('Private key: ' + str(private_key))
    return FileDecryptor(private_key)


def test_load_bytes(decryptor):
    data = decryptor.load('secure.data')
    print(data)
    assert data.hex() == "000102030405060708090a0b0c0d0e0f"
