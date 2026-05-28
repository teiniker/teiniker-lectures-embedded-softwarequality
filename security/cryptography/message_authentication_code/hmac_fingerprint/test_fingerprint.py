import pytest
from fingerprint import Fingerprint


@pytest.fixture
def fingerprint():
    # The key consists of 32 random bytes
    key = "fce0ddc9bf4ad0f68d92af77b42b486bd10c27bc1b45a4c4929cda4f63bf0386"
    return Fingerprint(key)


def test_from_bytes(fingerprint):
    data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    mac = fingerprint.from_bytes(data)
    print(f'mac of byte array = {mac}')
    assert mac == "9864b5619d85f2c0d8025bdfcf375d9f1c95aca25fea7fa235053f2f60925086"


def test_from_string(fingerprint):
    text = 'Pleased to meet you, hope you guess my name'
    mac = fingerprint.from_string(text)
    print(f'mac of string    = {mac}')
    assert mac == "a88533ad56b2acaa1d569cae1a9a6785b0a5cd2dc266ee601dc33667ff9daa6f"


def test_from_file(fingerprint):
    filename = "./tux.jpeg"
    mac = fingerprint.from_file(filename)
    print(f'mac of file      = {mac}')
    assert mac == "0f23c00edc0ae15fea5834e0ea0b447d549938fc5f267920741caf2dce1c5490"
