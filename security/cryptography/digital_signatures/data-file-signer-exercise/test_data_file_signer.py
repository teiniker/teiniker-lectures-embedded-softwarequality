import pytest

from cryptography.hazmat.primitives import serialization
from data_file_signer import DataFileSigner


@pytest.fixture
def signer():
    with open("openssl-private-key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )
        print('Private key: ' + str(private_key))
    return DataFileSigner(private_key)


def test_signing(signer):
    signer.sign_data_file('measurement')
