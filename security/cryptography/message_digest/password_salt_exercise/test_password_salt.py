import pytest
from password_salt import PasswordEncryption


@pytest.fixture
def encryption():
    return PasswordEncryption()


def test_encrypt(encryption):
    encrypted_password = encryption.encrypt("trink4bier!")
    assert type(encrypted_password) is bytes
    assert len(encrypted_password) == 48  # 16 bytes salt + 32 bytes SHA-256 digest


def test_verify(encryption):
    encrypted_password = bytes.fromhex(
        "e7f7c77cdc8eb67d0918153adc89fed4837bf136db5dab1a66d3365f56c652b"
        "b5937abecb0d81e1101f8a6dbc83c1fdc"
    )
    assert encryption.verify("trink4bier!", encrypted_password)


def test_encrypt_and_verify(encryption):
    encrypted_password = encryption.encrypt("trink4bier!")
    assert encryption.verify("trink4bier!", encrypted_password)


def test_wrong_password_not_verified(encryption):
    encrypted_password = encryption.encrypt("trink4bier!")
    assert not encryption.verify("wrongpassword", encrypted_password)
