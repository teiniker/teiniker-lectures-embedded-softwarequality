import secrets
import hmac
import hashlib

KEY = bytes.fromhex("fce0ddc9bf4ad0f68d92af77b42b486bd10c27bc1b45a4c4929cda4f63bf0386")


def test_hmac():
    msg = bytes("This is a message.", 'utf-8')
    digest = hmac.new(KEY, msg, hashlib.sha256)
    # digest.update(bytes("another message", 'utf-8'))
    value = digest.hexdigest()
    assert len(value) == 64
    print('hmac = ' + value)


# The recommendation for HMAC is that the key size is identical to the output size
def test_generate_key():
    key_hex = secrets.token_hex(32)
    assert len(key_hex) == 64
    print(key_hex)
