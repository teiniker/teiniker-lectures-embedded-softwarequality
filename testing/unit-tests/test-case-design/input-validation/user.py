class ValidationError(Exception):
    pass

class User:
    def __init__(self, oid:int, username:str, password:str):
        if oid < 0:
            raise ValueError('Invalid object id: should be a positive number!')
        if len(username) < 5:
            raise ValueError('Invalid username: too short!')
        if len(password) < 12:
            raise ValidationError('Invalid password: too short!')

        self.oid = oid
        self.username = username
        self.password = password
