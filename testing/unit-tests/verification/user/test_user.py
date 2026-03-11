from user import User

def test_assert_each_property():
    user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

    # Verification (attribute by attribute)
    assert 7 == user.oid, 'different id'
    assert 'homer' == user.username, 'different username'
    assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == user.password, 'different password'


def test_custom_assert():
    user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

    # Verification (custom assert function)
    expected = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')
    assert_equal_user(expected, user)


# Custom assert function
def assert_equal_user(expected: User, actual: User) -> None:
    assert expected.oid == actual.oid, 'different object id'
    assert expected.username == actual.username, 'different username'
    assert expected.password == actual.password, 'different password'
