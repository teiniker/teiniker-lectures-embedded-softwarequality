def test_encode():
    msg = 'message'
    b = msg.encode('utf-8')
    assert type(msg) is str
    assert type(b) is bytes


def test_decode():
    b = bytes.fromhex('6d657373616765')
    s = b.decode('utf-8')
    assert type(b) is bytes
    assert type(s) is str
    assert s == 'message'
