def test_constructor():
    msg = "message"
    b = bytearray(msg, 'utf-8')
    assert type(b) is bytearray
    assert b == b'message'


def test_fromhex():
    hex_str = 'f9cdb9ec44d8d3'
    b = bytearray.fromhex(hex_str)
    assert type(b) is bytearray
    assert b == b'\xf9\xcd\xb9\xec\x44\xd8\xd3'


def test_to_hex():
    b = b'\xf9\xcd\xb9\xec\x44\xd8\xd3'
    hex_str = b.hex()
    assert type(hex_str) is str
    assert hex_str == 'f9cdb9ec44d8d3'


def test_list_to_bytearray():
    prime_numbers = [2, 3, 5, 7]
    byte_array = bytearray(prime_numbers)
    assert type(byte_array) is bytearray
    assert list(byte_array) == prime_numbers
