import unittest
import secrets


class RandomNumberTest(unittest.TestCase):

    def test_random_token(self):
        iv = secrets.token_bytes(32)
        print(iv)
        print(iv.hex())

    def test_random_token_hex(self):
        iv = secrets.token_hex(32)
        print(iv)

    def test_random_token_urlsafe(self):
        iv = secrets.token_urlsafe(32)
        print(iv)


if __name__ == '__main__':
    unittest.main()
