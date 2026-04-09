import pytest
from user import User, ValidationError


def test_assert_each_property():
    user = User(7, "homer", "Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=")
    # Verification
    assert 7 == user.oid
    assert "homer" == user.username
    assert "Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=" == user.password


def test_assert_id_value():
    with pytest.raises(ValidationError):  # Verification
        User(-7, "homer", "Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=") # Exercise


def test_assert_username():
    with pytest.raises(ValidationError):
        User(7, "ho", "Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=")


def test_assert_password():
    with pytest.raises(ValidationError):
        User(7, "homer", "Kqq3")
