import bcrypt


def test_bcrypt_encrypt_and_verify():
    password = b's$cret12'
    salt = bcrypt.gensalt()  # randomly generated salt
    hashed = bcrypt.hashpw(password, salt)
    assert isinstance(hashed, bytes)
    assert bcrypt.checkpw(password, hashed)


def test_bcrypt_wrong_password_not_verified():
    password = b's$cret12'
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    assert not bcrypt.checkpw(b'wrongpassword', hashed)
