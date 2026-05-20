import pytest
from password_iterations import PasswordEncryption


@pytest.fixture
def encryption():
    return PasswordEncryption()


def test_encrypt(encryption):
    encrypted_password = encryption.encrypt("trink4bier!", 1024)
    assert type(encrypted_password) is bytes
    assert len(encrypted_password) == 48  # 16 bytes salt + 32 bytes SHA-256 digest


def test_verify(encryption):
    encrypted_password = bytes.fromhex(
        "7eda9a8030dfb2abc70a45a5548b9d557b6d64c0ece13f44fad1bc621aa9b34e"
        "5249c14165335605bf135dd25454c73b"
    )
    assert encryption.verify("trink4bier!", encrypted_password, 1024)


def test_encrypt_and_verify(encryption):
    encrypted_password = encryption.encrypt("trink4bier!", 1024)
    assert encryption.verify("trink4bier!", encrypted_password, 1024)


def test_wrong_password_not_verified(encryption):
    encrypted_password = encryption.encrypt("trink4bier!", 1024)
    assert not encryption.verify("wrongpassword", encrypted_password, 1024)
