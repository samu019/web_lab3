from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id_, username, password):
        self.id = id_
        self.username = username
        self.password = password

users = {
    "user": User(1, "user", "qwerty")
}

def get_user(username):
    return users.get(username)