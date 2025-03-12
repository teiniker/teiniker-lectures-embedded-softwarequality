from user import User
from user import Mail

class UserBuilder:
    def __init__(self):
        # set default values for the user
        self._oid = 7
        self._username = 'homer'
        self._password_hash = 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8='
        self._email_address = 'homer.simpson@springfield.com'

    def oid(self, oid: int):
        self._oid = oid
        return self

    def username(self, username: str):
        self._username = username
        return self

    def password(self, password_hash: str):
        self._password_hash = password_hash
        return self

    def email(self, email_address: str):
        self._email_address = email_address
        return self

    def build(self):
        mail = Mail(self._email_address)
        user = User(self._oid, self._username, self._password_hash, mail)
        return user
