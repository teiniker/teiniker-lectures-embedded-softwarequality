import pytest
from file_encryptor import FileEncryptor


@pytest.fixture
def encryptor():
    # key = os.urandom(32)  # 256 bit key
    key = bytes.fromhex('a4f7802bd2b099fdd603abb5cc20a5402719f6d408975017950a021bb2f1ee52')
    print('key: ' + key.hex())
    # iv = os.urandom(16)  # equal to block size
    iv = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
    print(' iv : ' + iv.hex())
    return FileEncryptor(key, iv)


def test_save_bytes(encryptor):
    data = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
    encryptor.save('secure.data', data)


def test_load_bytes(encryptor):
    data = encryptor.load('secure.data')
    print(data)
    assert data.hex() == "000102030405060708090a0b0c0d0e0f"
