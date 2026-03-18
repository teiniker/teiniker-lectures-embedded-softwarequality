import pytest

from user_table import User, UserTable


@pytest.fixture
def table():
    homer = User(3, "homer", "MoreDuff4Me!")
    marge = User(7, "marge", "Kh7gT.9/8#gH")
    table = UserTable()
    table.insert(homer)
    table.insert(marge)
    return table

def test_find_by_id(table):
    assert table.find_by_id(7).username == "marge"
    assert table.find_by_id(3).username == "homer"

# TODO: Implement more tests for UserTable
