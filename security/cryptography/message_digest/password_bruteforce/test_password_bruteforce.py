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
    hash_value = "04e77bf8f95cb3e1a36a59d1e93857c411930db646b46c218a0352e432023cf2"
    with open("wordlist.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()
        found = None
        for line in lines:
            if encryption.encrypt(line) == hash_value:
                found = line
                break
    assert found == "princess"
