import base64


def test_base16_encode():
    b = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
    encoded = base64.b16encode(b)
    assert encoded == b'F9CDB9EC44D8D3C18D41CDF26AE6123C'


def test_base16_decode():
    s = b'F9CDB9EC44D8D3C18D41CDF26AE6123C'
    decoded = base64.b16decode(s)
    assert decoded.hex() == 'f9cdb9ec44d8d3c18d41cdf26ae6123c'
