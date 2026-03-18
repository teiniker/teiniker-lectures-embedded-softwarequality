from user_table import User, UserTable


def test_find_by_id_returns_matching_user():
    homer = User(3, "homer", "MoreDuff4Me!")
    marge = User(7, "marge", "Kh7gT.9/8#gH")
    table = UserTable()
    table.insert(homer)
    table.insert(marge)
    assert table.find_by_id(7).username == "marge"
    assert table.find_by_id(3).username == "homer"


def test_find_by_id_returns_none_for_missing_user():
    table = UserTable()
    assert table.find_by_id(99) is None


def test_find_all_returns_all_inserted_users_in_order():
    table = UserTable()
    homer = User(3, "homer", "MoreDuff4Me!")
    marge = User(7, "marge", "Kh7gT.9/8#gH")
    table.insert(homer)
    table.insert(marge)
    users = table.find_all()
    assert len(users) == 2
    assert "homer" == users[0].username
    assert "marge" == users[1].username
