
class User():
    def __init__(self, oid:int, username:str, password:str) -> None:
        self.oid:int = oid
        self.username:str = username
        self.password:str = password

    def __str__(self) -> str:
        return f"User: id={self.oid}, username='{self.username}'"

    def __eq__(self, other) -> bool:
        return self.oid == other.oid and self.username == other.username


class UserTable():
    def __init__(self) -> None:
        self._users:list[User] = []    # ---[*]-> [User]

    def insert(self, user) -> None:
        self._users.append(user)

    def find_by_id(self, oid:int):
        for user in self._users:
            if user.oid == oid:
                return user
        return None

    def find_all(self) -> list[User]:
        return self._users


if __name__ == '__main__':

    # Verify implementations
    bart1 = User(1, 'bart', 'EatMyShorts!')
    bart2 = User(1, 'bart', '#Kig%/5gT54$§')
    assert bart1 == bart2
    assert "User: id=1, username='bart'" == str(bart1)

    homer = User(3, 'homer', 'MoreDuff4Me!')
    marge = User(7, 'marge', 'Kh7gT.9/8#gH')

    table = UserTable()
    table.insert(homer)
    table.insert(marge)

    assert 'marge' == table.find_by_id(7).username
    assert 'homer' == table.find_by_id(3).username
    assert 2 == len(table.find_all())
