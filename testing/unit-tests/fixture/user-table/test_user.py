import pytest
from user_table import User

@pytest.fixture
def user():
    return User(1, "bart", "EatMyShorts!")


def test_user_equality_ignores_password(user):
    bart = User(1, "bart", "#Kig%/5gT54$§")
    assert user == bart


def test_user_string_representation(user):
    assert str(user) == "User: id=1, username='bart'"
