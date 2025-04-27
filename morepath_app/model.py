class Document(object):
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content


class User(object):
    users = {}
    def __init__(self, username, fullname, email):
        self.username = username
        self.fullname = fullname
        self.email = email



    @classmethod
    def add_user(cls,user):
        cls.users[user.username] = user


faassen = User('faassen', 'Martijn Faassen', 'faassen@startifact.com')
bob = User('bob', 'Bob Bobsled', 'bob@example.com')
sa=User.add_user(faassen)
sa=User.add_user(bob)