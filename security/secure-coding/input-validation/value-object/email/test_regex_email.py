import pytest
from email_string import EMail


def test_value():
    assert EMail('user@example.com').value == 'user@example.com'
    assert EMail('firstname.lastname@domain.org').value == 'firstname.lastname@domain.org'


def test_equality():
    assert EMail('user@example.com') == EMail('user@example.com')
    assert EMail('user@example.com') != EMail('other@example.com')


def test_hash():
    assert hash(EMail('user@example.com')) == hash(EMail('user@example.com'))
    assert hash(EMail('user@example.com')) != hash(EMail('other@example.com'))


def test_str():
    assert str(EMail('user@example.com')) == 'user@example.com'


def test_immutability():
    e = EMail('user@example.com')
    with pytest.raises(AttributeError):
        e._value = 'other@example.com'


def test_invalid_missing_at():
    with pytest.raises(ValueError):
        EMail('invalid.email')


def test_invalid_missing_domain():
    with pytest.raises(ValueError):
        EMail('user@')


def test_invalid_missing_tld():
    with pytest.raises(ValueError):
        EMail('user@domain')
