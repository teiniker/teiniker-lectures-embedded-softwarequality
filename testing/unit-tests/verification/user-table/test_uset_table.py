import pytest

from user_table import User, UserTable
from user_table_builder import UserTableBuilder

@pytest.fixture
def table() -> UserTable:
    return (
        UserTableBuilder()
        .user(3, 'Lisa', 'lKi8/hhgT')
        .user(7, 'Bart', 'kJ7&fRsd34%7')
        .build()
    )


def test_find_by_id_3(table):
    # Exercise
    actual = table.find_by_id(3)
    # Verify
    expected = User(3, 'Lisa', 'lKi8/hhgT')
    assert_equal_user(expected, actual)

def test_find_by_id_7(table):
    # Exercise
    actual = table.find_by_id(7)
    # Verify
    expected = User(7, 'Bart', 'kJ7&fRsd34%7')
    assert_equal_user(expected, actual)


def test_find_all(table):
    # Exercise
    users = table.find_all()
    # Verify
    assert len(users) == 2
    assert users[0].oid == 3
    assert users[1].oid == 7


def test_insert_user(table):
    # Exercise
    user = User(11, 'Homer', 'lKfDt54sss6')
    table.insert(user)
    # Verify
    assert len(table.find_all()) == 3


# Custom assertion method for comparing User objects
def assert_equal_user(expected: User, actual: User):
    assert expected.oid == actual.oid
    assert expected.username == actual.username
    assert expected.password == actual.password
