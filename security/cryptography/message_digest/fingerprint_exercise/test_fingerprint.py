import pytest
from fingerprint import Fingerprint

@pytest.fixture
def fingerprint():
    return Fingerprint()


def test_from_bytes(fingerprint):
    data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    hash_value = fingerprint.from_bytes(data)
    assert hash_value == "be45cb2605bf36bebde684841a28f0fd43c69850a3dce5fedba69928ee3a8991"


def test_from_string(fingerprint):
    text = 'Pleased to meet you, hope you guess my name'
    hash_value = fingerprint.from_string(text)
    assert hash_value == "3b8be20de1d75d3087f5591b0687d9b3fd036a68b42dc27c5c9618a9bb72732e"


def test_from_file(fingerprint):
    hash_value = fingerprint.from_file("tux.jpeg")
    assert hash_value == "44eefdc0d4b5ea8d999d743e2651044f8033585ef3c97b2d69b508ad8c282cf1"
    # compare with: sha256sum tux.jpeg
