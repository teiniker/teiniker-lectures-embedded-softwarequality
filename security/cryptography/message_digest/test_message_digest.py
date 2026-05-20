import hashlib


def test_sha1():
    b = bytes("message", 'utf-8')
    digest = hashlib.sha1(b)
    hash_value = digest.hexdigest()
    assert hash_value == "6f9b9af3cd6e8b8a73c2cdced37fe9f59226e27d"


def test_sha256():
    b = bytes("message", 'utf-8')
    digest = hashlib.sha256(b)
    hash_value = digest.hexdigest()
    assert hash_value == "ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d"


def test_sha256_update():
    digest = hashlib.sha256()
    b = bytes("message", 'utf-8')
    digest.update(b)
    hash_value = digest.hexdigest()
    assert hash_value == "ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d"


def test_sha512():
    b = bytes("message", 'utf-8')
    digest = hashlib.sha512(b)
    hash_value = digest.hexdigest()
    assert hash_value == "f8daf57a3347cc4d6b9d575b31fe6077e2cb487f60a96233c08cb479dbf31538cc915ec6d48bdbaa96ddc1a16db4f4f96f37276cfcb3510b8246241770d5952c"
