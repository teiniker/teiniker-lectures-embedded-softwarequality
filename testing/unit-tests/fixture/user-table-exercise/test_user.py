from user_table import User

def test_user_equality_ignores_password():
    user = User(1, "bart", "EatMyShorts!")
    bart = User(1, "bart", "#Kig%/5gT54$§")
    assert user == bart


def test_user_string_representation():
    user = User(1, "bart", "EatMyShorts!")
    assert str(user) == "User: id=1, username='bart'"
