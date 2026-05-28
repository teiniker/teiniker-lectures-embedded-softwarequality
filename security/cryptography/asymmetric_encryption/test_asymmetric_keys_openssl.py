from cryptography.hazmat.primitives import serialization


# Generate "openssl-private-key.pem" via openSSL
def test_load_private_key():
    with open("openssl-private-key.pem", "rb") as key_file:
        pk = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
        print('Private key: ' + str(pk))
        print('Public  key: ' + str(pk.public_key()))
        assert pk.key_size > 0


# Generate "openssl-public-key.pem" via openSSL
def test_load_public_key():
    with open("openssl-public-key.pem", "rb") as key_file:
        pubk = serialization.load_pem_public_key(
            key_file.read()
        )
        print('Public key: ' + str(pubk))
        assert pubk.key_size > 0
