from morepath_app.app import App
from morepath_app.model import Document,User

@App.path(model=Document, path='documents/{id}')
def get_document(id):
   if id != 'foo':
      return None # not found
   return Document('foo', 'Foo document', 'FOO!')


@App.path(model=User, path='/users/{username}')
def get_user(username):
    return User.users.get(username)

