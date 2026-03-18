import pytest

from user_table import User

@pytest.fixture
def user():
    return User(1, "bart", "EatMyShorts!")


def test_user_equality(user):
    bart2 = User(1, "bart", "#Kig%/5gT54$§")
    assert user == bart2

def test_user_equality_with_non_user(user):
    assert (user == "") is False

def test_user_string_representation(user):
    assert str(user) == "User: id=1, username='bart'"
