import pytest

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from data_file_verifier import DataFileVerifier


@pytest.fixture
def verifier():
    with open("openssl-public-key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    return DataFileVerifier(public_key)


def test_verify_valid(verifier):
    verifier.verify_data_file('measurement')


def test_verify_invalid(verifier):
    with pytest.raises(InvalidSignature):
        verifier.verify_data_file('measurement2')
