import os
import jwt


def test_secret_gen():
    secret = os.urandom(32).hex()
    assert len(secret) == 64
    print(f'key: {secret}')


def test_encode():
    payload = {'iss': 'teini', 'sub': '123'}
    secret = '0dc939e138599cfccf6be87df8f7a47d6d79746ce1acd2a4d676f2c40e6e0c3d'
    token = jwt.encode(payload, secret, algorithm='HS256')
    assert token is not None
    print(f'jwt: {token}')


def test_decode():
    token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ0ZWluaSIsInN1YiI6IjEyMyJ9.OOLIGPoPn17dnvn1XH0tfI11t6RJjvDuVXZlYWeerSQ'
    secret = '0dc939e138599cfccf6be87df8f7a47d6d79746ce1acd2a4d676f2c40e6e0c3d'
    payload = jwt.decode(token, secret, algorithms=['HS256'])
    assert payload == {'iss': 'teini', 'sub': '123'}
    print(f'payload: {payload}')
