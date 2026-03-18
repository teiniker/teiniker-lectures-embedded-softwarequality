
class User():
    oid: int
    username: str
    password: str

    def __init__(self, oid: int, username: str, password: str) -> None:
        self.oid = oid
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f"User: id={self.oid}, username='{self.username}'"

    def __eq__(self, other) -> bool:
        return self.oid == other.oid and self.username == other.username


class UserTable():
    users: list[User]

    def __init__(self) -> None:
        self.users = []    # ---[*]-> [User]

    def insert(self, user: User) -> None:
        self.users.append(user)

    def find_by_id(self, oid: int) -> User | None:
        for user in self.users:
            if user.oid == oid:
                return user
        return None

    def find_all(self) -> list[User]:
        return self.users
