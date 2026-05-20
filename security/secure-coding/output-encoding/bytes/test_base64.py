import base64


def test_base64_encode():
    b = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
    encoded = base64.standard_b64encode(b)
    assert encoded == b'+c257ETY08GNQc3yauYSPA=='


def test_base64_decode():
    s = b'+c257ETY08GNQc3yauYSPA=='
    decoded = base64.standard_b64decode(s)
    assert decoded.hex() == 'f9cdb9ec44d8d3c18d41cdf26ae6123c'


def test_base64_url_encode():
    b = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
    encoded = base64.urlsafe_b64encode(b)
    assert encoded == b'-c257ETY08GNQc3yauYSPA=='


def test_base64_url_decode():
    s = b'-c257ETY08GNQc3yauYSPA=='
    decoded = base64.urlsafe_b64decode(s)
    assert decoded.hex() == 'f9cdb9ec44d8d3c18d41cdf26ae6123c'
