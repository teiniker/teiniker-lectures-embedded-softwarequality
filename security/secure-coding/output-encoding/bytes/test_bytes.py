def test_string_types():
    s1 = 'message'
    s2 = b'message'
    assert isinstance(s1, str)
    assert isinstance(s2, bytes)


def test_constructor():
    msg = "message"
    b = bytes(msg, 'utf-8')
    assert isinstance(b, bytes)
    assert b == b'message'


def test_encode():
    b = "message".encode('utf-8')
    assert isinstance(b, bytes)
    assert b == b'message'


def test_fromhex():
    hex_str = 'f9cdb9ec44d8d3c18d41cdf26ae6123c'
    b = bytes.fromhex(hex_str)
    assert isinstance(b, bytes)
    assert b == b'\xf9\xcd\xb9\xecD\xd8\xd3\xc1\x8dA\xcd\xf2j\xe6\x12<'


def test_to_hex():
    b = b'\xf9\xcd\xb9\xecD\xd8\xd3\xc1\x8dA\xcd\xf2j\xe6\x12<'
    hex_str = b.hex()
    assert isinstance(hex_str, str)
    assert hex_str == 'f9cdb9ec44d8d3c18d41cdf26ae6123c'


def test_bytes_to_list():
    b = b'\xf9\xcd\xb9\xecD\xd8\xd3\xc1\x8dA\xcd\xf2j\xe6\x12<'
    l = list(b)
    assert isinstance(l, list)
    assert l == [249, 205, 185, 236, 68, 216, 211, 193, 141, 65, 205, 242, 106, 230, 18, 60]
