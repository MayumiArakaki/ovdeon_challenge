from utils.PasswordFormat import PasswordFormat

class Restaurant():

    def __init__(self, id, username=None, password=None) -> None:
        self.id = id
        self.username = username
        self.password = password

    def to_JSON(self):
        return {
            'id':self.id,
            'username': self.username,
            'password': self.password
            #'password': PasswordFormat.convert_password(self.password)
            }

