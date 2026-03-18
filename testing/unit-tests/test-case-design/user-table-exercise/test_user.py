import pytest

from user_table import User

@pytest.fixture
def user():
    return User(1, "bart", "EatMyShorts!")


def test_user_equality(user):
    bart2 = User(1, "bart", "#Kig%/5gT54$§")
    assert user == bart2

# TODO: Implement more tests for User 
