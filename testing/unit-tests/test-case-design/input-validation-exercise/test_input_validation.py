import pytest
from user import User, ValidationError


def test_assert_each_property():
    user = User(7, "homer", "Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=")

    # Verification
    assert 7 == user.oid
    assert "homer" == user.username
    assert "Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=" == user.password

# TODO: Add more test cases to cover the validation logic in the User class
