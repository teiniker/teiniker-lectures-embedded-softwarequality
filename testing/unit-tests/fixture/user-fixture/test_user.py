import pytest

from user import User, Mail

@pytest.fixture # Creation function
def user():
    mail = Mail('homer.simpson@springfield.com')
    return User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)


def test_inline_fixture(user):
    # Exercise + Verify
    assert 7 == user.oid
    assert 'homer' == user.username
    assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == user.password
    assert 'homer.simpson@springfield.com' == user.mail.adress


def test_implicit_fixture(user):
    # exercise

    # verify
    assert 7 == user.oid
    assert 'homer' == user.username
    assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == user.password
    assert 'homer.simpson@springfield.com' == user.mail.adress


def test_delegation_fixture(user):
    # exercise

    # verify
    assert 7 == user.oid
    assert 'homer' == user.username
    assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == user.password
    assert 'homer.simpson@springfield.com' == user.mail.adress


def test_modified_delegation_fixture(user):
    # setup
    user.password = 'SBiFOHaODQY65DJBS8vxsoihdknrtdKqq3lbODaQT4L='

    # exercise

    # verify
    assert 7 == user.oid
    assert 'homer' == user.username
    assert 'SBiFOHaODQY65DJBS8vxsoihdknrtdKqq3lbODaQT4L=' == user.password
    assert 'homer.simpson@springfield.com' == user.mail.adress
