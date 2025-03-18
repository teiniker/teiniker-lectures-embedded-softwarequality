class User():
    def __init__(self, oid, username, password):
        self.oid = oid
        self.username = username
        self.password = password

    def __str__(self):
        return f"User: id={self.oid}, username='{self.username}'"

    def __eq__(self, other):
        return self.oid == other.oid and self.username == other.username


class UserTable():
    def __init__(self):
        self._users = []    # ---[*]-> [User]

    def insert(self, user):
        self._users.append(user)

    def find_by_id(self, oid):
        for user in self._users:
            if user.oid == oid:
                return user
        return None

    def find_all(self):
        return self._users
