from user_table import UserTable, User

class UserTableBuilder():
    def __init__(self):
        self._table = UserTable()

    def user(self, oid:int, username:str, password:str) -> 'UserTableBuilder':
        user = User(oid, username, password)
        self._table.insert(user)
        return self

    def build(self) -> UserTable:
        return self._table
