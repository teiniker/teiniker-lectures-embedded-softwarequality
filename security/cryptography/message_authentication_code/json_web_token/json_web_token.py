import unittest
import os
import jwt

class JsonWebTokenTest(unittest.TestCase):

    def test_secret_gen(self):
        self.secret = os.urandom(32).hex()
        print(f'key: {self.secret}')

    def test_encode(self):
        payload = {'iss': 'teini', 'sub': '123'}
        secret = '0dc939e138599cfccf6be87df8f7a47d6d79746ce1acd2a4d676f2c40e6e0c3d'
        token = jwt.encode(payload, secret, algorithm='HS256')
        print(f'jwt: {token}')

    def test_decode(self):
        token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ0ZWluaSIsInN1YiI6IjEyMyJ9.OOLIGPoPn17dnvn1XH0tfI11t6RJjvDuVXZlYWeerSQ'
        secret = '0dc939e138599cfccf6be87df8f7a47d6d79746ce1acd2a4d676f2c40e6e0c3d'
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        print(f'payload: {payload}')


if __name__ == '__main__':
    unittest.main()
