def test_encode():
    msg = 'message'
    b = msg.encode('utf-8')
    assert isinstance(msg, str)
    assert isinstance(b, bytes)


def test_decode():
    b = bytes.fromhex('6d657373616765')
    s = b.decode('utf-8')
    assert isinstance(b, bytes)
    assert isinstance(s, str)
    assert s == 'message'
