import pytest
from hex_string import HexString


def test_value():
    assert HexString('AA').value == 'AA'
    assert HexString('FF').value == 'FF'
    assert HexString('00').value == '00'
    assert HexString('9999').value == '9999'
    assert HexString('FFFF').value == 'FFFF'


def test_equality():
    assert HexString('AA') == HexString('AA')
    assert HexString('FF') != HexString('AA')


def test_hash():
    assert hash(HexString('AA')) == hash(HexString('AA'))
    assert hash(HexString('FF')) != hash(HexString('AA'))

def test_str():
    assert str(HexString('AA')) == 'AA'

def test_immutability():
    h = HexString('AA')
    with pytest.raises(AttributeError):
        h._value = 'FF'


def test_invalid_too_short():
    with pytest.raises(ValueError):
        HexString('A')
    with pytest.raises(ValueError):
        HexString('0')


def test_invalid_too_long():
    with pytest.raises(ValueError):
        HexString('AAAAA')
    with pytest.raises(ValueError):
        HexString('00000')


def test_invalid_out_of_range():
    with pytest.raises(ValueError):
        HexString('@@')
    with pytest.raises(ValueError):
        HexString('GG')
    with pytest.raises(ValueError):
        HexString('::')
