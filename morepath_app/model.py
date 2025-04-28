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


class Employee(object):
    employees={}
    def __init__(self, eid,ename,edept):
        self.eid=eid
        self.ename=ename
        self.edept=edept

    @classmethod
    def add_employee(cls, emp):
        cls.employees[emp.eid] = emp

    @classmethod
    def update_employee(cls,eid,edept):
        employee_to_update=cls.employees[eid]
        employee_to_update.edept=edept


class AddEmployee(object):
    pass

class UpdateEmployee(object):
    pass

faassen = User('faassen', 'Martijn Faassen', 'faassen@startifact.com')
bob = User('bob', 'Bob Bobsled', 'bob@example.com')
sa=User.add_user(faassen)
sa=User.add_user(bob)

new_emp = Employee(eid="101", ename="vaibhav", edept="IT")
new_emp1 = Employee(eid="102", ename="pravi", edept="HR")
Employee.add_employee(new_emp)
Employee.add_employee(new_emp1)