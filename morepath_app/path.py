from morepath_app.app import App
from morepath_app.model import Document,User,AddEmployee,UpdateEmployee
@App.path(model=Document, path='documents/{id}')
def get_document(id):
   if id != 'foo':
      return None # not found
   return Document('foo', 'Foo document', 'FOO!')



@App.path(model=User, path='/users/{username}')
def get_user(username):
    return User.users.get(username)

#http://127.0.0.1:5000/employees/add?eid=102&ename=Bob&edept=IT
@App.path(path='/employees/add', model=AddEmployee)
def get_add_employee():
    return AddEmployee()

@App.path(path='/employees/update', model=UpdateEmployee)
def get_add_employee():
    return UpdateEmployee()