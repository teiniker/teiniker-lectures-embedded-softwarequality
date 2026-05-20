import secrets


def test_random_token():
    iv = secrets.token_bytes(32)
    assert isinstance(iv, bytes)
    assert len(iv) == 32


def test_random_token_hex():
    iv = secrets.token_hex(32)
    assert isinstance(iv, str)
    assert len(iv) == 64  # 32 bytes -> 64 hex characters


def test_random_token_urlsafe():
    iv = secrets.token_urlsafe(32)
    assert isinstance(iv, str)
    assert len(iv) >= 32  # base64url encoding is longer than raw bytes
