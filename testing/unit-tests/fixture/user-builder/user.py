class Mail:
    def __init__(self, address:str) -> None:
        self.adress = address


class User:
    def __init__(self, oid:int, username:str, password:str, mail:Mail) -> None:
        self.oid = oid
        self.username = username
        self.password = password
        self.mail = mail
