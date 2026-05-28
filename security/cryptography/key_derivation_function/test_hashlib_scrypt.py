import secrets
from hashlib import scrypt


def test_scrypt():
    salt = secrets.token_bytes(16)
    password = b'password'
    key_len = 32
    key = scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=key_len)
    assert len(key) == key_len
    print(key.hex())
