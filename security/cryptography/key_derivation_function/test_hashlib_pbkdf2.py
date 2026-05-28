import secrets
from hashlib import pbkdf2_hmac


def test_pbkdf2():
    password = b'password'
    salt = secrets.token_bytes(16)
    iterations = 500000
    key_len = 32
    key = pbkdf2_hmac('sha256', password, salt, iterations, key_len)
    assert len(key) == key_len
    print(key.hex())
