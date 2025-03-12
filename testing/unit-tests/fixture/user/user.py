class User:
    def __init__(self, oid, username, password, mail):
        self.oid = oid
        self.username = username
        self.password = password
        self.mail = mail

class Mail:
    def __init__(self, address):
        self.adress = address
