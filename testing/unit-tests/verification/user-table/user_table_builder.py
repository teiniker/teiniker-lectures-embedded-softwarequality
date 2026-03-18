from user_table import UserTable, User

class UserTableBuilder():
    def __init__(self):
        self.table = UserTable()

    def user(self, oid:int, username:str, password:str) -> 'UserTableBuilder':
        user = User(oid, username, password)
        self.table.insert(user)
        return self

    def build(self) -> UserTable:
        return self.table
