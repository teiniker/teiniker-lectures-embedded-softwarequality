import unittest
import secrets
import hmac
import hashlib


class MessageAuthenticationCodeTest(unittest.TestCase):

    def setUp(self):
        self.key = bytes.fromhex("fce0ddc9bf4ad0f68d92af77b42b486bd10c27bc1b45a4c4929cda4f63bf0386")
        print('key = ' + str(self.key))

    def test_HMAC(self):
        msg = bytes("This is a message.",'utf-8')
        digest = hmac.new(self.key, msg, hashlib.sha256)
        # digest.update(bytes("another message", 'utf-8'))
        value = digest.hexdigest()
        print('hmac = ' + value)

    # The recommendation for HMAC is that the key size is identical to the output size
    def test_generate_key(self):
        key_hex = secrets.token_hex(32)
        print(key_hex)


if __name__ == '__main__':
    unittest.main()
