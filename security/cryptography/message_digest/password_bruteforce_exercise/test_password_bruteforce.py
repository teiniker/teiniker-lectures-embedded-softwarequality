import pytest
from password_bruteforce import PasswordEncryption

@pytest.fixture
def encryption():
    return PasswordEncryption()


def test_encrypt(encryption):
    hash_value = encryption.encrypt("trink4bier!")
    assert hash_value == "f806c28ecedb097b27e4d93a08a3e2fdb1b7e0766b4c6b73c0b9c162b9e5ecc2"


def test_verify(encryption):
    hash_value = "f806c28ecedb097b27e4d93a08a3e2fdb1b7e0766b4c6b73c0b9c162b9e5ecc2"
    assert encryption.verify("trink4bier!", hash_value) is True


def test_bruteforce(encryption):
    # TODO
    pass
