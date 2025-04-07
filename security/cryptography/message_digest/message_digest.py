import unittest
import hashlib

class MessageDigestTest(unittest.TestCase):

    def test_sha256(self):
        b = bytes("message", 'utf-8')
        digest = hashlib.sha256(b)
        hash = digest.hexdigest()
        self.assertEquals("ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d", hash)

    def test_sha256_update(self):
        digest = hashlib.sha256()
        b = bytes("message", 'utf-8')
        digest.update(b)
        hash = digest.hexdigest()
        self.assertEquals("ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d", hash)

    def test_sha512(self):
        b = bytes("message", 'utf-8')
        m = hashlib.sha512(b)
        hash = m.hexdigest()
        self.assertEquals("f8daf57a3347cc4d6b9d575b31fe6077e2cb487f60a96233c08cb479dbf31538cc915ec6d48bdbaa96ddc1a16db4f4f96f37276cfcb3510b8246241770d5952c", hash)

if __name__ == '__main__':
    unittest.main()
